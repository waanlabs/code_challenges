from dotenv import load_dotenv
import os
import itertools
import heapq


class CalorieCounter:
    def __init__(self) -> None:
        load_dotenv()
        self.project_folder = os.getenv('AOC_2022_ROOT')

        if self.project_folder is None:
            raise ValueError("Environment variable AOC_2022_ROOT not found")

        self.file_path = os.path.join(
            self.project_folder, 'day-1/puzzle-input.txt')

    def read_and_process(self) -> None:
        try:
            with open(self.file_path, 'r') as file:
                calories = [int(line) if line.strip() else '' for line in file]

            self.calories_sum = [sum(group) for is_empty, group in itertools.groupby(
                calories, lambda x: x == '') if not is_empty]

        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def max_group_sum(self) -> int:
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int:
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None


counter = CalorieCounter()
counter.read_and_process()

print(counter.max_group_sum())  # 1st answer
print(counter.sum_of_largest_three())  # 2nd answer
