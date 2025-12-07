import sys
from collections import deque

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()


grid = {}
start_position = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "S":
            start_position = (x, y)
        grid[(x, y)] = c

visited_p1 = {start_position}
timeline_counter = {start_position: 1}
positions = deque([start_position])
visited = {start_position}
ans, ans_2 = 0, 0
while positions:
    x, y = positions.popleft()
    current_count = timeline_counter[(x, y)]
    new_position = (x, y + 1)
    if new_position not in grid:
        ans_2 += current_count
        continue
    if (char := grid[new_position]) == ".":
        timeline_counter[new_position] = (
            timeline_counter.get(new_position, 0) + current_count
        )
        if new_position not in visited:
            visited.add(new_position)
            positions.append(new_position)
        if new_position not in visited_p1:
            visited_p1.add(new_position)
    elif char == "^":
        if new_position not in visited_p1:
            ans += 1
            visited_p1.add(new_position)
        new_positions = [
            (new_position[0] + 1, new_position[1]),
            (new_position[0] - 1, new_position[1]),
        ]
        for next_pos in new_positions:
            if next_pos not in grid:
                continue
            timeline_counter[next_pos] = (
                timeline_counter.get(next_pos, 0) + current_count
            )
            if next_pos not in visited:
                visited.add(next_pos)
                positions.append(next_pos)
            if next_pos not in visited_p1:
                visited_p1.add(next_pos)

print(f"Part 1: {ans}")
print(f"Part 2: {ans_2}")
