"""
This module contains optimized calorie_counter solution for Advent of Code 2022 - Day 1.

This is a class and
function/ based solution for learning industrial programming practices.

Package: code_challenges
Subpackage: code_challenges/aoc/y2k22/day_1
File: calorie_counter.py
Author: Waan <admin@waan.email>
Version: 1.0.0
Created: 01/12/2022
Modified: 01/02/2024 by admin@waan.email
"""

import heapq
import itertools
from typing import Union
from icecream import ic

# from pydantic import BaseModel


class CalorieCounter:
    """
    Class to count calories by reading a data file.

    Attributes
    ----------
    file_path : str
        The file path of the calorie data.
    calories_sum : list
        A list of sums of calorie groups.

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
            The file path of the calorie data.
        """
        self.puzzle_file_path = file_path

    @property
    def puzzle_file_path(self) -> str:
        """
        Return the file path associated with the calorie counter as an immutable string.

        Returns
        -------
        str
            The file path.
        """
        return self._file_path

    @puzzle_file_path.setter
    def puzzle_file_path(self, file_path: str) -> None:
        """
        Set the file path for the puzzle input.

        Parameters
        ----------
        file_path : str
            The file path to set.

        Raises
        ------
        ValueError
            If the file path is an empty string.
        TypeError
            If the file path is not a string.
        """
        if not file_path:
            raise ValueError("File path must not be empty.")

        if not isinstance(file_path, str):
            raise TypeError("File path must be a string.")

        self._file_path = file_path

    def read_calaories(self) -> list[Union[int | str]]:
        """
        Reads the file and processes the calorie data.

        returns
        -------
        list[Union[int, str]]
            The calorie data.

        variables
        ---------
        calories: list[Union[int, str]]
            list of integers or empty strings representing calorie data, or None

        Raises
        ------
        FileNotFoundError
            If the file is not found.
        """

        calories: list[Union[int | str]]

        try:
            with open(self.puzzle_file_path, "r", encoding="utf-8") as file:
                calories = [int(line) if line.strip() else "" for line in file]

        except FileNotFoundError as error:
            raise FileNotFoundError(f"File not found: {error}") from error
        except ValueError as error:
            raise ValueError(f"Invalid data: {error}") from error

        return calories

    def process_calories(self, calories: list[Union[int | str]]) -> None:
        """
        Processes the calorie data.

        parameters
        ----------
        calories : list[int]
            The calorie data to process.

        Raises
        ------
        ValueError
            If the calorie data is empty.
        """
        if not calories:
            raise ValueError(
                "Calorie data must not be empty, make sure the file is not empty and contains valid data."
            )

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


def test() -> None:
    """
    This function creates an instance of the CalorieCounter class, reads and processes the calorie data,
    and then prints the maximum sum of calorie groups and the sum of the three largest calorie groups.
    """
    try:
        calorie_counter = CalorieCounter("./puzzle-input.txt")
        file = calorie_counter.read_calaories()
        calorie_counter.process_calories(file)

        ic(calorie_counter.puzzle_file_path)
        ic(calorie_counter.max_group_sum())
        ic(calorie_counter.sum_of_largest_three())

    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"System error: {error}")


if __name__ == "__main__":
    """If the script is being run directly (not imported as a module), the test function is called."""
    test()
