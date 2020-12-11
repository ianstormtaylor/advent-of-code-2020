import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).read().strip().split("\n")
matrix = [[l for l in line] for line in lines]
hash = {}
points = []
directions = []

for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
        hash[(x, y)] = cell

for x in range(0, len(matrix[0])):
    for y in range(0, len(matrix)):
        points.append((x, y))

for x in range(-1, 2):
    for y in range(-1, 2):
        if x != 0 or y != 0:
            directions.append((x, y))


def is_occupied(seats, point, direction, infinite = False):
    if seats.get(point) == '.':
        return None
    x, y = point
    xx, yy = direction
    target = (x + xx, y + yy)
    target_seat = seats.get(target)
    while infinite and target_seat == '.':
        target = (target[0] + xx, target[1] + yy)
        target_seat = seats.get(target)
        if target_seat is None:
            return False
    return target_seat == '#'


def count(seats, point, infinite = False):
    occupied = 0
    for d in directions:
        if is_occupied(seats, point, d, infinite):
            occupied += 1
    return occupied


def get_changes(seats, threshold, infinite = False):
    changes = {}
    for p in points:
        seat = seats.get(p)
        occ = count(seats, p, infinite)
        if seat == 'L' and occ == 0:
            changes[p] = '#'
        elif seat == '#' and occ >= threshold:
            changes[p] = 'L'
    return changes


def run(threshold, infinite = False):
    seats = hash.copy()
    while True:
        changes = get_changes(seats, threshold, infinite)
        seats.update(changes)
        if len(changes) == 0:
            break
    count = len([v for v in seats.values() if v == '#'])
    return count


def part_one():
    return run(4)


def part_two():
    return run(5, True)


print("Part one:", part_one())
print("Part two:", part_two())
