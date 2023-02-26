import itertools
import heapq
"""
Using a bit more advance solution.

The code reads in a file located at './day-1/puzzle-input.txt' and stores its contents in a list called 'calories'.

The file is opened in read mode using the 'with open' statement, which ensures that the file is properly closed after it has been read.

The contents of the file are then read line by line using a for loop, and each line is processed using a list comprehension. The 'if line.strip()' condition in the list comprehension checks if the line is not empty or only contains whitespace characters. If the line is not empty, the 'int(line)' statement converts the line to an integer and adds it to the 'calories' list. If the line is empty or only contains whitespace characters, an empty string is added to the 'calories' list.

Finally, when the 'with open' block is exited, the file is automatically closed.
"""
with open('./day-1/puzzle-input.txt', 'r') as file:
    calories = [int(line) if line.strip() else '' for line in file]

print(calories)

"""
The code calculates the sum of consecutive non-empty groups of integers in the 'calories' list, which is assumed to have been previously defined.

The 'itertools.groupby' function is used to group the integers in 'calories' into separate lists based on whether or not they are separated by an empty string. The lambda function 'lambda x: x == '' ' is used as the key function to group the elements. If a group contains an empty string, it is considered an empty group and is ignored.

The resulting groups are passed to a list comprehension, which calculates the sum of each group using the 'sum()' function. The resulting sums are stored in a new list called 'calories_sum'.

The list comprehension uses the syntax 'for is_empty, group in itertools.groupby()', which assigns the first value of each group (whether or not it is empty) to the variable 'is_empty', and the group itself to the variable 'group'. The condition 'if not is_empty' filters out any empty groups, and the resulting sums are returned as a list.

Finally, the resulting list of sums is stored in the variable 'calories_sum'.
"""
calories_sum = [sum(group) for is_empty, group in itertools.groupby(
    calories, lambda x: x == '') if not is_empty]

# print(calories_sum)

"""
The 'max()' function takes the 'calories_sum' list as an argument and returns the highest value in the list. The resulting value is then passed to the 'print()' function, which displays it in the console.
"""
# print(max(calories_sum))  # 1st answer

"""
The 'heapq.nlargest()' function is used to find the three largest values in the 'calories_sum' list. The first argument of 'heapq.nlargest()' is the number of largest values to return, which in this case is three. The second argument is the list to search, which is the 'calories_sum' list. The resulting values are returned as a list.

The 'sum()' function is then used to calculate the sum of the three largest values in the list. The resulting sum is passed to the 'print()' function, which displays it in the console.
"""
# print(sum(heapq.nlargest(3, calories_sum)))  # 2nd answer
