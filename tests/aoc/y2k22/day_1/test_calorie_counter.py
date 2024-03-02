import unittest
from code_challenges.aoc.y2k22.day_1.calorie_counter import CalorieCounter


class TestCalorieCounter(unittest.TestCase):

    max_group_sum = 67633
    sum_of_largest_three = 199628
    file_path = "./code_challenges/aoc/y2k22/day_1/puzzle-input.txt"

    def setUp(self) -> None:

        self.calorie_counter = CalorieCounter(self.file_path)
        self.calorie_counter.read_and_process()

    def test_file_not_found(self):
        error_calorie_counter = CalorieCounter("./puzzle-input.txt")

        with self.assertRaises(FileNotFoundError) as context:
            error_calorie_counter.read_and_process()

        expected_error_message = (
            f"File not found: {error_calorie_counter.puzzle_file_path}"
        )
        self.assertEqual(str(context.exception), expected_error_message)

    def test_puzzle_file_path_setter(self):
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter._file_path, self.file_path)

    def test_set_puzzle_file_path(self) -> None:
        self.calorie_counter.puzzle_file_path = self.file_path
        self.assertEqual(self.calorie_counter.puzzle_file_path, self.file_path)

    def test_max_group_sum(self) -> None:
        self.assertEqual(self.calorie_counter.max_group_sum(), self.max_group_sum)

    def test_sum_of_largest_three(self) -> None:
        self.assertEqual(
            self.calorie_counter.sum_of_largest_three(), self.sum_of_largest_three
        )


if __name__ == "__main__":
    unittest.main()
