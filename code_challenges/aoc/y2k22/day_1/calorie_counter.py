"""
Advent of Code 2022 - Day 1 optimized solution in Python

Author: waan<admin@waan.email>
Date: 2021-12-01
"""

import itertools
import heapq
import os


class CalorieCounter:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_and_process(self) -> None:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r") as file:
            calories = [int(line) if line.strip() else "" for line in file]

            self.calories_sum = [
                sum(group)
                for is_empty, group in itertools.groupby(calories, lambda x: x == "")
                if not is_empty
            ]

    def max_group_sum(self) -> int | None:
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int | None:
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None
