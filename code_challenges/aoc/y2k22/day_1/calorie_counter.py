"""
This module contains optimized calorie_counter solution for Advent of Code 2022 - Day 1. This is a class and
function/ based solution for learning industrial programming practices.
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
import sys

# from pydantic import BaseModel
# from icecream import ic


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

    file_path: str
    calories_sum: list[int]

    def __init__(self, file_path: str) -> None:
        """
        Constructs all the necessary attributes for the CalorieCounter object.

        Parameters
        ----------
        file_path : str
            file path of the calorie data
        """
        self._file_path = file_path

    @property
    def puzzle_file_path(self) -> str:
        """
        Get the file path associated with the calorie counter and return as an immutable string.

        Parameters:
        - value (str): The file path to set.

        Returns:
            str: The file path.
        """
        return self._file_path

    @puzzle_file_path.setter
    def puzzle_file_path(self, path: str) -> None:
        """
        Set the file path for the puzzle input.

        Parameters:
        - path (str): The file path to set.

        Returns:
        - None

        Raises:
        - ValueError: If the file path is an empty string.
        - TypeError: If the file path is not a string.
        """
        self._file_path = path

    def read_and_process(self) -> None:
        """
        Reads the file and processes the calorie data.
        """
        if not self.puzzle_file_path:
            raise ValueError("File path must not be empty.")

        if not isinstance(self.puzzle_file_path, str):
            raise TypeError("File path must be a string.")

        with open(self.puzzle_file_path, "r", encoding="utf-8") as file:
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
#     try:
#         calorie_counter = CalorieCounter("./puzzle-input.txt")
#         calorie_counter.read_and_process()

#         ic(calorie_counter.puzzle_file_path)
#         ic(calorie_counter.max_group_sum())
#         ic(calorie_counter.sum_of_largest_three())

#         # print(f"Max group sum: {calorie_counter.max_group_sum()}")
#         # print(f"Sum of largest three: {calorie_counter.sum_of_largest_three()}")
#     catch (ValueError, TypeError)  as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     """
#     If the script is being run directly (not imported as a module), the test function is called.
#     """
#     test()
