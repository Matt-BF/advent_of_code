with open("input.txt") as f:
    total_calories_per_elf = []
    total_calories_current_elf = 0
    for line in f:
        if line != "\n":
            total_calories_current_elf += int(line)
        else:
            total_calories_per_elf.append(total_calories_current_elf)
            total_calories_current_elf = 0

print(max(total_calories_per_elf))
top_three_elves = sorted(total_calories_per_elf, reverse=True)[:3]
print(sum(top_three_elves))
