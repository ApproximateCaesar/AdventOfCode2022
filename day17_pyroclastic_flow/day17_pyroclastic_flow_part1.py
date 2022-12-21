# https://adventofcode.com/2022/day/17

"""
Note on coordinates: Coordinates take (0, 0) as bottom-left of chamber wall (the plus sign in example).
This is the naive but intuitive solution and won't be fast enough for part 2.
"""
import time

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day17_pyroclastic_flow/day17_input.txt") as f:
    jet_pattern = f.read().strip('\n')

# each rock type is given as a list of points, with coords relative to the bottom-left of their bounding box
ROCK_TYPES = ({(0, 0), (1, 0), (2, 0), (3, 0)},  # horizontal line
              {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},  # plus sign
              {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},  # backwards L
              {(0, 0), (0, 1), (0, 2), (0, 3)},  # vertical line
              {(0, 0), (0, 1), (1, 0), (1, 1)})  # square

NUM_ROCKS = 2022  # number of rocks that will fall
CHAMBER_WIDTH = 7  # width of the chamber rocks are falling in
INITIAL_ROCK_X = 3  # initial x pos of bottom-left of rock bounding box
INITIAL_ROCK_Y_OFFSET = 4  # initial y offset above top of rock tower
rock_tower = set()  # tower consisting of rocks that have come to rest
tower_height = 0  # height of the rock tower
next_jet_index = 0  # index in the jet pattern of the next jet that will occur
jet_pattern_length = len(jet_pattern)  # length of the jet pattern


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
for i in range(NUM_ROCKS):
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
        next_jet_index += 1

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
    # print_chamber(rock_tower, tower_height, falling_rock, CHAMBER_WIDTH)

print(time.time() - start_time, "seconds")
print(f'The height of the rock tower after {NUM_ROCKS} rocks is {tower_height}')

