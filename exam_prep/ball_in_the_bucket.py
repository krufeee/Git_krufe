import sys
from io import StringIO

test_input = """10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)"""

test_input1 = """B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)"""

test_input2 = """
"""

sys.stdin = StringIO(test_input1)


def print_matrix(the_matrix):
    for r in the_matrix:
        print(*r, end="\n")


size = 6

matrix = [[x for x in input().split(" ")] for x in range(size)]
score = 0

for throw in range(3):
    current_ball = input().strip('()').split(",")
    current_row = int(current_ball[0])
    current_col = int(current_ball[1])
    if 0 <= current_row < size and 0 <= current_col < size:
        hit_box = matrix[current_row][current_col]
        if hit_box == "B":
            for box in range(size):
                if not matrix[box][current_col].isalpha():
                    score += int(matrix[box][current_col])
                else:
                    continue
        else:
            continue
    else:
        continue

if score < 100:
    needed_points = 100 - score
    print(f"Sorry! You need {needed_points} points more to win a prize.")
elif 100 <= score <= 199:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif 200 <= score <= 299:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
