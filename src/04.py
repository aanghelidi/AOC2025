import sys
from collections.abc import Iterator


def parse(data: list[str]) -> tuple[dict, set]:
    grid = {}
    rolls_positions = set()
    for j, line in enumerate(data):
        for i, c in enumerate(line):
            position = complex(i, j)
            grid[position] = c
            if c == "@":
                rolls_positions.add(position)
    return grid, rolls_positions


def n8(position: complex, grid: dict) -> Iterator[complex]:
    deltas = (-1 + 1j, 0 + 1j, 1 + 1j, -1 + 0j, 1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j)
    for delta in deltas:
        if (neighbour_position := position + delta) not in grid:
            continue
        yield neighbour_position


def can_be_accessed(position: complex, grid: dict) -> bool:
    return len([np for np in n8(position, grid) if grid[np] == "@"]) < 4


with open(sys.argv[1]) as f:
    data = f.read().splitlines()

grid, rolls_positions = parse(data)
ans = sum(can_be_accessed(rp, grid) for rp in rolls_positions)
print(f"Part 1: {ans}")

ans2 = 0
while True:
    rolls_to_remove = set(rp for rp in rolls_positions if can_be_accessed(rp, grid))
    if (n_to_remove := len(rolls_to_remove)) == 0:
        break
    ans2 += n_to_remove
    rolls_positions -= rolls_to_remove
    for rrp in rolls_to_remove:
        grid[rrp] = "X"

print(f"Part 2: {ans2}")
