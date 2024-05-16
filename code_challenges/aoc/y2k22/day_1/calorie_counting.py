"""
Day 1 - Calorie Counting
"""

# Part 1
puzzle_file_path: str = "./puzzle-input.txt"

with open(puzzle_file_path, "r", encoding="utf-8") as file:
    calorie_list = [int(line) if line.strip() else "" for line in file]

calorie_sum: list[int] = []
calorie_group_sum: int = 0


for calorie in calorie_list:
    if calorie != "":
        calorie_group_sum += int(calorie)
    else:
        if calorie_group_sum != 0:
            calorie_sum.append(calorie_group_sum)
            calorie_group_sum: int = 0

if calorie_group_sum != 0:
    calorie_sum.append(calorie_group_sum)

print(f"Part 1: {max(calorie_sum)}")

# Part 2
calorie_sum.sort(reverse=True)
print(f"Part 2: {sum(calorie_sum[:3])}")
