import os
import re

file = os.path.join(os.path.dirname(__file__), "input.txt")
passports = []
fields = {
    'byr': lambda x: re.match(r'^\d{4}$', x) and '1920' <= x and x <= '2002',
    'iyr': lambda x: re.match(r'^\d{4}$', x) and '2010' <= x and x <= '2020',
    'eyr': lambda x: re.match(r'^\d{4}$', x) and '2020' <= x and x <= '2030',
    'hgt': lambda x: re.match(r'^(15[0-9]|1[6-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in$', x),
    'hcl': lambda x: re.match(r'^#[0-9a-f]{6}$', x),
    'ecl': lambda x: re.match(r'^amb|blu|brn|gry|grn|hzl|oth$', x),
    'pid': lambda x: re.match(r'^\d{9}$', x),
}

with open(file) as f:
    lines = f.readlines()
    passport = {}

    for line in lines:
        if line.strip() == '':
            passports.append(passport)
            passport = {}
        else:
            pairs = re.findall(r"\w{3}:[^ ]+", line)
            for pair in pairs:
                search = re.search(r"(\w{3}):(.*)", pair)
                key = search.group(1)
                value = search.group(2)
                passport[key] = value
    
    passports.append(passport)

def check(passport, validation = False):
    for f in fields:
        if not f in passport:
            return False
        elif validation and not fields[f](passport[f]):
            return False
    return True

def part_one():
    return len(list(filter(lambda p: check(p), passports)))

def part_two():
    return len(list(filter(lambda p: check(p, True), passports)))

print("Part one:", part_one())
print("Part two:", part_two())
