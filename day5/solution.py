from collections import defaultdict
import re
import sys


def answer(part):
    with open("input.txt") as f:
        crates, actions = f.read().split("\n\n")
    stacks = defaultdict(list)
    crates = crates.splitlines()
    # remove index not needed
    crates.pop()
    for stack in crates:
        for i in range(len(stack) // 4 + 1):
            if stack[i * 4 + 1] != " ":
                stacks[i + 1].append(stack[i * 4 + 1])

    for i in stacks:
        stacks[i].reverse()
    for action in actions.splitlines():
        count, src, dest = map(int, re.findall("\d+", action))
        move = stacks[src][-1 * count :]
        del stacks[src][-1 * count :]
        if part == 1:
            move.reverse()
        stacks[dest] = stacks[dest] + move

    return "".join([stacks[i][-1] for i in sorted(stacks.keys())])


print(answer(1))
print(answer(2))

