# https://adventofcode.com/2022/day/22

"""Note: Points are given as row, column coordinates starting from zero at top left"""

import re

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day22_monkey_map/day22_input.txt") as f:
    input_txt = f.read().splitlines()

PATH_INDEX = 201  # 13  # index of the line containing the path
board = input_txt[0:PATH_INDEX - 1]
NUM_COLS = max(len(row) for row in board)  # number of columns in the board
walls = set()  # set of points on the board that are walls
# lists containing (lower, upper) indices for each row and column in the board
row_bounds = [[None, None] for _ in range(len(board))]
col_bounds = [[None, None] for _ in range(NUM_COLS)]
for i, row in enumerate(board):
    for j, tile in enumerate(row):
        if tile == '.' or tile == '#':  # tile is part of the board
            if row_bounds[i][0] is None:
                row_bounds[i][0] = j  # get lower bound
            row_bounds[i][1] = j  # update upper bound
            if col_bounds[j][0] is None:
                col_bounds[j][0] = i  # get lower bound
            col_bounds[j][1] = i  # update upper bound
        if tile == '#':
            walls.add((i, j))

path = input_txt[PATH_INDEX]
movements = list(map(int, re.findall(r'\d+', path)))
rotations = re.findall(r'[A-Z]', path)


def inbounds(pos, row_bounds):
    if 0 <= pos[0] < len(row_bounds):
        low, upp = row_bounds[pos[0]]
        if low <= pos[1] <= upp:
            return True
    else:
        return False


facing = 0  # which direction we are facing: right = 0, and we increase by 1 going clockwise
step_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # which step to take for each direction one can face
pos = (0, row_bounds[0][0])  # current row, column position
for i in range(len(movements)):
    # move:
    num_steps = movements[i]
    step_direction = step_directions[facing]
    step = 0
    for step in range(num_steps):  # TODO check steps off by 1 error
        next_pos = (pos[0] + step_direction[0], pos[1] + step_direction[1])
        if not inbounds(next_pos, row_bounds):  # wrap around if needed
            if facing == 0:  # moving right
                next_pos = (pos[0], row_bounds[pos[0]][0])  # wrap around to lower row bound
            elif facing == 2:  # moving left
                next_pos = (pos[0], row_bounds[pos[0]][1])  # wrap around to upper row bound
            elif facing == 1:  # moving down
                next_pos = (col_bounds[pos[1]][0], pos[1])  # wrap around to lower col bound
            elif facing == 3:  # moving up
                next_pos = (col_bounds[pos[1]][1], pos[1])  # wrap around to upper col bound
        if next_pos in walls:
            break
        else:
            pos = next_pos

    # rotate:
    if i < len(rotations):  # one less rotation than movement so we must check index
        if rotations[i] == 'L':
            facing = (facing - 1) % 4
        else:
            facing = (facing + 1) % 4


print(f'The final password is {1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing}')



