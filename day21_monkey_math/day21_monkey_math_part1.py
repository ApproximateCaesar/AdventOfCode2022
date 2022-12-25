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
    return number


root_number = get_monkey_number('root')
print(f'The number that root will yell is {root_number}')



