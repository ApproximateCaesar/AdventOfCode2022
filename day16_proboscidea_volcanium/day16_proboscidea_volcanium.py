# https://adventofcode.com/2022/day/16

"""Dynamic programming approach. AAAAAAAAH this won't work because the decision at stage t
cant tell us the full state at stage t+1: we don't know the open status of the valve we move to."""

import re

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day16_proboscidea_volcanium/day16_example_input.txt") as f:
    valve_descriptions = f.read().splitlines()

valve_labels = []
flow_rates = {}  # flow rate for each valve
neighbours = {}  # neighbours for each valve (adjacent valves connected by a tunnel)
for valve_desc in valve_descriptions:
    labels = re.findall(r'[A-Z]{2}', valve_desc)
    valve_labels.append(labels[0])
    flow_rate = int(re.search(r'\d+', valve_desc).group(0))
    flow_rates[labels[0]] = flow_rate
    neighbours[labels[0]] = labels[1:]

for valve, neighbours in neighbours.items():
    print(valve, flow_rates[valve], neighbours)

max_t = 30
# max total eventual pressure (TEP) for a given [start time][start valve][valve open status]
max_TEP = [dict.fromkeys(flow_rates, [0, 0]) for t in range(max_t + 1)]

for t in range(max_t, 0, -1):  # for each stage (starting minute)
    for valve in valve_labels:  # for each starting valve
        for valve_open_status in range()