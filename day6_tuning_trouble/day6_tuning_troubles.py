# https://adventofcode.com/2022/day/6

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day6_tuning_trouble/day6_input.txt") as f:
    buffer = f.read()

print(buffer)
MARKER_LENGTH = 14  # change this for part 1 or 2
marker_found = False
i = MARKER_LENGTH
while not marker_found:
    if len(set(buffer[i - MARKER_LENGTH:i])) == MARKER_LENGTH:
        marker_found = True
    else:
        i += 1
print(f"The first marker appears after character {i}")
