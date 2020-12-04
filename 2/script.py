import os
import re

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).readlines()
entries = []
for line in lines:
    [(a, b, c, d)] = re.findall(r"^(\d+)-(\d+) (\w): (.*)$", line)
    entries.append([int(a), int(b), c, d])


def part_one():
    valid = 0
    for [min, max, char, password] in entries:
        count = password.count(char)
        if min <= count and count <= max:
            valid += 1
    return valid


def part_two():
    valid = 0
    for [a, b, char, password] in entries:
        has_a = password[a - 1] == char
        has_b = password[b - 1] == char
        if has_a or has_b:
            if has_a != has_b:
                valid += 1
    return valid


print("Part one:", part_one())
print("Part two:", part_two())
