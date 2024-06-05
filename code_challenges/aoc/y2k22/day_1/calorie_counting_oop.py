"""
This module contains an optimized object-oriented solution for Advent of Code (AoC) 2022 - Day 1.

Package: code_challenges
Subpackage: aoc/y2k22/day_1
File: calorie_counting_oop.py
Author: waanlabs <support@waanlabs.com>
Version: 1.0.0
Created: 01/12/2022 by waanlabs
Modified: 02/06/2024 by waanlabs
"""

# import gc
import heapq
import itertools

# import cProfile
# import pstats
from typing import Union
from data_config import DataConfig
from aoc_data_reader import AocDataReader

# from icecream import ic
# from pympler import asizeof


class CalorieCounting:
    """
    The class CalorieCounting is designed to read calorie data from a file, process the data to
    calculate the group with the maximum calories, and determine the sum of the three largest
    calorie groups.

    Attributes
    ----------
    calories_sum: list[int]
        A list of calorie sums by calorie groups.

    Methods
    -------
    @property
    puzzle_file_path()
        Returns the file path associated with the calorie counter.
    @puzzle_file_path.setter
    puzzle_file_path()
        Set the file path for the puzzle input.
    read_calaories()
        Reads the file and create a list.
    process_calories()
        Processes the calorie data.
    max_group_sum()
        Returns the maximum sum of calorie groups.
    sum_of_largest_three()
        Returns the sum of the three largest calorie groups.
    """

    calories_sum: list[int]

    def __init__(self, file_path: str) -> None:
        """
        Constructs all the necessary attributes for the calorie counter object.

        Parameters
        ----------
        file_path: str
            The file path of the calorie data.
        """
        self.puzzle_file_path = file_path
        self.data_reader = AocDataReader()

    def __del__(self) -> None:
        """
        Call destructor to free up memory (C-style).

        This method is automatically called when the object is about to be destroyed.
        It can be used to perform any necessary cleanup operations before the object is
        removed from memory.

        Note
        ----
        Since Python is a garbage-collected language, explicit deletion is not necessary.
        The purpose of this method is to provide a way to release any resources or perform
        cleanup tasks.
        """
        if hasattr(self, "calories_sum"):
            del self.calories_sum

        if hasattr(self, "_file_path"):
            del self._file_path

        if hasattr(self, "data_reader"):
            del self.data_reader

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
        file_path: str
            The file path to set.
        """
        data_config = DataConfig(file_path=file_path)
        self._file_path = data_config.file_path

    @puzzle_file_path.deleter
    def puzzle_file_path(self) -> None:
        """
        Delete the file path associated with the calorie counter.

        Note
        ----
        This method is not necessary since the destructor is called automatically.
        """
        del self._file_path

    def read_calories(self) -> list[Union[int | str]]:
        """
        Read the calories data from file and return a list of integers or empty strings.

        Returns
        -------
        list[Union[int, str]]
            The calorie data.
        """
        return self.data_reader.read_data(self.puzzle_file_path)

    def process_calories(self, calories: list[Union[int | str]]) -> int | None:
        """
        Processes the calorie list.

        parameters
        ----------
        calories: list[int | str]
            list of integers or empty strings representing calorie data, or None.
        """
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
    This function creates an instance of the CalorieCounter class, reads and processes the calorie
    data, and then prints the sum of  maximum calories group  and the sum of the three largest
    calorie groups.
    """
    try:
        file_path = "./puzzle-input.txt"
        # file_path = "./code_challenges/aoc/y2k22/day_1/puzzle-input.txt"
        calorie_counting = CalorieCounting(file_path)
        calories_list = calorie_counting.read_calories()
        calorie_counting.process_calories(calories_list)

        # ic(calorie_counting.puzzle_file_path)
        # ic(calorie_counting.max_group_sum())
        # ic(calorie_counting.sum_of_largest_three())

        print(calorie_counting.puzzle_file_path)
        print(calorie_counting.max_group_sum())
        print(calorie_counting.sum_of_largest_three())

        del calorie_counting.puzzle_file_path

        # print(asizeof.asized(calorie_counting, detail=1).format())

    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"Application Error: {error}")


if __name__ == "__main__":
    """
    If the script is being run directly (not imported as a module), the test function is
    called.
    """
    # gc.disable()
    # profiler = cProfile.Profile()
    # profiler.enable()
    test()
    # profiler.disable()
    # profiler.print_stats(sort="time")
    # stats = pstats.Stats(profiler).sort_stats("time")
    # stats.dump_stats("my.prof")
    # gc.enable()

"""
Path: code_challenges/aoc/y2k22/day_1/calorie_counter.py
End of count_calories_oop.py
"""
