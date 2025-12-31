from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    content = f.read()

ranges = []

for id_range in content.strip().split(","):
    start, end = id_range.split("-")
    ranges.append((int(start), int(end)))


def part_1():
    count = 0
    for id_range in ranges:
        start, end = id_range
        for n in range(start, end + 1):
            num = str(n)
            if int(len(num)) % 2 == 0:
                midpoint = len(num) // 2
                if num[midpoint:] == num[:midpoint]:
                    count += n

    print(count)


def part_2():
    count = 0
    for id_range in ranges:
        start, end = id_range
        for n in range(start, end + 1):
            num = str(n)
            if int(len(num)) % 2 == 0:
                midpoint = len(num) // 2
                if num[midpoint:] == num[:midpoint]:
                    count += n
    print(count)


part_1()
part_2()
