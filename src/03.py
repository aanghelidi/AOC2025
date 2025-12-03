import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()


def find_largest_joltage(battery_bank: list[int], n_digits: int) -> int:
    stack = []
    n = len(battery_bank)
    for i, digit in enumerate(battery_bank):
        while stack and digit > stack[-1] and len(stack) + (n - i - 1) >= n_digits:
            stack.pop()
        if len(stack) >= n_digits:
            continue
        stack.append(digit)
    return int("".join(map(str, stack)))


ans, ans2 = 0, 0
for line in data:
    battery_bank = [int(e) for e in line]
    max_joltage = find_largest_joltage(battery_bank, 2)
    ans += max_joltage
    max_joltage_2 = find_largest_joltage(battery_bank, 12)
    ans2 += max_joltage_2

print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
