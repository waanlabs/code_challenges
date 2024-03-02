"""
This module contains optimized calorie_counter solution for Advent of Code 2022 - Day 1. This is a class and
method/function based solution for learning industrial programming practices.
----

Package: code_challenges
Subpackage: code_challenges/aoc/y2k22/day_1
File: calorie_counter.py
Author: Waan <admin@waan.email>
Version: 1.0.0
Created: 01/12/2022
Modified: 01/02/2024 by admin@waan.email
"""

import itertools
import heapq
import os


class CalorieCounter:
    """
    Class to count calories by reading a data file.
    ----

    Attributes
    ----------
    file_path : str
        a formatted string to print out the file_path
    calories_sum : list
        a list of sums of calorie groups

    Methods
    -------
    read_and_process():
        Reads the file and processes the calorie data.
    max_group_sum():
        Returns the maximum sum of calorie groups.
    sum_of_largest_three():
        Returns the sum of the three largest calorie groups.
    """

    def __init__(self, file_path: str) -> None:
        """
        Constructs all the necessary attributes for the CalorieCounter object.

        Parameters
        ----------
        file_path : str
            file path of the calorie data
        """
        self.file_path = file_path
        self.calories_sum: list[int] = []

    def read_and_process(self) -> None:
        """
        Reads the file and processes the calorie data.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as file:
            calories = [int(line) if line.strip() else "" for line in file]

            self.calories_sum = [
                sum(x for x in group if isinstance(x, int))
                for is_empty, group in itertools.groupby(calories, lambda x: x == "")
                if not is_empty
            ]

    def max_group_sum(self) -> int | None:
        """
        Returns the maximum sum of calorie groups.

        Returns
        -------
        int | None
            The maximum sum of calorie groups or None if there are no groups.
        """
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int | None:
        """
        Returns the sum of the three largest calorie groups.

        Returns
        -------
        int | None
            The sum of the three largest calorie groups or None if there are less than three groups.
        """
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None


# def test() -> None:
#     """
#     This function creates an instance of the CalorieCounter class, reads and processes the calorie data,
#     and then prints the maximum sum of calorie groups and the sum of the three largest calorie groups.
#     """
#     calorie_counter = CalorieCounter("./puzzle-input.txt")
#     calorie_counter.read_and_process()

#     print(f"Max group sum: {calorie_counter.max_group_sum()}")
#     print(f"Sum of largest three: {calorie_counter.sum_of_largest_three()}")


# if __name__ == "__main__":
#     """
#     If the script is being run directly (not imported as a module), the test function is called.
#     """
#     test()
