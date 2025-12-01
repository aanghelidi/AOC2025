import sys


def count_extra(current_pos: int, rotation_char: str, distance: int) -> int:
    if rotation_char == "R":
        return (current_pos + distance) // 100
    if distance < current_pos:
        return 0
    if current_pos == 0:
        return (distance - 1) // 100
    return 1 + (distance - current_pos) // 100


with open(sys.argv[1]) as f:
    data = f.read().splitlines()

current = 50
ans = 0
ans2 = 0
for line in data:
    rotation, distance = line[0], int(line[1:])
    ans2 += count_extra(current, rotation, distance)
    coef = 1 if rotation == "R" else -1
    current = (current + distance * coef) % 100
    ans += current == 0

print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
