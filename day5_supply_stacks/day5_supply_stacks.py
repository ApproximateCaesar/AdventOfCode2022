# https://adventofcode.com/2022/day/5

import re

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day5_supply_stacks/day5_input.txt") as f:
    input_txt = f.read().splitlines()

# create the initial crate configuration as an array of stacks
INITIAL_MAX_STACK_HEIGHT = 8
NUM_STACKS = 9
initial_crate_config = input_txt[:INITIAL_MAX_STACK_HEIGHT]
stacks = [list() for i in range(NUM_STACKS)]  # initialise array of stacks

for i in reversed(range(INITIAL_MAX_STACK_HEIGHT)):  # go through rows bottom to top
    for match in re.finditer(r"[A-Z]", initial_crate_config[i]):  # find crates in each row
        stacks[(match.start() - 1) // 4].append(match.group())  # add crate to correct stack

# rearrange crates according to procedure
procedure = input_txt[INITIAL_MAX_STACK_HEIGHT + 2:]
procedure = [list(map(int, re.findall(r"\d+", step))) for step in procedure]  # as list of list of int

# cratemover 9000 (use deque instead of list for stacks for speedup)
# for step in procedure:
#     for i in range(step[0]):  # move step[0] items
#         stacks[step[2] - 1].append(stacks[step[1] - 1].pop())  # from stack step[1] to stack step[2]

# cratemover 9001
for step in procedure:
    for i in range(step[0], 0, -1):  # move step[0] items
        stacks[step[2] - 1].append(stacks[step[1] - 1].pop(-i))  # from stack step[1] to stack step[2]

print(stacks)
top_crates = [stack[-1] for stack in stacks]
top_crates_msg = ''.join(top_crates)
print(f"The top crates are {top_crates_msg}")

