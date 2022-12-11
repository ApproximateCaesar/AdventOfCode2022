# https://adventofcode.com/2022/day/3

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day3_rucksack_reorganisation/day3_input.txt") as f:
    input_txt = f.read().splitlines()

# Part 1 ###
total_priority = 0
for rucksack in input_txt:
    first_compartment = set(rucksack[:len(rucksack) // 2])
    second_compartment = set(rucksack[len(rucksack) // 2:])
    (common_item,) = first_compartment.intersection(second_compartment)

    # compute priority
    if common_item.islower():
        priority = ord(common_item) - ord("a") + 1
    else:
        priority = ord(common_item) - ord("A") + 27
    total_priority += priority

print(f"The sum of priorities of common item types is {total_priority}")

# Part 2 ###
total_badge_priority = 0
for i in range(0, len(input_txt), 3):
    elf1, elf2, elf3 = set(input_txt[i]), set(input_txt[i+1]), set(input_txt[i+2])
    (badge,) = elf1.intersection(elf2, elf3)

    # compute priority
    if badge.islower():
        priority = ord(badge) - ord("a") + 1
    else:
        priority = ord(badge) - ord("A") + 27
    total_badge_priority += priority

print(f"The sum of priorities of badges is {total_badge_priority}")
