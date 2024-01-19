"""
The code reads in the contents of a file named "puzzle-input.txt" located in the current directory and stores each line of the file as a string element in a list called "rounds". The "with" statement is used to open the file in read-only mode, and it automatically closes the file when the block of code inside the "with" statement is finished executing.

The list comprehension inside the "with" statement removes any spaces from each line of the file using the "replace" method and removes the newline character at the end of each line using the "rstrip" method with the "\n" argument.

Finally, the code prints out the "rounds" list, which contains all the lines from the "puzzle-input.txt" file as string elements, with spaces removed and newline characters stripped.
"""
with open('./day-2/puzzle-input.txt', 'r') as file:
    rounds = [line.replace(" ", "").strip("\n") for line in file]

# print(rounds)

"""
The code is a comment that explains the mappings and rules for a game played using three items - rock, paper, and scissors - represented by the integers 1, 2, and 3, respectively. The comment also defines the scoring system for the game, with a win worth 6 points, a draw worth 3 points, and a loss worth 0 points.

The code then defines a dictionary called "expected_outcomes" that maps each possible matchup between the three items to its expected outcome based on the game's rules. The expected outcomes are calculated using the scoring system defined in the comment.

Finally, the code uses the "sum" function to calculate the expected score for the given set of rounds using the "expected_outcomes" dictionary, which was defined earlier in the comment. The result is stored in a variable called "expected_score", which is then printed out. This value represents the total expected score for the given set of rounds based on the expected outcomes from the "expected_outcomes" dictionary.
"""
# A is Rock = 1
# B is Paper = 2
# C is Scissors = 3
#
# X assume Rock = 1
# Y assume paper = 2
# Z assume Scissors = 3
#
# {Rock,A,X} = 1
# {Paper,B,Y} = 2
# {Scissors,C,Z} = 3
#
# lose = 0
# draw = 3
# win = 6
#
# P + Q = {DRAW,LOSS,WIN}
# ----------------------------------------------
# Rounds | Result | TOTAL (Q+{DRAW,LOSS,WIN})
# ----------------------------------------------
# A vs X = DRAW   = (1+3) = 4
# A vs Y = WIN    = (2+6) = 8
# A vs Z = LOSS   = (3+0) = 3
#
# B vs X = LOSS   = (1+0) = 1
# B vs Y = DRAW   = (2+3) = 5
# B vs Z = WIN    = (3+6) = 9
#
# C vs X = WIN    = (1+6) = 7
# C vs Y = LOSS   = (2+0) = 2
# C vs Z = DRAW   = (3+3) = 6
#
# Outcomes -> 3*3 = 9
expected_outcomes = {
    "AX": 4, "AY": 8, "AZ": 3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
}

expected_score = sum(expected_outcomes[round] for round in rounds)
print(expected_score)  # 1st answer

"""
This code is a comment that explains the mappings and rules for a game played using three items - rock, paper, and scissors - represented by the integers 1, 2, and 3, respectively. The comment also defines a new scoring system for the game, with a win worth 6 points, a draw worth 3 points, and a loss worth 0 points, and assigns the labels X, Y, and Z to the values of 0, 3, and 6, respectively.

The code then defines a dictionary called "desired_outcomes" that maps each possible matchup between the three items to its expected outcome based on the new scoring system. The desired outcomes are calculated using the scoring system defined in the comment.

Finally, the code uses the "sum" function to calculate the desired score for the given set of rounds using the "desired_outcomes" dictionary, which was defined earlier in the comment. The result is stored in a variable called "desired_score", which is then printed out. This value represents the total desired score for the given set of rounds based on the desired outcomes from the "desired_outcomes" dictionary.
"""
# A is Rock = 1
# B is Paper = 2
# C is Scissors = 3

# X is lose = 0
# Y is Draw = 3
# Z is Win = 6
#
# {Rock,A} = 1
# {Paper,B} = 2
# {Scissor,C} = 3
#
# {X,lose} = 0
# {Y,draw} = 3
# {Z,win}  = 6
#
# P + Q{A,B,C} = {DRAW,LOSS,WIN}
# -----------------------------------------------------
# Rounds    | Result | TOTAL (Q{A,B,C}+{DRAW,LOSS,WIN})
# -----------------------------------------------------
# A vs X(C) = LOSE   = (3+0) = 3
# A vs Y(A) = DRAW   = (1+3) = 4
# A vs Z(B) = WIN    = (2+6) = 8
#
# B vs X(A) = LOSE   = (1+0) = 1
# B vs Y(B) = DRAW   = (2+3) = 5
# B vs Z(C) = WIN    = (3+6) = 9
#
# C vs X(B) = LOSE   = (2+0) = 2
# C vs Y(C) = DRAW   = (3+3) = 6
# C vs Z(A) = WIN    = (1+6) = 7
#
# Outcomes -> 3*3 = 9
desired_outcomes = {
    "AX": 3, "AY": 4, "AZ": 8,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 2, "CY": 6, "CZ": 7
}

desired_score = sum(desired_outcomes[round] for round in rounds)
print(desired_score)  # 2nd answer
