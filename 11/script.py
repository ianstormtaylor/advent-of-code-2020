import os

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).read().strip().split("\n")
start = [[l for l in line] for line in lines]


def get_adjacents(input, x, y):
    x1 = max(x - 1, 0)
    x2 = min(x + 1, len(input[0]) - 1)
    y1 = max(y - 1, 0)
    y2 = min(y + 1, len(input) - 1)
    adjacents = []
    for xx in range(x1, x2 + 1):
        for yy in range(y1, y2 + 1):
            if xx == x and yy == y:
                continue
            adjacents.append(input[yy][xx])
    return adjacents


def transform(input):
    changes = 0
    next = [[cell for cell in row] for row in input]
    for y, row in enumerate(input):
        for x, cell in enumerate(row):
            adj = get_adjacents(input, x, y)
            occ = len([s for s in adj if s == '#'])
            if cell == 'L' and occ == 0:
                next[y][x] = '#'
                changes += 1 
            elif cell == '#' and occ >= 4:
                next[y][x] = 'L'
                changes += 1
    return (next, changes)


def part_one():
    next = start
    count = 0
    while True:
        (next, changes) = transform(next)
        if changes == 0:
            break
    for r in next:
        for c in r:
            if c == '#':
                count += 1
    return count


def part_two():
    return None


print("Part one:", part_one())
print("Part two:", part_two())
