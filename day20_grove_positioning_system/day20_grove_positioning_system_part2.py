# https://adventofcode.com/2022/day/20

"""Array approach in O(n^2). Linked lists would be faster?
My array representation isn't the same as the sample output, but is the same up to rotation,
so my final answer should be correct."""

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day20_grove_positioning_system/day20_input.txt") as f:
    encrypted_list = f.read().splitlines()

encrypted_list = list(map(int, encrypted_list))  # encrypted list of numbers
KEY = 811589153
encrypted_list = [KEY * num for num in encrypted_list]
n = len(encrypted_list)  # number of numbers in the list
decrypted_indices = list(range(n))  # indices of the numbers once the list is decrypted
ZERO_INDEX = 3093  # index of the single zero in the encrypted list

for mix in range(10):
    for i in range(n):
        number = encrypted_list[i]
        if number == 0:
            continue
        old_index = decrypted_indices[i]
        new_index = old_index + number  # get new index
        # adjust for odd wrapping around behaviour
        if new_index < 0 or new_index >= n - 1:
            new_index = new_index % (n - 1)
        elif new_index == 0:
            new_index = (new_index - 1) % n

        if new_index == old_index:
            continue

        for j in range(n):  # update indices of other numbers (i.e. shift other numbers)
            if old_index < new_index:
                if old_index <= decrypted_indices[j] <= new_index:
                    decrypted_indices[j] -= 1  # shift numbers left
            else:
                if new_index <= decrypted_indices[j] <= old_index:
                    decrypted_indices[j] += 1  # shift numbers right

        decrypted_indices[i] = new_index  # move number by updating index

        # print(f'moving {number} from index {old_index} to {new_index}')
decrypted_list = [k[0] for k in sorted(zip(encrypted_list, decrypted_indices), key=lambda x: x[1])]
    # print(decrypted_list)

coord_sum = 0
for i in (1000, 2000, 3000):
    coord_sum += decrypted_list[(decrypted_indices[ZERO_INDEX] + i) % n]

#print(decrypted_list)
print(f'The sum of the grove coordinates is {coord_sum}')



    

