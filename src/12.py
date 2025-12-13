import sys


def parse_shapes(shapes: list[str]) -> list[tuple[int, list[str]]]:
    return [
        (i, shape.split(":")[-1].strip().splitlines()) for i, shape in enumerate(shapes)
    ]


def parse_regions(regions: str) -> list[tuple[int, int, list[int]]]:
    regions = [region.split(": ") for region in regions.splitlines()]
    result = []
    for region in regions:
        wl, quantities = region
        wl = tuple(map(int, wl.split("x")))
        quantities = list(map(int, quantities.split()))
        result.append((*wl, quantities))
    return result


def n_present_area(width: int, length: int) -> int:
    return (width // 3) * (length // 3)


def is_present_fitting(region: tuple[int, int, list[int]]) -> bool:
    width, length, quantities = region
    return sum(quantities) <= n_present_area(width, length)


with open(sys.argv[1]) as f:
    data = f.read()

sections = data.split("\n\n")
shapes = parse_shapes(sections[:-1])
regions = parse_regions(sections[-1])
shape_area = ["".join(map(str, shape)).count("#") for shape in shapes]
ans = sum(is_present_fitting(region) for region in regions)
print(f"Answer: {ans}")
