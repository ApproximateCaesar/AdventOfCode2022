# https://adventofcode.com/2022/day/17

"""
Note on coordinates: Coordinates take (0, 0) as bottom-left of chamber wall (the plus sign in example).
To compute the height of the tower for part 2 we notice that the jet pattern and rock types both cycle,
and so after some time we expect a repeating structure to the tower. The cycle seems to occur after
jet_pattern_length steps (why???) and have length jet_pattern_length * num_rock_types (which makes sense).
We find the
"""
import time

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day17_pyroclastic_flow/day17_example_input.txt") as f:
    jet_pattern = f.read().strip('\n')

# each rock type is given as a list of points, with coords relative to the bottom-left of their bounding box
ROCK_TYPES = ({(0, 0), (1, 0), (2, 0), (3, 0)},  # horizontal line
              {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},  # plus sign
              {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},  # backwards L
              {(0, 0), (0, 1), (0, 2), (0, 3)},  # vertical line
              {(0, 0), (0, 1), (1, 0), (1, 1)})  # square
NUM_ROCK_TYPES = len(ROCK_TYPES)
NUM_ROCKS = 2022  # number of rocks that will fall
CHAMBER_WIDTH = 7  # width of the chamber rocks are falling in
INITIAL_ROCK_X = 3  # initial x pos of bottom-left of rock bounding box
INITIAL_ROCK_Y_OFFSET = 4  # initial y offset above top of rock tower
rock_tower = set()  # tower consisting of rocks that have come to rest
tower_height = 0  # height of the rock tower
next_jet_index = 0  # index in the jet pattern of the next jet that will occur
jet_pattern_length = len(jet_pattern)  # length of the jet pattern
# the cycle length (in number of jets) before the jet pattern and rock types repeat
cycle_length = jet_pattern_length * NUM_ROCK_TYPES


def print_chamber(rock_tower, tower_height, falling_rock, chamber_width):
    for y in range(tower_height + 10, -1, -1):
        row = ''
        for x in range(chamber_width + 2):
            if (x, y) in rock_tower:
                row += '#'
            elif (x, y) in falling_rock:
                row += '@'
            elif y == 0:
                if x == 0 or x == chamber_width + 1:
                    row += '+'
                else:
                    row += '-'
            elif x == 0 or x == chamber_width + 1:
                row += '|'
            else:
                row += '.'
        print(row)
    print('\n')


def get_shifted_rock(x_offset, y_offset, rock):
    """Returns a new rock shifted by x and y offset."""
    shifted_rock = set()
    for point in rock:
        shifted_rock.add((point[0] + x_offset, point[1] + y_offset))
    return shifted_rock


def in_bounds(rock):
    is_in_bounds = True
    for point in rock:
        if not (0 < point[0] <= CHAMBER_WIDTH and point[1] > 0):
            is_in_bounds = False
            break
    return is_in_bounds


start_time = time.time()
jets_occurred = 0  # number of jets that have occurred
i = 0  # number of rocks that have fallen
cycle_number = 0  # which cycle we are in, starting from 1
cycle_length_in_rocks = 0  # cycle length in number of rocks fallen
cycle_offset_in_rocks = 0  # the number of rocks that fall before the first cycle begins
cycle_tower_height = []  # tower height after each rock is added during a cycle
tower_height_offset = 0  # tower height at start of first cycle
while cycle_number < 2:
    # place rock in correct starting position
    falling_rock = get_shifted_rock(INITIAL_ROCK_X, tower_height + INITIAL_ROCK_Y_OFFSET, ROCK_TYPES[i % 5])
    at_rest = False  # Whether the current rock has come to rest
    while not at_rest:
        # get pushed by one unit by jet
        if jet_pattern[next_jet_index % jet_pattern_length] == '<':  # left
            shifted_falling_rock = get_shifted_rock(-1, 0, falling_rock)
        else:  # right
            shifted_falling_rock = get_shifted_rock(1, 0, falling_rock)
        if shifted_falling_rock.isdisjoint(rock_tower) and in_bounds(shifted_falling_rock):  # no collision
            falling_rock = shifted_falling_rock

        if jets_occurred % cycle_length == jet_pattern_length:  # new cycle started
            # print(i, jets_occurred % cycle_length, i % NUM_ROCK_TYPES, next_jet_index % jet_pattern_length)
            cycle_number += 1
            # record offset when first cycle starts
            if cycle_number == 1:
                cycle_offset_in_rocks = i
                tower_height_offset = tower_height
            elif cycle_number == 2:  # TODO remove?
                cycle_length_in_rocks = i - cycle_offset_in_rocks

        # fall downward one unit
        shifted_falling_rock = get_shifted_rock(0, -1, falling_rock)
        if shifted_falling_rock.isdisjoint(rock_tower) and in_bounds(shifted_falling_rock):  # no collision
            falling_rock = shifted_falling_rock
        else:
            at_rest = True
            rock_tower.update(falling_rock)
            top_of_rock = max([point[1] for point in falling_rock])
            if top_of_rock > tower_height:
                tower_height = top_of_rock
        jets_occurred += 1
        next_jet_index += 1

        # record tower height for each rock added during a cycle
        if cycle_number == 1:
            cycle_tower_height.append(tower_height - tower_height_offset)

    i += 1
    # print_chamber(rock_tower, tower_height, falling_rock, CHAMBER_WIDTH)

print(time.time() - start_time, "seconds")
num_completed_cycles = (NUM_ROCKS - cycle_offset_in_rocks) // cycle_length_in_rocks
remaining_height = cycle_tower_height[(NUM_ROCKS - cycle_offset_in_rocks) % cycle_length_in_rocks]
print(remaining_height)
tower_height = tower_height_offset + num_completed_cycles * cycle_tower_height[-1] + remaining_height
print(f'The height of the rock tower after {NUM_ROCKS} rocks is {tower_height}')
print(cycle_offset_in_rocks, cycle_length_in_rocks)
print(cycle_tower_height[-1], tower_height_offset)

