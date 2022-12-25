# https://adventofcode.com/2022/day/21

import re

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day21_monkey_math/day21_input.txt") as f:
    monkey_descriptions = f.read().splitlines()

monkeys = {}
for desc in monkey_descriptions:
    monkey_name = desc[0:4]
    if match := re.search(r'\d+', desc):
        number = int(match.group(0))
        monkeys[monkey_name] = {'operation': 'yell',
                                'number': number}
    else:
        monkeys[monkey_name] = {'operation': desc[11],
                                'inputs': [desc[6:10], desc[13:17]]}

humn_ancestors = set()  # set containing all monkeys in the tree whose job depends on humn (its ancestors)
monkey_numbers = {}  # dict of the number that each monkey yells


def is_humn_ancenstor(monkey_name):
    monkey = monkeys[monkey_name]
    if monkey_name == 'humn':
        humn_ancestors.add(monkey_name)
        return True
    elif monkey['operation'] == 'yell':  # leaf node
        return False
    else:
        child1, child2 = monkey['inputs']
        if is_humn_ancenstor(child1) or is_humn_ancenstor(child2):
            humn_ancestors.add(monkey_name)
            return True
        else:
            return False


def get_monkey_number(monkey_name):
    monkey = monkeys[monkey_name]
    if monkey['operation'] == 'yell':
        number = monkey['number']
    elif monkey['operation'] == '/':  # handle / separately because we want integer division
        number = get_monkey_number(monkey['inputs'][0]) // get_monkey_number(monkey['inputs'][1])
    else:
        number = eval("get_monkey_number(monkey['inputs'][0])" +
                      monkey['operation'] +
                      "get_monkey_number(monkey['inputs'][1])")
    monkey_numbers[monkey_name] = number
    return number


def get_child_desired_number(monkey_name, desired_number, child):
    other_child = 1 if child == 0 else 0
    monkey = monkeys[monkey_name]
    if monkey['operation'] == '+':
        child_desired_number = desired_number - monkey_numbers[monkey['inputs'][other_child]]
    elif monkey['operation'] == '-':
        if child == 0:
            child_desired_number = desired_number + monkey_numbers[monkey['inputs'][1]]
        else:
            child_desired_number = monkey_numbers[monkey['inputs'][0]] - desired_number
    elif monkey['operation'] == '*':
        child_desired_number = desired_number // monkey_numbers[monkey['inputs'][other_child]]
    elif monkey['operation'] == '/':
        if child == 0:
            child_desired_number = desired_number * monkey_numbers[monkey['inputs'][1]]
        else:
            child_desired_number =  monkey_numbers[monkey['inputs'][0]] // desired_number
    return child_desired_number


def get_humn_number(monkey_name, desired_number):
    monkey = monkeys[monkey_name]
    if monkey_name == 'humn':
        return desired_number  # the number that humn should yell
    elif monkey_name == 'root':
        child0, child1 = monkey['inputs']
        if child0 in humn_ancestors:
            return get_humn_number(child0, monkey_numbers[child1])  # child0 should yell child1 number
        else:
            return get_humn_number(child1, monkey_numbers[child0])  # child1 should yell child0 number
    else:
        child0, child1 = monkey['inputs']
        if child0 in humn_ancestors:
            child0_desired_number = get_child_desired_number(monkey_name, desired_number, 0)
            return get_humn_number(child0, child0_desired_number)
        else:
            child1_desired_number = get_child_desired_number(monkey_name, desired_number, 1)
            return get_humn_number(child1, child1_desired_number)


is_humn_ancenstor('root')  # calculate humn ancestors
print(humn_ancestors)
get_monkey_number('root')  # calculate monkey numbers
print(monkey_numbers)
humn_number = get_humn_number('root', None)
print(f'The number I should yell is {humn_number}')


