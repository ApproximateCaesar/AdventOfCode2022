# https://adventofcode.com/2022/day/18

from collections import deque

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day18_boiling_boulders/day18_input.txt") as f:
    input_txt = f.read().splitlines()

droplet = set([tuple(map(int, cube.split(','))) for cube in input_txt])

droplet_surface_area = 0
for cube in droplet:
    # check for neighbouring cubes
    adjacent_points = set()
    for i in (-1, 1):
        adjacent_points.add((cube[0] + i, cube[1], cube[2]))
        adjacent_points.add((cube[0], cube[1] + i, cube[2]))
        adjacent_points.add((cube[0], cube[1], cube[2] + i))
    # count the number of sides not directly adjacent to another cube
    droplet_surface_area += 6 - len(adjacent_points.intersection(droplet))

print(f'The surface area of the droplet is {droplet_surface_area}')

# part 2 ###
exterior_surface_area = 0

# get droplet bounding box
x_min, x_max = min([cube[0] for cube in droplet]), max([cube[0] for cube in droplet])
y_min, y_max = min([cube[1] for cube in droplet]), max([cube[1] for cube in droplet])
z_min, z_max = min([cube[2] for cube in droplet]), max([cube[2] for cube in droplet])

# BFS
start = (x_min - 1, y_min, z_min)  # starting point just outside bounding box ensures it is exterior
visited = set()  # visited cubes will be exterior air (or water/steam when lava hits pond)
queue = deque()

visited.add(start)
queue.appendleft(start)

while queue:  # while queue not empty
    v = queue.pop()

    adjacent_points = set()  # adjacent exterior points that are in bounds
    for i in (-1, 1):
        if x_min - 1 <= v[0] + i <= x_max + 1:
            adjacent_points.add((v[0] + i, v[1], v[2]))
        if y_min - 1 <= v[1] + i <= y_max + 1:
            adjacent_points.add((v[0], v[1] + i, v[2]))
        if z_min - 1 <= v[2] + i <= z_max + 1:
            adjacent_points.add((v[0], v[1], v[2] + i))
        adjacent_air_points = adjacent_points.difference(droplet)  # remove adjacent points that are droplet cubes

    exterior_surface_area += len(adjacent_points.intersection(droplet))

    for w in adjacent_air_points:
        if w not in visited:
            visited.add(w)
            queue.appendleft(w)

print(f'The exterior droplet surface area is {exterior_surface_area}')
