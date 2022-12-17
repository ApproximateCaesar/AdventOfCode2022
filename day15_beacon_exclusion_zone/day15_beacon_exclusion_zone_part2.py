# https://adventofcode.com/2022/day/15

"""I couldn't get my part 1 solution to efficiently generalise to part 2,
 so I am using a completely different approach: search in a small grid around intersection
 points of sensor exclusion zone boundaries, because we know the distress
 beacon must be near one of these points (it will be bounded by intersecting zone boundaries).
 Using a small grid is just a hack that stops me from having to consider every geometrical case
 and also lets me ignore the arbitrary rounding that happened in computing intersection points
 This method also assumes the beacon isn't at the very edge of the search area."""

import re


def manhattan_dist(p1, p2):
    """Returns the manhattan distance between points p1 and p2."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_possible_intersection_points(sensors, beacon_dists, search_bound):
    """Returns a list of points within the search bounds which are
    possible intersection points of the sensor exclusion zones.
    This is done by extending the zone boundaries as lines with slope +-1 and finding all intersections.
    This will include many extraneous intersections but is much easier than
    computing only actual intersections."""
    intersection_points = []
    line_def_points = []  # points used to define exclusion zones (top and bottom of diamond shape)
    for i, sensor in enumerate(sensors):
        line_def_points.append((sensor[0], sensor[1] + beacon_dists[i]))
        line_def_points.append((sensor[0], sensor[1] - beacon_dists[i]))
    for (x1, y1) in line_def_points:
        for (x2, y2) in line_def_points:
            intersection_point = ((x1 + x2 + y1 - y2) // 2, (x1 - x2 + y1 + y2) // 2)
            if 0 <= intersection_point[0] <= search_bound and 0 <= intersection_point[1] <= search_bound:
                intersection_points.append(intersection_point)
    return intersection_points



PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day15_beacon_exclusion_zone/day15_input.txt") as f:
    input_txt = f.read().splitlines()

sensors = []  # sensor coordinates
beacons = []  # closest beacon coordinates
beacon_dists = []  # distances from sensor to closest beacon (exclusion radius)
for line in input_txt:
    matches = list(map(int, re.findall(r'-?\d+', line)))
    sensors.append(tuple(matches[0:2]))
    beacons.append(tuple(matches[2:4]))
    beacon_dists.append(manhattan_dist(sensors[-1], beacons[-1]))

search_bound = 4000000  # max x and y positions the beacon can be within
possible_int_points = find_possible_intersection_points(sensors, beacon_dists, search_bound)
search_grid_size = 2  # radius of square grid around intersection point in which to search for beacon
beacon_found = False
beacon_pos = None  # distress beacon position once found
i = 0
while i < len(possible_int_points) and not beacon_found:
    point = possible_int_points[i]
    # search near possible intersection point.
    x = point[0] - search_grid_size
    while x <= point[0] + search_grid_size and 0 <= x <= search_bound and not beacon_found:
        y = point[1] - search_grid_size
        while y <= point[1] + search_grid_size and 0 <= y <= search_bound and not beacon_found:
            j = 0
            while j < len(sensors) and manhattan_dist((x, y), sensors[j]) > beacon_dists[j]:
                j += 1
            if j == len(sensors):  # if not excluded by any sensor  TODO write this better
                beacon_found = True
                beacon_pos = (x, y)
            y += 1
        x += 1
    i += 1

tuning_frequency = beacon_pos[0] * 4000000 + beacon_pos[1]
print(f'The tuning frequency of the distress beacon is {tuning_frequency}')
