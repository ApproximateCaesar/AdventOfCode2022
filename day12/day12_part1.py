# https://adventofcode.com/2022/day/12

from collections import deque
from copy import deepcopy

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day12/day12_input.txt") as f:
    valuemap = f.read().splitlines()

WIDTH = len(valuemap[0])  # horizontal width of the valuemap
HEIGHT = len(valuemap)  # vertical height of valuemap
valuemap = [list(row) for row in valuemap]

heightmap = deepcopy(valuemap)
for i, row in enumerate(valuemap):
    for j, value in enumerate(row):
        if value == 'S':
            heightmap[i][j] = ord('a')
        elif value == 'E':
            heightmap[i][j] = ord('z')
        else:
            heightmap[i][j] = ord(valuemap[i][j])


# get valid (reachable) neighbours for vertex v
def get_valid_neighbours(v):
    valid_neighbours = []
    if v[0] - 1 >= 0 and heightmap[v[0] - 1][v[1]] <= heightmap[v[0]][v[1]] + 1:
        valid_neighbours.append((v[0] - 1, v[1]))
    if v[0] + 1 < HEIGHT and heightmap[v[0] + 1][v[1]] <= heightmap[v[0]][v[1]] + 1:
        valid_neighbours.append((v[0] + 1, v[1]))
    if v[1] - 1 >= 0 and heightmap[v[0]][v[1] - 1] <= heightmap[v[0]][v[1]] + 1:
        valid_neighbours.append((v[0], v[1] - 1))
    if v[1] + 1 < WIDTH and heightmap[v[0]][v[1] + 1] <= heightmap[v[0]][v[1]] + 1:
        valid_neighbours.append((v[0], v[1] + 1))
    return valid_neighbours


# BFS
visited = set()
queue = deque()

START = (0, 0)  # (20, 0)
visited.add(START)
queue.appendleft(START)

parents = {}
found = False

while queue and not found:  # while queue not empty and we havent found goal
    v = queue.pop()

    if valuemap[v[0]][v[1]] == 'E':
        found = True
        print(v)
    else:
        valid_neighbours = get_valid_neighbours(v)
        for w in valid_neighbours:
            if w not in visited:
                visited.add(w)
                parents[w] = v
                queue.appendleft(w)

# Get shortest path length
path_length = 0
while v != START:
    path_length += 1
    v = parents[v]
print(f"The shortest path from S to E has length {path_length}")

