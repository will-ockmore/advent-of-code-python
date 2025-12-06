from collections import Counter
from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()

items = [[int(x) for x in line.split()] for line in lines]


def part_1():
    safe = 0
    for seq in items:
        diffs = []
        curr = seq[0]
        for x in seq[1:]:
            diffs.append(x - curr)
            curr = x

        if all(0 < abs(diff) < 4 for diff in diffs) and (
            all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
        ):
            safe += 1

    print(safe)


def part_2():
    safe = 0
    for seq in items:
        diffs = []
        curr = seq[0]
        for x in seq[1:]:
            diffs.append(x - curr)
            curr = x

        if all(0 < abs(diff) < 4 for diff in diffs) and (
            all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
        ):
            safe += 1
        else:
            # Remove one level at a time and see if it's safe
            for removed_item in range(len(seq)):
                diffs = []
                new_seq = seq[0:removed_item] + seq[removed_item + 1 :]
                curr = new_seq[0]
                for x in new_seq[1:]:
                    diffs.append(x - curr)
                    curr = x
                if all(0 < abs(diff) < 4 for diff in diffs) and (
                    all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
                ):
                    safe += 1
                    break

    print(safe)


part_1()
part_2()
