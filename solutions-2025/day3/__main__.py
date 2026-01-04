from pathlib import Path
from collections import defaultdict

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
banks = [tuple(int(x) for x in line) for line in lines if line]


def part_1():
    joltage = 0

    for bank in banks:
        # Construct an index of all positions of all numbers in the bank
        d = defaultdict(list)
        for i, num in enumerate(bank):
            d[num].append(i)

        first, second = None, None

        # Pick the largest number, which must always be the greatest, as long as there is a number following
        first_pos = None
        for num in sorted(d, reverse=True):
            if d[num][0] < (len(bank) - 1):
                first_pos = d[num][0]
                first = num
                break

        # Find the second digit, which is the greatest pos of any subsequent digit in order

        for num in sorted(d, reverse=True):
            for pos in d[num]:
                if pos > first_pos:
                    second = num
                    break

            if second is not None:
                break

        bank_joltage = int(str(first) + str(second))
        joltage += bank_joltage

    print(joltage)


def part_2():
    joltage = 0

    for bank in banks:
        # Construct an index of all positions of all numbers in the bank
        d = defaultdict(list)
        for i, num in enumerate(bank):
            d[num].append(i)

        bank_joltage = ""
        remaining_digits = 11

        # Pick the largest number, which must always be the next digit for the largest result,
        # as long as there's enough space for the remaining digits.
        last_pos = -1
        for remaining_digits in range(11, -1, -1):
            found = False
            for num in sorted(d, reverse=True):
                for pos in d[num]:
                    if pos > last_pos and pos < (len(bank) - remaining_digits):
                        last_pos = pos
                        bank_joltage += str(num)
                        found = True
                        break
                if found:
                    break

        joltage += int(bank_joltage)

    print(joltage)


part_1()
part_2()
