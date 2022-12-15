# https://adventofcode.com/2022/day/9

PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day9_rope_bridge/day9_input.txt") as f:
    motions = f.read().splitlines()


def print_tail_path(visited_by_T):
    """visualise the tail path."""
    min_x = min([p[0] for p in visited_by_T])
    max_x = max([p[0] for p in visited_by_T])
    min_y = min([p[1] for p in visited_by_T])
    max_y = max([p[1] for p in visited_by_T])

    for y in range(max_y, min_y - 1, -1):
        row = ''
        for x in range(min_x, max_x + 1, 1):
            if (x, y) == (0, 0):
                row += 's'
            elif (x, y) in visited_by_T:
                row += '#'
            else:
                row += '.'
        print(row)


def print_rope(knot_pos):
    """visualise the rope for debugging."""
    for y in range(15, -6, -1):
        row = ''
        for x in range(-11, 15, 1):
            if [x, y] == [0, 0]:
                row += 's'
            elif [x, y] in knot_pos:
                row += str(knot_pos.index([x, y]))
            else:
                row += '.'
        print(row)
    print('\n')


def chebyshev_distance(a, b):
    """Returns the chebyshev (chessboard) distance between points a and b.
    A chebyshev distance of 1 means x and y are adjacent."""
    return max([abs(a_i - b_i) for a_i, b_i in zip(a, b)])


def new_knot_pos(current_knot_pos, leading_knot_pos):
    """Returns the updated position of a knot given its current position and
    the position of the leading knot (closer to the head). The rule for updating
    position can be expressed as follows: find the displacement vector from current
    to leading pos, half the component with the largest abs value (or both if equal),
     then add the result to current pos."""

    displacement = [a - b for a, b in zip(leading_knot_pos, current_knot_pos)]
    if abs(displacement[0]) > abs(displacement[1]):  # x component is larger
        displacement[0] = displacement[0] // 2
    elif abs(displacement[0]) < abs(displacement[1]):  # y component larger
        displacement[1] = displacement[1] // 2
    else:  # components are equally large
        displacement[0] = displacement[0] // 2
        displacement[1] = displacement[1] // 2
    return [a + b for a, b in zip(current_knot_pos, displacement)]


def get_tail_positions(motions, rope_length):
    """Returns the set of points visited at least once by the rope tail."""
    # positions of each knot, the head being at index 0. All start at (0, 0)
    knot_pos = [[0, 0] for i in range(rope_length)]
    visited_by_T = set()
    visited_by_T.add(tuple(knot_pos[-1]))
    for motion in motions:
        direction, steps = motion[0], int(motion[2:])  # direction and number of steps head moves
        for i in range(steps):
            # move head 1 step
            if direction == 'L':
                knot_pos[0][0] -= 1
            elif direction == 'R':
                knot_pos[0][0] += 1
            elif direction == 'U':
                knot_pos[0][1] += 1
            elif direction == 'D':
                knot_pos[0][1] -= 1
            # move other knots until adjacency is satisfied
            j = 1
            while j < rope_length and chebyshev_distance(knot_pos[j], knot_pos[j - 1]) > 1:
                knot_pos[j] = new_knot_pos(knot_pos[j], knot_pos[j - 1])
                j += 1

            visited_by_T.add(tuple(knot_pos[-1]))  # record pos of tail
    return visited_by_T


ROPE_LENGTH = 10  # Rope length in number of knots
visited_by_T = get_tail_positions(motions, ROPE_LENGTH)
print(f'The number of points visited at least once by the tail is {len(visited_by_T)}')
print(f'Tail path for rope of length {ROPE_LENGTH}:')
print_tail_path(visited_by_T)

