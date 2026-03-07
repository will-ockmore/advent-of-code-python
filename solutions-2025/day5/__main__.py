from pathlib import Path

ranges = []
ids = []

with open(Path(__file__).parent / "input.txt") as f:
    while (line := f.readline()).strip():
        ranges.append(tuple(int(x) for x in line.split("-")))

    for line in f:
        if line.strip():
            ids.append(int(line.strip()))


# Combine ranges

combined_ranges = []

for start, end in sorted(ranges):
    if combined_ranges and start <= combined_ranges[-1][1] + 1:
        combined_ranges[-1] = (combined_ranges[-1][0], max(combined_ranges[-1][1], end))
    else:
        combined_ranges.append((start, end))


def part_1():
    fresh_ingredients = 0

    for num in ids:
        # Find a range that the id is contained within
        for start, end in combined_ranges:
            if start <= num and end >= num:
                fresh_ingredients += 1
                break
            if start > num:
                break

    print(fresh_ingredients)


def part_2():
    print(sum(end - start + 1 for start, end in combined_ranges))


part_1()
part_2()
