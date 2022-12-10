# https://adventofcode.com/2022/day/1

with open("day1_calorie_counting/day1_input.txt") as f:
    input_txt = f.read().splitlines()  # creates list of strings, with empty string separating elves

    # find total calories for each elf
    total_calories = []
    current_elf_calories = 0
    for item in input_txt:
        if item == '':  # current elf inventory finished
            total_calories.append(current_elf_calories)
            current_elf_calories = 0  # new elf inventory
        else:
            current_elf_calories += int(item)
    total_calories.append(current_elf_calories)  # add last entry
    print(f"The maximum total calories carried by an elf is: {max(total_calories)}")

    total_calories.sort(reverse=True)
    print(f"The top three elves are carrying total calories {sum(total_calories[:3])}")





