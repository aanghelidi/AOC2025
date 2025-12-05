import sys

with open(sys.argv[1]) as f:
    ranges, ingredients = f.read().split("\n\n")


def parse_ranges(ranges: str) -> list[range]:
    result = []
    for r in ranges.splitlines():
        start, _, end = r.partition("-")
        result.append(range(int(start), int(end) + 1))
    return result


def is_fresh(ingredient: int, ranges: list[range]) -> bool:
    return any(ingredient in r for r in ranges)


def merge_ranges(ranges: list[range]) -> list[range]:
    if not ranges:
        return []
    ranges.sort(key=lambda x: x.start)
    result = [ranges[0]]
    for current in ranges[1:]:
        last = result[-1]
        if current.start <= last.stop:
            new_start = last.start
            new_stop = max(last.stop, current.stop)
            result[-1] = range(new_start, new_stop)
        else:
            result.append(current)
    return result


ranges = parse_ranges(ranges)
ranges = merge_ranges(ranges)

ans = sum(is_fresh(int(ingredient), ranges) for ingredient in ingredients.splitlines())
print(f"Part 1: {ans}")

ans2 = sum(len(r) for r in ranges)
print(f"Part 2: {ans2}")
