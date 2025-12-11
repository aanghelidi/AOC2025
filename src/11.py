import sys
from functools import cache

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

graph = {}
for line in data:
    left, right = line.split(":")
    left = left.strip()
    destinations = right.strip().split()
    graph[left] = destinations


@cache
def count_paths(current, target):
    if current == target:
        return 1
    if current not in graph:
        return 0
    return sum(count_paths(neighbor, target) for neighbor in graph[current])


ans = count_paths("you", "out")
print(f"Part 1: {ans}")


paths_1 = (
    count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
)
paths_2 = (
    count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
)
ans_2 = paths_1 + paths_2
print(f"Part 2: {ans_2}")
