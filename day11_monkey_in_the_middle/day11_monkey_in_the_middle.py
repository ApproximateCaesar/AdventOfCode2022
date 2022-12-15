# https://adventofcode.com/2022/day/11

# Am I writing a parser only to have it read in seven monkeys? Bruh.


# example ###
NUM_ROUNDS = 20
monkey_items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]  # starting items for each monkey
monkey_operations = ['* 19', '+ 6', '** 2', '+ 3']  # worry operation for inspecting at item
monkey_tests = [[23, 2, 3], [19, 2, 0], [13, 1, 3], [17, 0, 1]]  # divisor to test, monkey if true, monkey if false
num_inspections = [0, 0, 0, 0]  # total number of items each monkey inspects

for throwing_round in range(NUM_ROUNDS):
    for turn in range(len(monkey_items)):
        for item in monkey_items[turn]:  # inspect and throw items
            new_worry_level = eval(str(item) + monkey_operations[turn]) // 3
            if new_worry_level % monkey_tests[turn][0] == 0:
                monkey_items[monkey_tests[turn][1]].append(new_worry_level)
            else:
                monkey_items[monkey_tests[turn][2]].append(new_worry_level)
        num_inspections[turn] += len(monkey_items[turn])  # count items inspected
        monkey_items[turn] = []  # remove items since we threw them

monkey_business = sorted(num_inspections)[-1] * sorted(num_inspections)[-2]
print(f'The level of monkey business is {monkey_business}')

# part 1 ###
NUM_ROUNDS = 20
monkey_items = [[99, 67, 92, 61, 83, 64, 98], [78, 74, 88, 89, 50],  # starting items for each monkey
                [98, 91], [59, 72, 94, 91, 79, 88, 94, 51], [95, 72, 78],
                [76], [69, 60, 53, 89, 71, 88], [72, 54, 63, 80]]
monkey_operations = ['* 17', '* 11', '+ 4', '** 2',  # worry operation for inspecting at item
                     '+ 7', '+ 8', '+ 5', '+ 3']
monkey_tests = [[3, 4, 2], [5, 3, 5], [2, 6, 4], [13, 0, 5],  # divisor to test, monkey if true, monkey if false
                [11, 7, 6], [17, 0, 2], [19, 7, 1], [7, 1, 3]]
num_inspections = [0, 0, 0, 0, 0, 0, 0, 0]  # total number of items each monkey inspects

for throwing_round in range(NUM_ROUNDS):
    for turn in range(len(monkey_items)):
        for item in monkey_items[turn]:  # inspect and throw items
            new_worry_level = eval(str(item) + monkey_operations[turn]) // 3
            if new_worry_level % monkey_tests[turn][0] == 0:
                monkey_items[monkey_tests[turn][1]].append(new_worry_level)
            else:
                monkey_items[monkey_tests[turn][2]].append(new_worry_level)
        num_inspections[turn] += len(monkey_items[turn])  # count items inspected
        monkey_items[turn] = []  # remove items since we threw them

monkey_business = sorted(num_inspections)[-1] * sorted(num_inspections)[-2]
print(f'The level of monkey business is {monkey_business}')

# part 2 ###
# uses chinese remainder theorem which I totally forgot https://en.wikipedia.org/wiki/Chinese_remainder_theorem
NUM_ROUNDS = 10000
monkey_items = [[99, 67, 92, 61, 83, 64, 98], [78, 74, 88, 89, 50],  # starting items for each monkey
                [98, 91], [59, 72, 94, 91, 79, 88, 94, 51], [95, 72, 78],
                [76], [69, 60, 53, 89, 71, 88], [72, 54, 63, 80]]
monkey_operations = ['* 17', '* 11', '+ 4', '** 2',  # worry operation for inspecting at item
                     '+ 7', '+ 8', '+ 5', '+ 3']
monkey_tests = [[3, 4, 2], [5, 3, 5], [2, 6, 4], [13, 0, 5],  # divisor to test, monkey if true, monkey if false
                [11, 7, 6], [17, 0, 2], [19, 7, 1], [7, 1, 3]]
num_inspections = [0, 0, 0, 0, 0, 0, 0, 0]  # total number of items each monkey inspects

for throwing_round in range(NUM_ROUNDS):
    for turn in range(len(monkey_items)):
        for item in monkey_items[turn]:  # inspect and throw items
            new_worry_level = eval(str(item) + monkey_operations[turn]) % (3*5*2*13*11*17*19*7)
            if new_worry_level % monkey_tests[turn][0] == 0:
                monkey_items[monkey_tests[turn][1]].append(new_worry_level)
            else:
                monkey_items[monkey_tests[turn][2]].append(new_worry_level)
        num_inspections[turn] += len(monkey_items[turn])  # count items inspected
        monkey_items[turn] = []  # remove items since we threw them

monkey_business = sorted(num_inspections)[-1] * sorted(num_inspections)[-2]
print(f'The level of monkey business is {monkey_business}')
