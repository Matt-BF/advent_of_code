def part_one():
    # score= shape + outcome (rock=1, paper=2, scissors=3) + (lost=0, tie=3, won=6)
    mapping = {"A": ["Y", "Z"], "B": ["Z", "X"], "C": ["X", "Y"]}
    scores = {"X": 1, "Y": 2, "Z": 3}
    results = []

    with open("input.txt") as f:
        for line in f:
            game = {line.split()[0]: line.split()[1]}
            for key, value in game.items():
                if value == mapping[key][0]:  # means I won
                    results.append(scores[value] + 6)
                elif value == mapping[key][1]:  # means I lost
                    results.append(scores[value] + 0)
                else:  # means we tied
                    results.append(scores[value] + 3)
    return sum(results)


def part_two():
    mapping = {"A": [1, "C", "B"], "B": [2, "A", "C"], "C": [3, "B", "A"]}
    results = []

    with open("input.txt") as f:
        for line in f:
            game = {line.split()[0]: line.split()[1]}
            for key, value in game.items():
                if value == "X":  # means I need to lose
                    results.append(mapping[mapping[key][1]][0] + 0)
                elif value == "Y":  # means I need to draw
                    results.append(mapping[key][0] + 3)
                else:  # means i need to win
                    results.append(mapping[mapping[key][2]][0] + 6)
        return sum(results)


print(f"part one:{part_one()}")
print(f"part two:{part_two()}")
