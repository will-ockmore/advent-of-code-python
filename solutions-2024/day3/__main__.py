import re
from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()


pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def part_1():
    total = 0
    for line in lines:
        for match in re.finditer(pattern, line):
            x, y = match.groups()

            total += int(x) * int(y)

    print(total)


second_pattern = re.compile(r"(do\(\))|(don't\(\))|" + pattern.pattern)


def part_2():
    enabled = True
    total = 0
    for line in lines:
        for match in re.finditer(second_pattern, line):
            groups = match.groups()

            if groups[0]:
                enabled = True
                continue

            if groups[1]:
                enabled = False
                continue

            if enabled:
                total += int(groups[2]) * int(groups[3])

    print(total)


part_1()
part_2()
