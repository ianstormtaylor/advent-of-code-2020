import os

file = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file) as f:
    lines = f.readlines()


def check_slope(right, down):
    x = 0
    y = 0
    trees = 0

    while y < len(lines):
        row = lines[y]
        max = len(row) - 1
        column = row[x % max]

        if column == "#":
            trees += 1

        y += down
        x += right

    return trees


def part_one():
    trees = check_slope(3, 1)
    return trees


def part_two():
    product = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    for right, down in slopes:
        product = product * check_slope(right, down)

    return product


print("Part one:", part_one())
print("Part two:", part_two())
