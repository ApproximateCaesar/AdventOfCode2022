# https://adventofcode.com/2022/day/16

"""Approach: First reduce problem size by working with a complete graph of valves with non-zero
flow rates, using shortest distances as edge weights. Then brute force search all feasible
(in terms of time) valve-opening sequences. What cuts down the search space from n! where
n is the number of nodes in the complete graph is that most sequences never get to length n
due to the time limit. Part 2 increases complexity to n*(n-2)*(n-4)*...*2 so another optimisation
I made was to stop each sequence if continuing it couldn't possibly beat the current max TEP.
Part 2 is still painfully slow."""

from collections import deque
import re
from pprint import PrettyPrinter


def all_pairs_shortest_paths(adjacency_dict):
    """Returns all pairs shortest paths for an unweighted undirected graph
     by running BFS from every node (not very efficient but simple)."""

    shortest_path_dists = {}  # dict of dict containing shortest path distances between nodes
    for v, v_neighbours in adjacency_dict.items():
        shortest_path_dists[v] = dict.fromkeys(adjacency_dict.keys(), 0)

    for start in adjacency_dict:  # BFS starting from each node
        visited = set()  # visited nodes
        queue = deque()  # queue to store nodes to be processed
        visited.add(start)
        queue.appendleft(start)

        while queue:  # while queue not empty
            v = queue.pop()

            for w in adjacency_dict[v]:  # for each neighbouring node
                if w not in visited:
                    visited.add(w)
                    shortest_path_dists[start][w] = shortest_path_dists[start][v] + 1
                    queue.appendleft(w)
    return shortest_path_dists


PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day16_proboscidea_volcanium/day16_input.txt") as f:
    valve_descriptions = f.read().splitlines()

valve_labels = []  # list of all valve labels
flow_rates = {}  # flow rate for each valve
adjacency_dict = {}  # neighbours for each valve (adjacent valves connected by a tunnel)
for valve_desc in valve_descriptions:
    labels = re.findall(r'[A-Z]{2}', valve_desc)
    valve_labels.append(labels[0])
    flow_rate = int(re.search(r'\d+', valve_desc).group(0))
    flow_rates[labels[0]] = flow_rate
    adjacency_dict[labels[0]] = labels[1:]

# debug prints
# for valve, neighbours in adjacency_dict.items():
#     print(valve, flow_rates[valve], neighbours)
shortest_path_dists = all_pairs_shortest_paths(adjacency_dict)

# pp = PrettyPrinter(width=200)
# pp.pprint(shortest_path_dists)

# check all feasible valve opening sequences using shortest distances between valves
usable_valves = [valve for valve in valve_labels if flow_rates[valve] != 0]  # valves with non-zero flow rate
t_max = 26  # time limit in minutes
#  TODO can start TEP_max at a larger value to avoid recomputing initial sequences from previous runs?
#   Largest value found so far is 2375
TEP_max = 2375  # maximum total eventual pressure
best_sequence = []  # optimal sequence in which to open valves, taking shortest paths inbetween


def find_max_TEP(t, t_max, TEP, usable_valves, current_valves, sequence):
    global TEP_max
    global best_sequence

    # return if the current sequence couldn't possibly beat the current max TEP
    max_extra_TEP = sum([flow_rates[v] * (t_max - min(t) - 1) for v in usable_valves])
    if TEP + max_extra_TEP <= TEP_max:
        return

    for person in (0, 1):  # you or the elephant
        for next_valve in usable_valves:
            if t[person] + shortest_path_dists[current_valves[person]][next_valve] + 1 < t_max:  # have time to open this valve
                new_t = t[:]
                new_t[person] = t[person] + shortest_path_dists[current_valves[person]][next_valve] + 1  # add time to move to valve and open it
                new_TEP = TEP + flow_rates[next_valve] * (t_max - new_t[person])  # add TEP from opening valve
                new_current_valves = current_valves[:]
                new_current_valves[person] = next_valve
                new_sequence = sequence[:]
                new_sequence.append((new_t[person], person, next_valve))
                new_usable_valves = usable_valves[:]
                new_usable_valves.remove(next_valve)  # remove opened valve (can't use it again)
                # recurse from next valve
                find_max_TEP(new_t, t_max, new_TEP, new_usable_valves, new_current_valves, new_sequence)

    if TEP > TEP_max:  # check if sequence gives higher TEP than current maximum
        TEP_max = TEP
        print(TEP_max)
        best_sequence = sequence


find_max_TEP([0, 0], 26, 0, usable_valves, ['AA', 'AA'], best_sequence)  # maximum total eventual pressure achievable in max_t minutes
print(TEP_max, sorted(best_sequence, key=lambda x: x[0]))






