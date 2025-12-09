import sys
from collections import namedtuple
from itertools import combinations
from math import prod

from shapely import Polygon
from shapely.geometry import box


def area(t1: RedTile, t2: RedTile) -> int:
    return prod(abs(x - y) + 1 for x, y in zip(t1, t2))


def rectangle_from_tiles(t1: RedTile, t2: RedTile) -> Polygon:
    min_x = min(t1.x, t2.x)
    max_x = max(t1.x, t2.x)
    min_y = min(t1.y, t2.y)
    max_y = max(t1.y, t2.y)
    return box(min_x, min_y, max_x, max_y)


with open(sys.argv[1]) as f:
    data = f.read().splitlines()

RedTile = namedtuple("RedTile", ["x", "y"])
red_tiles = [RedTile(**dict(zip("xy", map(int, x.split(","))))) for x in data]
ans = max(
    area(red_tiles[i], red_tiles[j]) for i, j in combinations(range(len(red_tiles)), 2)
)
print(f"Part 1: {ans}")

polygon = Polygon(red_tiles)
areas = []
for i, j in combinations(range(len(red_tiles)), 2):
    t1, t2 = red_tiles[i], red_tiles[j]
    current_area = area(t1, t2)
    if areas and current_area <= max(areas):
        continue
    rectangle = rectangle_from_tiles(t1, t2)
    if polygon.covers(rectangle):
        areas.append(current_area)

print(f"Part 2: {max(areas)}")
