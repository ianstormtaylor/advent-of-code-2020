import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).readlines()


def parse_seat(line):
    x = 8
    y = 128
    row = 0
    col = 0
    for char in line:
        if char == "F" or char == "B":
            y = y / 2
            if char == "B":
                row += y
        elif char == "L" or char == "R":
            x = x / 2
            if char == "R":
                col += x
    return (int(row), int(col))


seats = [parse_seat(l) for l in lines]
ids = [row * 8 + col for row, col in seats]


def part_one():
    return max(ids)


def part_two():
    for id in range(max(ids)):
        if not id in ids and id - 1 in ids and id + 1 in ids:
            return id


print("Part one:", part_one())
print("Part two:", part_two())
