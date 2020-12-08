import os
import re

file = os.path.join(os.path.dirname(__file__), "input.txt")
lines = open(file).read().strip().split("\n")
parent_map = {}
child_map = {}

for line in lines:
    [type, contents] = line.split(" bags contain ")
    contents = re.sub(r" bags?\.", "", contents)
    contents = re.split(r" bags?, ", contents)
    for entry in contents:
        search = re.search(r"(\d+) (\w+ \w+)", entry)
        if search:
            (c, t) = search.groups()
            if t not in parent_map:
                parent_map[t] = {}
            if type not in child_map:
                child_map[type] = {}
            parent_map[t][type] = int(c)
            child_map[type][t] = int(c)


def get_containers(type):
    containers = set()
    if type in parent_map:
        keys = parent_map[type].keys()
        containers.update(keys)
        for k in keys:
            containers.update(get_containers(k))
    return containers


def count_children(type):
    count = 0
    if type in child_map:
        for key in child_map[type]:
            value = child_map[type][key]
            count += value
            count += count_children(key) * value
    return count


def part_one():
    containers = get_containers("shiny gold")
    return len(containers)


def part_two():
    count = count_children("shiny gold")
    return count


print("Part one:", part_one())
print("Part two:", part_two())
