import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
groups = open(file).read().strip().split('\n\n')

def accumulate(group, intersection = False):
  answers = None
  for line in group.split('\n'):
    if answers is None:
      answers = set(line)
    elif intersection:
      answers = answers.intersection(set(line))
    else:
      answers = answers.union(set(line))
  return answers

def part_one():
  return sum([len(accumulate(g)) for g in groups])

def part_two():
  return sum([len(accumulate(g, True)) for g in groups])

print('Part one:', part_one())
print('Part two:', part_two())