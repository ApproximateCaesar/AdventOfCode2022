# https://adventofcode.com/2022/day/13

from itertools import zip_longest

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day13_distress_signal/day13_input.txt") as f:
    packet_strings = f.read().splitlines()

# convert packet strings to lists using eval
left_packets = []
right_packets = []
for i in range(0, len(packet_strings), 3):
    left_packets.append(eval(packet_strings[i]))
    right_packets.append(eval(packet_strings[i + 1]))

# The < operator in python actually already compares sequences (recursively) using lexicographical ordering:
# https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types
# But this only works if the values are of the same type (we never compare an int to a list) so I could
# make everything be nested in a list, but then I may as well write my own comparison function.


# whether left_value < right_value using lexicographical order. None implies values are equal
def is_correct_order(left_value, right_value):
    correct_order = None
    if type(left_value) is int and type(right_value) is int:
        if left_value < right_value:
            correct_order = True
        elif left_value > right_value:
            correct_order = False
    elif type(left_value) is list and type(right_value) is list:
        for l, r in zip_longest(left_value, right_value, fillvalue=-1):  # pad shorter list with -1
            if is_correct_order(l, r) is not None:  # difference in values
                correct_order = is_correct_order(l, r)
                break
    # convert either value to list
    elif type(left_value) is int:
        correct_order = is_correct_order([left_value], right_value)
    elif type(right_value) is int:
        correct_order = is_correct_order(left_value, [right_value])
    return correct_order


correct_pair_index_sum = 0
for i in range(len(left_packets)):
    if is_correct_order(left_packets[i], right_packets[i]):
        correct_pair_index_sum += i + 1

print(f'The sum of indices of correct packet pairs is {correct_pair_index_sum}')

# part 2 ###
# This wants us to sort the packets to find the indices of two divider packets,
# but it's easier to just see how many packets come before the dividers without fully sorting -
# basically checking their height in a max heap.

packets = []
for i in range(0, len(packet_strings), 3):
    packets.append(eval(packet_strings[i]))
    packets.append(eval(packet_strings[i + 1]))

divider1, divider2 = [[2]], [[6]]
index1, index2 = 1, 1  # indices of dividers
for packet in packets:
    if is_correct_order(packet, divider1):
        index1 += 1
    if is_correct_order(packet, divider2):
        index2 += 1

decoder_key = index1 * (index2 + 1)  # add 1 to index 2 to account for div 1 coming before div 2
print(f'The decoder key is {decoder_key}')
