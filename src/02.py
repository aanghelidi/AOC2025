import bisect
import sys
from collections.abc import Iterator

with open(sys.argv[1]) as f:
    ranges = f.read().split(",")


def invalid_ids(n: int) -> Iterator[int]:
    for i in range(1, (n // 2) + 1):
        coef = 10**i + 1
        start = 10 ** (i - 1)
        end = 10**i
        for s in range(start, end):
            yield s * coef


def invalid_ids_2(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        for j in range(2, n // i + 1):
            d = i * j
            m = (10**d - 1) // (10**i - 1)
            start = 10 ** (i - 1)
            stop = 10**i
            for k in range(start, stop):
                N = k * m
                yield N


MAX_DIGITS = 10
ans, ans2 = 0, 0
all_invalid_ids = sorted(invalid_ids(MAX_DIGITS))
all_invalid_ids_2 = sorted(set(invalid_ids_2(MAX_DIGITS)))

for r in ranges:
    start, stop = r.split("-")
    start, stop = int(start), int(stop)

    ans += sum(
        all_invalid_ids[
            bisect.bisect_left(all_invalid_ids, start) : bisect.bisect_right(
                all_invalid_ids, stop
            )
        ]
    )

    ans2 += sum(
        all_invalid_ids_2[
            bisect.bisect_left(all_invalid_ids_2, start) : bisect.bisect_right(
                all_invalid_ids_2, stop
            )
        ]
    )


print(f"Part 1: {ans}")
print(f"Part 2: {ans2}")
