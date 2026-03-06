from pathlib import Path
from pprint import pprint

with open(Path(__file__).parent / "input.txt") as f:
    lines = f.readlines()

grid = [[char for char in line.strip()] for line in lines if line.strip()]


def surrounding_points(x, y):
    pass


def part_1():
    accessible_rolls = 0
    # Iterate the positions in the grid
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            # Count the surrounding rolls of paper
            num_rolls = 0
            if grid[y][x] == "@":
                for i, j in (
                    (x - 1, y - 1),
                    (x - 1, y),
                    (x - 1, y + 1),
                    (x, y - 1),
                    (x, y + 1),
                    (x + 1, y - 1),
                    (x + 1, y),
                    (x + 1, y + 1),
                ):
                    if (
                        i >= 0
                        and i < len(row)
                        and j >= 0
                        and j < len(grid)
                        and grid[j][i] == "@"
                    ):
                        num_rolls += 1

                if num_rolls < 4:
                    accessible_rolls += 1

    # pprint(grid)
    print(accessible_rolls)


def part_2():
    accessible_rolls = set()
    should_run_pass = True

    while should_run_pass:
        should_run_pass = False
        # Iterate the positions in the grid
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                # Count the surrounding rolls of paper
                num_rolls = 0
                if grid[y][x] == "@":
                    for i, j in (
                        (x - 1, y - 1),
                        (x - 1, y),
                        (x - 1, y + 1),
                        (x, y - 1),
                        (x, y + 1),
                        (x + 1, y - 1),
                        (x + 1, y),
                        (x + 1, y + 1),
                    ):
                        if (
                            i >= 0
                            and i < len(row)
                            and j >= 0
                            and j < len(grid)
                            and grid[j][i] == "@"
                        ):
                            num_rolls += 1

                    if num_rolls < 4:
                        accessible_rolls.add((x, y))
                        grid[y][x] = "."
                        should_run_pass = True

    # pprint(grid)
    print(len(accessible_rolls))


part_1()
part_2()
