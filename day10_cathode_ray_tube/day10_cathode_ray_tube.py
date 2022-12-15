# https://adventofcode.com/2022/day/10

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day10_cathode_ray_tube/day10_input.txt") as f:
    program = f.read().splitlines()

addx_length = 2  # number of cycles to complete addx
signal_strengths = []
X = 1  # the cpu register
cycle = 1  # which cycle we are in
for line in program:
    if line[:4] == 'noop':
        if (cycle - 20) % 40 == 0:  # cycle we are interested in
            signal_strengths.append(cycle * X)
        cycle += 1
    elif line[:4] == 'addx':
        for i in range(addx_length):
            if (cycle - 20) % 40 == 0:  # cycle we are interested in
                signal_strengths.append(cycle * X)
            cycle += 1
        X += int(line[5:])

print(f'The sum of signal strengths is {sum(signal_strengths)}')

# part 2 ###
X = 1  # the cpu register
cycle = 1  # which cycle we are in
row = ''  # row of pixels on CRT
for line in program:
    if line[:4] == 'noop':
        if X - 1 <= (cycle - 1) % 40 <= X + 1:
            row += '#'
        else:
            row += '.'
        if cycle % 40 == 0:
            print(row)
            row = ''
        cycle += 1
    elif line[:4] == 'addx':
        for i in range(addx_length):
            if X - 1 <= (cycle - 1) % 40 <= X + 1:
                row += '#'
            else:
                row += '.'
            if cycle % 40 == 0:
                print(row)
                row = ''
            cycle += 1
        X += int(line[5:])

