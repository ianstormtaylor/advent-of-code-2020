import os
import re

file = os.path.join(os.path.dirname(__file__), 'input.txt')
pattern = r'^(\d+)-(\d+) (\w): (.*)$'
valid = 0

with open(file) as f:
  lines = f.readlines()
  entries = []

  for l in lines:
    search = re.search(pattern, l)
    a = int(search.group(1))
    b = int(search.group(2))
    char = search.group(3)
    password = search.group(4)
    entries.append([a, b, char, password])

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

print('Part one:', part_one())
print('Part two:', part_two())