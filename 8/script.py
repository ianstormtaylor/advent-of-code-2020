import os
import re

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).read().strip().split("\n")


def parse_line(line):
    search = re.search(r"(acc|jmp|nop) (\+|\-)(\d+)", line)
    (type, sign, count) = search.groups()
    count = int(count)
    count *= -1 if sign == '-' else 1
    return (type, count)


instructions = [parse_line(l) for l in lines]


def run(list):
    visited = set()
    index = 0
    result = 0
    while index not in visited and index < len(list) and index >= 0:
        visited.add(index)
        (type, count) = list[index]
        result += count if type == 'acc' else 0
        index += count if type == 'jmp' else 1
    return result


def is_terminating(list):
    visited = set()
    index = 0
    while index < len(list) and index >= 0:
        if index in visited:
            return False
        visited.add(index)
        (type, count) = list[index]
        index += count if type == 'jmp' else 1
    return True


def part_one():
    result = run(instructions)
    return result


def part_two():
    for (i, (type, count)) in enumerate(instructions):
        if type != 'acc':
            new_type = 'jmp' if type == 'nop' else 'nop'
            new_tuple = (new_type, count)
            new_instructions = instructions.copy()
            new_instructions[i] = new_tuple
            terminates = is_terminating(new_instructions)
            if terminates:
                result = run(new_instructions)
                return result


print("Part one:", part_one())
print("Part two:", part_two())
