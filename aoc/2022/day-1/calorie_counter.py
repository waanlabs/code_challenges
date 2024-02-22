import itertools
import heapq
import os


class CalorieCounter:
    def read_and_process(self) -> None:
        file_path = './aoc/2022/day-1/puzzle-input.txt'

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        with open(file_path, 'r') as file:
            calories = [int(line) if line.strip() else '' for line in file]

            self.calories_sum = [sum(group) for is_empty, group in itertools.groupby(
                calories, lambda x: x == '') if not is_empty]

        return self.calories_sum

    def max_group_sum(self) -> int:
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int:
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None
