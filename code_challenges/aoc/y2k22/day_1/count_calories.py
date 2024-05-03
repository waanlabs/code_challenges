"""
Count Calories - AoC Day 1 (compatative programming)
"""

# Part 1
puzzle_file_path: str = "./puzzle-input.txt"

with open(puzzle_file_path, "r", encoding="utf-8") as file:
    calories_list = [int(line) if line.strip() else "" for line in file]

calories_sum: list[int] = []
calories_group_sum: int = 0

for calories in calories_list:
    if calories != "":
        calories_group_sum += int(calories)

    else:
        if calories_group_sum != 0:
            calories_sum.append(calories_group_sum)

        calories_group_sum: int = 0

if calories_group_sum != 0:
    calories_sum.append(calories_group_sum)

print(f"Part 1: {max(calories_sum)}")

# Part 2
calories_sum.sort(reverse=True)
print(f"Part 2: {sum(calories_sum[:3])}")
