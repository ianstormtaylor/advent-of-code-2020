import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
numbers = [int(l) for l in open(file).readlines()]


def part_one():
    for a in numbers:
        for b in numbers:
            if a + b == 2020:
                return a * b


def part_two():
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    return a * b * c


print("Part one:", part_one())
print("Part two:", part_two())
