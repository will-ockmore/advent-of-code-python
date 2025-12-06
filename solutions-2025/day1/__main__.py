from collections import Counter
from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()

ids = [line.split() for line in lines]

first, second = [list(x) for x in zip(*ids)]


def part_1():
    print(
        sum(
            abs(x - y)
            for x, y in zip(
                sorted(int(i) for i in first), sorted(int(i) for i in second)
            )
        )
    )


def part_2():
    count_second = Counter(second)

    print(sum(int(x) * int(count_second.get(x, 0)) for x in first))


part_1()
part_2()
