import os

file = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(file) as f:
  lines = f.readlines()
  numbers = list(map(int, lines))

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

print('Part one:', part_one())
print('Part two:', part_two())