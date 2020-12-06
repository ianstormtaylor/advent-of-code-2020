import os
import re

file = os.path.join(os.path.dirname(__file__), "input.txt")
groups = open(file).read().strip().split("\n\n")
lines = [g.replace("\n", " ") for g in groups]
passports = []
for line in lines:
    passport = {}
    pairs = re.findall(r"\w{3}:[^ ]+", line)
    for pair in pairs:
        [(key, value)] = re.findall(r"(\w{3}):(.*)", pair)
        passport[key] = value
    passports.append(passport)

fields = {
    "byr": lambda x: re.match(r"^\d{4}$", x) and "1920" <= x and x <= "2002",
    "iyr": lambda x: re.match(r"^\d{4}$", x) and "2010" <= x and x <= "2020",
    "eyr": lambda x: re.match(r"^\d{4}$", x) and "2020" <= x and x <= "2030",
    "hgt": lambda x: re.match(
        r"^(15[0-9]|1[6-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$", x
    ),
    "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x),
    "ecl": lambda x: re.match(r"^amb|blu|brn|gry|grn|hzl|oth$", x),
    "pid": lambda x: re.match(r"^\d{9}$", x),
}


def check(passport, validation=False):
    for f in fields:
        if not f in passport:
            return False
        elif validation and not fields[f](passport[f]):
            return False
    return True


def part_one():
    valids = [p for p in passports if check(p)]
    return len(valids)


def part_two():
    valids = [p for p in passports if check(p, True)]
    return len(valids)


print("Part one:", part_one())
print("Part two:", part_two())
