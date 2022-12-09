dir_structure = {"/": []}
from collections import defaultdict

path = []
totals = defaultdict(int)

with open("input.txt") as f:
    for line in f:
        split_line = line.split()
        if split_line[1] == "ls":
            continue
        elif split_line[1] == "cd":
            if split_line[2] == "..":
                path.pop()
            else:
                totals[split_line[2]] += 0
                path.append(split_line[2])
        elif split_line[0].isnumeric():
            size = int(split_line[0])
            for i in range(len(path) + 1):
                last_dir_on_path = "/".join(path[:i])
                totals[last_dir_on_path] += size

print(sum(total for total in totals.values() if total <= 100000))

total_space = 70_000_000
space_needed = 30_000_000
free_space = total_space - totals["/"]
update_space = space_needed - free_space

print(min(total for total in totals.values() if total >= update_space))

