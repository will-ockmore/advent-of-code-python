from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
instructions = [(line[0], int(line[1:])) for line in lines if line]


def part_1():
    # The dial starts on 50.
    pos = 50
    times_on_zero = 0
    for direction, amount in instructions:
        if direction == "L":
            pos = (pos - amount) % 100
        else:
            pos = (pos + amount) % 100

        if pos == 0:
            times_on_zero += 1
    print(times_on_zero)


def part_2():
    # The dial starts on 50.
    pos = 50
    times_on_zero = 0
    for direction, amount in instructions:
        if direction == "L":
            d = pos - amount

            distance_to_first_zero = pos if pos > 0 else 100

            amount -= distance_to_first_zero

            if amount >= 0:
                times_on_zero += amount // 100 + 1

            pos = d % 100
        else:
            d = pos + amount

            amount -= 100 - pos

            if amount >= 0:
                times_on_zero += amount // 100 + 1

            pos = d % 100

    print(times_on_zero)


part_1()
part_2()
