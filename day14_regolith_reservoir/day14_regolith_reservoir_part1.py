# https://adventofcode.com/2022/day/14

def print_cave(rock, sand):
    """visualise the cave."""
    obstacles = rock.union(sand)
    min_x = min([p[0] for p in obstacles])
    max_x = max([p[0] for p in obstacles])
    min_y = min([p[1] for p in obstacles])
    max_y = max([p[1] for p in obstacles])

    for y in range(min_y, max_y + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            if (x, y) == (500, 0):
                row += '+'
            elif (x, y) in rock:
                row += '#'
            elif (x, y) in sand:
                row += 'o'
            else:
                row += '.'
        print(row)
    print('\n')

def get_line_of_points(p1, p2):
    """Returns a list of points (tuples) representing a straight horizontal/vertical line from p1 to p2."""
    line = []
    if p1[1] == p2[1]:  # horizontal line
        line = [(x, p1[1]) for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)]
    elif p1[0] == p2[0]:  # vertical line
        line = [(p1[0], y) for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)]
    return line


PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day14_regolith_reservoir/day14_input.txt") as f:
    cave_scan = f.read().splitlines()

# convert cave scan to list of paths, each being a list of points
cave_scan = [[tuple(map(int, point.split(','))) for point in path.split(' -> ')] for path in cave_scan]

# I will use sets to store positions since this avoids having to manually resize a 2d array
rock = set()  # positions of rock
sand = set()  # positions of sand at rest

# add rock positions to the set
for path in cave_scan:
    for i in range(len(path) - 1):
        rock.update(get_line_of_points(path[i], path[i + 1]))

print_cave(rock, sand)
max_y_rock = max([int(p[1]) for p in rock])  # maximum y pos of a rock, after which comes the abyss

# can the while loop logic be simplified?
sand_lost = False  # whether sand has been lost to the abyss
while not sand_lost:
    at_rest = False  # whether the current sand unit has come to rest
    sand_unit_pos = [500, 0]  # sand enters cave at point (500, 0)
    obstacles = rock.union(sand)
    while not (at_rest or sand_lost):
        if sand_unit_pos[1] > max_y_rock:  # sand will fall into the abyss
            sand_lost = True
        elif (sand_unit_pos[0], sand_unit_pos[1] + 1) not in obstacles:
            sand_unit_pos[1] += 1  # move down
        elif (sand_unit_pos[0] - 1, sand_unit_pos[1] + 1) not in obstacles:
            # move down-left
            sand_unit_pos[1] += 1
            sand_unit_pos[0] -= 1
        elif (sand_unit_pos[0] + 1, sand_unit_pos[1] + 1) not in obstacles:
            # move down-right
            sand_unit_pos[1] += 1
            sand_unit_pos[0] += 1
        else:  # sand unit cant move any further
            at_rest = True
            sand.add(tuple(sand_unit_pos))
    print_cave(rock, sand)

print(f'The number of units of sand at rest before sand is lost is {len(sand)}')