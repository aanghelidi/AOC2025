import math
import sys
from itertools import combinations
from typing import NamedTuple

import networkx as nx


class Position(NamedTuple):
    x: int
    y: int
    z: int


with open(sys.argv[1]) as f:
    data = f.read().splitlines()

positions = [
    Position(**dict(zip("xyz", map(int, line.strip().split(","))))) for line in data
]
n = len(positions)
G = nx.Graph()
G.add_nodes_from(range(n))
all_edges = [
    (math.dist(positions[i], positions[j]), i, j) for i, j in combinations(range(n), 2)
]
all_edges.sort()
top_edges = all_edges[:1000]
for _, u, v in top_edges:
    G.add_edge(u, v)
components = list(nx.connected_components(G))
sizes = sorted((len(c) for c in components), reverse=True)
ans = sizes[0] * sizes[1] * sizes[2]
print(f"Part 1: {ans}")

G.clear()
G.add_nodes_from(range(n))
last_u, last_v = -1, -1
for _, u, v in all_edges:
    if nx.has_path(G, u, v):
        continue
    if (
        u_component := next((c for c in nx.connected_components(G) if u in c), None)
    ) is None or v not in u_component:
        last_u, last_v = u, v
        G.add_edge(last_u, last_v)
        if nx.number_connected_components(G) == 1:
            break
ans_2 = positions[last_u].x * positions[last_v].x
print(f"Part 2: {ans_2}")
