# https://adventofcode.com/2022/day/15

import re

def manhattan_dist(p1, p2):
    """Returns the manhattan distance between points p1 and p2."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# might have to adjust this for discrete segments instead of real intervals
def segment_union_length(segments):
    """Returns the length of the union of line segments using Klee's algorithm.
    Code from https://iq.opengenus.org/klee-algorithm/"""
    n = len(segments)

    # Initialing list to store the points
    points = [None] * (n * 2)

    # Store points in a list and mark endpoints as true
    for i in range(n):
        points[i * 2] = (segments[i][0], False)
        points[i * 2 + 1] = (segments[i][1], True)

    # sort the points in ascending order
    points = sorted(points, key=lambda x: x[0])

    total_length = 0  # total length of the union of segments
    num_open_startpoints = 0  # The number of open (excess) startpoints

    # Traversing through the points
    for i in range(0, n * 2):

        # Adding length from previous to current point
        if (i > 0) & (points[i][0] > points[i - 1][0]) & (num_open_startpoints > 0):
            total_length += (points[i][0] - points[i - 1][0])

        # If this is an endpoint decrement counter by 1
        if points[i][1]:
            num_open_startpoints -= 1
        # If this is a startpoint increment counter by 1
        else:
            num_open_startpoints += 1
    return total_length


PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day15_beacon_exclusion_zone/day15_example_input.txt") as f:
    input_txt = f.read().splitlines()

sensors = []  # sensor coordinates
beacons = []  # closest beacon coordinates
beacon_dists = []  # distances from sensor to closest beacon (exclusion radius)
for line in input_txt:
    matches = list(map(int, re.findall(r'-?\d+', line)))
    sensors.append(tuple(matches[0:2]))
    beacons.append(tuple(matches[2:4]))
    beacon_dists.append(manhattan_dist(sensors[-1], beacons[-1]))

y = 10  # y level we care about
num_excluded = 0  # number of points which are excluded (covered by a sensor)
for sensor, beacon_dist in zip(sensors, beacon_dists):
    if sensor[1] - beacon_dist <= y <= sensor[1] + beacon_dist:  # if exclusion radius intersections level y
        # TODO find segment of y level in exclusion radius
        # TODO add segment to list
        # TODO compute length of segment union
        # TODO dont count any points that contain already discovered beacons
print(f'The number of excluded points (that arent a discovered beacon) in row {y} is ')