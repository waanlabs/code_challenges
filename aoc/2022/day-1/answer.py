import itertools
import heapq
import os

class CalorieCounter:
    def read_and_process(self) -> None:
        file_path = './puzzle-input.txt'
        
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return 
        
        with open(file_path, 'r') as file:
            calories = [int(line) if line.strip() else '' for line in file]
                
            self.calories_sum = [sum(group) for is_empty, group in itertools.groupby(
                calories, lambda x: x == '') if not is_empty]

    def max_group_sum(self) -> int:
        return max(self.calories_sum) if self.calories_sum else None

    def sum_of_largest_three(self) -> int:
        return sum(heapq.nlargest(3, self.calories_sum)) if self.calories_sum else None

# Example usage
counter = CalorieCounter()
counter.read_and_process()

if hasattr(counter, 'calories_sum'):
    print(counter.max_group_sum())  # 1st answer
    print(counter.sum_of_largest_three())  # 2nd answer
    
else:
    print("File read error.")
