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

# part 2 ###  apparently this part can be done in O(n)


# checks whether x,y indices are within the tree grid bounds
def in_bounds(x, y):
    is_in_bounds = True if 0 <= x < WIDTH and 0 <= y < HEIGHT else False
    return is_in_bounds


# gets view distance for the tree at i, j. x_step and y_step determine view direction
def get_view_dist(i, j, x_step, y_step):
    view_dist = 0  # always start with 1 from adjacent tree
    x = j + x_step
    y = i + y_step
    while in_bounds(x, y) and tree_heights[y][x] < tree_heights[i][j]:  # while view not blocked
        view_dist += 1
        x += x_step
        y += y_step
    if in_bounds(x, y):
        view_dist += 1  # add final tree if we finish in bounds
    return view_dist


max_scenic_score = 0
for i in range(1, HEIGHT - 1):  # don't include (literal) edge cases because they will have scenic score 0
    for j in range(1, WIDTH - 1):
        view_dist_left = get_view_dist(i, j, -1, 0)
        view_dist_right = get_view_dist(i, j, 1, 0)
        view_dist_up = get_view_dist(i, j, 0, -1)
        view_dist_down = get_view_dist(i, j, 0, 1)

        scenic_score = view_dist_left * view_dist_right * view_dist_up * view_dist_down
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(f'The max scenic score is {max_scenic_score}')





