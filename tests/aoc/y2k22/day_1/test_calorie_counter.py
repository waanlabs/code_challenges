import unittest
from code_challenges.aoc.y2k22.day_1.calorie_counter import CalorieCounter


class TestCalorieCounter(unittest.TestCase):

    max_group_sum = 67633
    sum_of_largest_three = 199628
    file_path = "./code_challenges/aoc/y2k22/day_1/puzzle-input.txt"

    def setUp(self) -> None:
        self.calorie_counter = CalorieCounter(self.file_path)
        self.calorie_counter.read_and_process()

    def test_puzzle_file_path_getter(self) -> None:
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter.puzzle_file_path, self.file_path)

    def test_puzzle_file_path_setter(self) -> None:
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter._file_path, self.file_path)

    # def test_read_and_process_empty_file(self) -> None:
    #     self.calorie_counter.puzzle_file_path = ()
    #     self.calorie_counter.read_and_process()
    #     self.assertEqual(len(self.calorie_counter.calories_sum), 0)

    # def test_read_and_process_invalid_file(self) -> None:
    #     self.calorie_counter.puzzle_file_path = 123
    #     with self.assertRaises(ValueError):
    #         self.calorie_counter.read_and_process()

    def test_read_and_process_valid_file(self) -> None:
        self.calorie_counter.puzzle_file_path = self.file_path
        self.calorie_counter.read_and_process()
        self.assertIsNotNone(self.calorie_counter.calories_sum)

    def test_max_group_sum(self) -> None:
        self.assertEqual(self.calorie_counter.max_group_sum(), self.max_group_sum)

    def test_sum_of_largest_three(self) -> None:
        self.assertEqual(
            self.calorie_counter.sum_of_largest_three(), self.sum_of_largest_three
        )


if __name__ == "__main__":
    unittest.main()
