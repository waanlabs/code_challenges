with open('./day-2/puzzle-input.txt', 'r') as file:
    rounds = [line.replace(" ", "").strip("\n") for line in file]

# print(rounds)

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
print(expected_score)

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
print(desired_score)
