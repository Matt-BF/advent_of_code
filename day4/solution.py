def part_one():
    num_subsets = 0
    with open("input.txt") as f:
        for line in f:
            groups = list(line.strip().split(","))
            range_groups = [
                list(range(int(group.split("-")[0]), int(group.split("-")[1]) + 1))
                for group in groups
            ]
            if set(range_groups[0]).issubset(set(range_groups[1])) or set(
                range_groups[1]
            ).issubset(set(range_groups[0])):
                num_subsets += 1
    return num_subsets


def part_two():
    num_subsets = 0
    with open("input.txt") as f:
        for line in f:
            groups = list(line.strip().split(","))
            range_groups = [
                list(range(int(group.split("-")[0]), int(group.split("-")[1]) + 1))
                for group in groups
            ]
            if any(num in range_groups[0] for num in range_groups[1]) or any(
                num in range_groups[1] for num in range_groups[0]
            ):
                num_subsets += 1
    return num_subsets


print(part_one())
print(part_two())
