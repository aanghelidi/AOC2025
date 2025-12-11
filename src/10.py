import re
import sys
from collections import deque

from pulp import LpMinimize, LpProblem, LpVariable, lpSum


def to_binary(arr: list) -> int:
    binary_str = "".join(map(str, arr))
    return int(binary_str, 2)


def parse(line: str) -> tuple[int, list[int], int]:
    target_str_match = re.search(r"\[([.\#]+)\]", line)
    if not target_str_match:
        raise ValueError("Invalid input format for target state")
    target_str = target_str_match.group(1)
    target = [0 if c == "." else 1 for c in target_str]
    target_bin = to_binary(target)
    button_matches = re.findall(r"\(([^)]+)\)", line)
    buttons = []
    for match in button_matches:
        indices = list(map(int, match.split(",")))
        button = [0] * len(target)
        for i in indices:
            button[i] = 1
        buttons.append(to_binary(button))
    return target_bin, buttons, len(target)


def parse_joltage(line: str) -> list[int]:
    joltage_match = re.search(r"\{([^}]+)\}", line)
    if not joltage_match:
        raise ValueError("Invalid input format for joltage requirements")
    joltage = list(map(int, joltage_match.group(1).split(",")))
    return joltage


def count_minimal_presses_2(joltage, buttons) -> int:
    n = len(joltage)
    m = len(buttons)
    prob = LpProblem("Joltage_Configuration", LpMinimize)
    x = [LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(m)]
    prob += lpSum(x)
    for i in range(n):
        prob += (
            lpSum(button[i] * x[j] for j, button in enumerate(buttons)) == joltage[i]
        )
    prob.solve()
    return int(prob.objective.value())


def count_minimal_presses(target: int, buttons: list, n: int) -> int:
    dist = [-1] * 2**n
    dist[0] = 0
    queue = deque([0])
    while queue:
        state = queue.popleft()
        if state == target:
            return dist[state]
        for button in buttons:
            new_state = state ^ button
            if dist[new_state] != -1:
                continue
            dist[new_state] = dist[state] + 1
            queue.append(new_state)
    return 0


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

ans, ans2 = 0, 0
for line in lines:
    target, buttons, n = parse(line)
    presses = count_minimal_presses(target, buttons, n)
    ans += presses
    joltage = parse_joltage(line)
    button_matrix = []
    for button in buttons:
        button_bin = [int(digit) for digit in f"{button:0{n}b}"]
        button_matrix.append(button_bin)
    presses2 = count_minimal_presses_2(joltage, button_matrix)
    ans2 += presses2
print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
