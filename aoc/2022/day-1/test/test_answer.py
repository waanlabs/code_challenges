from answer import CalorieCounter
from unittest.mock import patch, mock_open
import unittest
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestCalorieCounter(unittest.TestCase):

    def setUp(self):
        # Mock environment variable
        patcher = patch('os.getenv', return_value='/path/to/folder')
        self.mock_getenv = patcher.start()
        self.addCleanup(patcher.stop)

    def test_initialization(self):
        counter = CalorieCounter()
        self.assertEqual(counter.project_folder, '/path/to/folder')

    def test_read_and_process_file_not_found(self):
        counter = CalorieCounter()
        with self.assertRaises(FileNotFoundError):
            counter.read_and_process()

    def test_read_and_process_valid_data(self):
        mock_data = "100\n200\n\n300\n400\n"
        counter = CalorieCounter()
        with patch('builtins.open', mock_open(read_data=mock_data)):
            counter.read_and_process()
            self.assertEqual(counter.calories_sum, [300, 700])

    def test_max_group_sum(self):
        counter = CalorieCounter()
        counter.calories_sum = [300, 700, 500]
        self.assertEqual(counter.max_group_sum(), 700)

    def test_sum_of_largest_three(self):
        counter = CalorieCounter()
        counter.calories_sum = [300, 700, 500, 800, 400]
        self.assertEqual(counter.sum_of_largest_three(), 2000)


if __name__ == '__main__':
    unittest.main()
