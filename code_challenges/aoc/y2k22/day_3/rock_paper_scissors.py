"""
Day 3 -
"""

# Part 1
puzzle_file_path: str = "./puzzle-input.txt"

with open(puzzle_file_path, "r", encoding="utf-8") as file:
    rounds = [line.replace(" ", "").strip("\n") for line in file]
