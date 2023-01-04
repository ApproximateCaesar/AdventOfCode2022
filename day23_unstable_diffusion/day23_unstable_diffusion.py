# https://adventofcode.com/2022/day/23


def padd(a, b):
    """Return the addition of two 2D points."""
    return (a[0] + b[0], a[1] + b[1])


def is_valid_direction(elf_pos, dir_index):
    """Check whether a direction specified by dir_index is a valid direction to move in from position elf_pos."""
    adjacent_positions = [padd(elf_pos, d) for d in ADJACENT_DIRECTIONS[dir_index]]
    for p in adjacent_positions:
        if p in elves:
            return False
    return True


PATH = "C:/Users/Julian_local/Documents/Coding Projects/AdventOfCode2022/"
with open(PATH + "day23_unstable_diffusion/day23_input.txt") as f:
    grove = f.read().splitlines()

NUM_ROUNDS = 10
elves = set()  # current elf positions using row, column coordinates
for i, row in enumerate(grove):
    for j, tile in enumerate(row):
        if tile == '#':  # Is an elf
            elves.add((i, j))
NUM_ELVES = len(elves)

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))  # directions elf can propose to move in: N, S, W, E
# adjacent directions to check for elves for each proposed direction
ADJACENT_DIRECTIONS = (((-1, -1), (-1, 0), (-1, 1)),  # N
                       ((1, -1), (1, 0), (1, 1)),  # S
                       ((-1, -1), (0, -1), (1, -1)),  # W
                       ((-1, 1), (0, 1), (1, 1)))  # E
first_dir_index = 0  # index of direction we check first

finished_moving = False
rounds_elapsed = 0
# Note: both halves of a round could be done in the same loop
while not finished_moving:  # for _ in range(NUM_ROUNDS):
    proposed_positions = {}  # proposed position: [positions of elves that want to move there]
    # First half - move proposal:
    for elf_pos in elves:
        proposed_position = None
        dir_index = first_dir_index
        num_valid_dir = 0
        for _ in range(4):
            if is_valid_direction(elf_pos, dir_index):
                num_valid_dir += 1
                if proposed_position is None:
                    proposed_position = padd(elf_pos, DIRECTIONS[dir_index])
            dir_index = (dir_index + 1) % 4  # next direction

        if num_valid_dir == 4 or proposed_position is None:  # no adjacent elves or no valid direction - don't move
            proposed_position = elf_pos

        if proposed_position not in proposed_positions:
            proposed_positions[proposed_position] = [elf_pos]
        else:
            proposed_positions[proposed_position].append(elf_pos)

    # Second half - proposal resolution
    new_elves = set()
    for proposed_position, elves_to_move in proposed_positions.items():
        if len(elves_to_move) == 1:  # only one elf proposing to move to this position
            new_elves.add(proposed_position)  # elf moves to proposed position
        else:  # multiple elves trying to move to same tile
            new_elves.update(elves_to_move)  # elves stay where they are
    if new_elves == elves:  # elves didn't move
        finished_moving = True
    else:
        elves = new_elves  # update elf positions

    first_dir_index = (first_dir_index + 1) % 4  # cycle first direction
    rounds_elapsed += 1

# Compute number of empty ground tiles:
max_row = max([elf_pos[0] for elf_pos in elves])
min_row = min([elf_pos[0] for elf_pos in elves])
max_col = max([elf_pos[1] for elf_pos in elves])
min_col = min([elf_pos[1] for elf_pos in elves])
rectangle_area = (max_row - min_row + 1) * (max_col - min_col + 1)
print(f'The bounding rectangle contains {rectangle_area - NUM_ELVES} empty ground tiles.')
print(f'The first round in which no elf moves is round {rounds_elapsed}')