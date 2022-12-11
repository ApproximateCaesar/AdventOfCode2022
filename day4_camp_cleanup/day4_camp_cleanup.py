# https://adventofcode.com/2022/day/4

import re
import numpy as np

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day4_camp_cleanup/day4_input.txt") as f:
    input_txt = f.read()

section_assignments = re.findall(r"\d+", input_txt)  # extract ids
section_assignments = list(map(int, section_assignments))  # convert to ints
section_assignments = np.array(section_assignments).reshape(-1, 4).tolist()  # split up by pairs

num_subset_pairs = 0
for pair in section_assignments:
    if pair[0] >= pair[2] and pair[1] <= pair[3]:  # first is subset
        num_subset_pairs += 1
    elif pair[0] <= pair[2] and pair[1] >= pair[3]:  # second is subset
        num_subset_pairs += 1

print(f"The number of pairs that are subsets are {num_subset_pairs}")

num_overlap_pairs = 0
for pair in section_assignments:
    if pair[1] >= pair[2] and pair[0] <= pair[3]:
        num_overlap_pairs += 1

print(f"The number of pairs that overlap are {num_overlap_pairs}")
