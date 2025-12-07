import operator
import sys
from collections.abc import Callable
from functools import reduce


def char_to_op(c: str) -> Callable:
    return dict(zip("+*", (operator.add, operator.mul)))[c]


with open(sys.argv[1]) as f:
    data = f.read()

problems = [line.split() for line in data.splitlines()]
n, m, ans = len(problems), len(problems[0]), 0
for x in range(m):
    current = []
    for y in range(n - 1):
        current.append(int(problems[y][x]))
    ans += reduce(char_to_op(problems[n - 1][x]), current)
print(f"Part 1: {ans}")

max_width = max(len(line) for line in data.splitlines())
grid = [line.ljust(max_width) for line in data.splitlines()]
n, m = len(grid), max_width
transposed = list(zip(*grid))
separator_cols = [i for i, col in enumerate(transposed) if all(c == " " for c in col)]
blocks, current_block = [], []
for i in range(m):
    if i in separator_cols and current_block:
        blocks.append(current_block)
        current_block = []
    else:
        current_block.append(transposed[i])
if current_block:
    blocks.append(current_block)
blocks = blocks[::-1]

ans_2 = 0
for block in blocks:
    for col in block:
        if (c := col[n - 1]) != " " and c in "+*":
            op_char = c
            break
    op_func, nums = char_to_op(op_char), []
    for col_index in range(len(block) - 1, -1, -1):
        num_str = "".join(c for c in block[col_index][: n - 1] if c != " ")
        nums.append(0 if num_str == "" else int(num_str))
    ans_2 += reduce(op_func, nums)
print(f"Part 2: {ans_2}")
