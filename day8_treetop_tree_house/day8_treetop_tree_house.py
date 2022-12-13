# https://adventofcode.com/2022/day/8

# is it possible to do part 1 in better than O(number of trees)?

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day8_treetop_tree_house/day8_input.txt") as f:
    tree_heights = f.read().splitlines()

HEIGHT, WIDTH = len(tree_heights), len(tree_heights[0])  # height and width of grid
tree_heights = [[int(col) for col in list(row)] for row in tree_heights]  # convert to 2d integer array
visible = [[False for col in range(WIDTH)] for row in range(HEIGHT)]

#  check if visible from left or right
for i in range(HEIGHT):
    tallest_tree = -1
    for j in range(WIDTH):
        if tree_heights[i][j] > tallest_tree:
            visible[i][j] = True
            tallest_tree = tree_heights[i][j]
    tallest_tree = -1
    for j in reversed(range(WIDTH)):
        if tree_heights[i][j] > tallest_tree:
            visible[i][j] = True
            tallest_tree = tree_heights[i][j]


#  check if visible from top or bottom
for j in range(WIDTH):
    tallest_tree = -1
    for i in range(HEIGHT):
        if tree_heights[i][j] > tallest_tree:
            visible[i][j] = True
            tallest_tree = tree_heights[i][j]
    tallest_tree = -1
    for i in reversed(range(HEIGHT)):
        if tree_heights[i][j] > tallest_tree:
            visible[i][j] = True
            tallest_tree = tree_heights[i][j]

# count number of visible trees
print(f'{sum(map(sum, visible))} trees are visible from outside the grid.')

# part 2 ###  apparently this can also be done in O(n)
scenic_score = [[1 for col in range(WIDTH)] for row in range(HEIGHT)]

