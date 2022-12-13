# https://adventofcode.com/2022/day/7

import re

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day7_no_space_left_on_device/day7_input.txt") as f:
    input_txt = f.read().splitlines()


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.file_size = 0
        self.total_size = None

    def add_child(self, child):
        self.children.append(child)


# create file tree
root = Directory('/', None)  # create root directory
current_dir = root
for line in input_txt[1:]:
    if line[0:4] == '$ cd':  # change directory
        if line[5:] == '..':  # move to parent
            current_dir = current_dir.parent
        else:  # move to child
            new_dir = Directory(name=line[5:], parent=current_dir)  # create child
            current_dir.add_child(new_dir)  # link child
            current_dir = new_dir  # move to child
    elif file_size := re.match(r'\d+', line):  # is a file
        current_dir.file_size += int(file_size.group(0))


directory_sizes = []
# compute directory sizes
def compute_dir_size(current_dir):
    if not current_dir.children:  # if dir has no children
        dir_size = current_dir.file_size
    else:  # has children
        dir_size = current_dir.file_size  # file contributions
        for child in current_dir.children:  # child contributions
            dir_size += compute_dir_size(child)
    current_dir.total_size = dir_size
    global directory_sizes
    directory_sizes.append(dir_size)
    return dir_size


# sum dir sizes <= 100000
compute_dir_size(root)
directory_sizes.sort()
print(directory_sizes)
total_below_100000 = 0
i = 0
while directory_sizes[i] <= 100000:
    total_below_100000 += directory_sizes[i]
    i += 1
print(f'The sum of dir sizes of at most 100000 is {total_below_100000}')

# part 2 ###
size_to_free = 30000000 - (70000000 - root.total_size)
print(f'Min space we must free up: {size_to_free}')

i = len(directory_sizes)
while directory_sizes[i - 1] >= size_to_free:
    i -= 1
print(f'The smallest directory we could delete has size {directory_sizes[i]}')
