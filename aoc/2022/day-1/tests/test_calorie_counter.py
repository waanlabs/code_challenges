import unittest
from calorie_counter import CalorieCounter


class TestCalorieCounter(unittest.TestCase):
    def setUp(self):
        self.counter = CalorieCounter()
        self.counter.read_and_process()

    def test_max_group_sum(self):
        self.assertEqual(self.counter.max_group_sum(), 67633)

    def test_sum_of_largest_three(self):
        self.assertEqual(self.counter.sum_of_largest_three(), 199628)

if __name__ == "__main__":
    unittest.main()
