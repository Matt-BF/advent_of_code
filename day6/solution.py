with open("input.txt") as f:
    stream = list(f.readline().strip())


def solution(num_chars):
    for position, i in enumerate(range(len(stream) - num_chars + 1), start=num_chars):
        window = stream[i : i + num_chars]
        if len(window) == len(set(window)):
            return position


print(f"Part 1: {solution(4)}")
print(f"Part 2: {solution(14)}")