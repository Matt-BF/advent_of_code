import numpy as np

trees = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        trees.append([int(num) for num in line])


vis = (2 * len(trees)) + (2 * (len(trees[0]) - 2))
distance = 0

for y, row in enumerate(trees):
    if y in [0, len(trees) - 1]:
        continue
    for x, col in enumerate(row):
        if x in [0, len(row) - 1]:
            continue
        tree = trees[y][x]
        up = [tree > row[x] for row in trees[:y]]
        up_d = sorted(
            (y - idx) if tree <= row[x] else y for idx, row in enumerate(trees[:y])
        )
        down = [tree > row[x] for row in trees[y + 1 :]]
        down_d = sorted(
            (idx + 1) if tree <= row[x] else (len(trees) - y - 1)
            for idx, row in enumerate(trees[y + 1 :])
        )
        left = [tree > col for col in trees[y][:x]]
        left_d = sorted(
            (x - idx) if tree <= col else x for idx, col in enumerate(trees[y][:x])
        )
        right = [tree > col for col in trees[y][x + 1 :]]
        right_d = sorted(
            (idx + 1) if tree <= col else (len(trees[0]) - x - 1)
            for idx, col in enumerate(trees[y][x + 1 :])
        )
        # part one
        if all(up) or all(down) or all(left) or all(right):
            vis += 1
        # part two
        if up_d[0] * down_d[0] * left_d[0] * right_d[0] > distance:
            distance = up_d[0] * down_d[0] * left_d[0] * right_d[0]


print(vis)
print(distance)

