import itertools
import heapq

with open('./day-1/puzzle-input.txt', 'r') as file:
    calories = [int(line) if line.strip() else '' for line in file]

calories_sum = [sum(group) for is_empty, group in itertools.groupby(
    calories, lambda x: x == '') if not is_empty]

print(max(calories_sum))  # 1st answer

print(sum(heapq.nlargest(3, calories_sum)))  # 2nd answer
