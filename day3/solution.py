import string

# a to z list
priorities = {
    **dict(zip(list(string.ascii_lowercase), range(1, 27))),
    **dict(zip(list(string.ascii_uppercase), range(27, 53))),
}


def part_one():
    with open("input.txt") as f:
        sum_priorities = 0
        for line in f:
            division_index = len(line.strip()) / 2
            first_compartment = line.strip()[: int(division_index)]
            second_compartment = line.strip()[int(division_index) :]
            for i in first_compartment:
                if i in second_compartment:
                    sum_priorities += priorities[i]
                    break
    return sum_priorities


def part_two():
    with open("input.txt") as f:
        sum_priorities = 0
        lines = [line.strip() for line in f]
        groups = [lines[i : i + 3] for i in range(0, len(lines), 3)]
    for group in groups:
        badge = set(group[0]).intersection(group[1], group[2])
        sum_priorities += priorities[badge.pop()]
    return sum_priorities


print(f"part one: {part_one()}")
print(f"part two: {part_two()}")
