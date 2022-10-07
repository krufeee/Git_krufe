import sys
from io import StringIO

test_input = """1
up up up up up up up up up up up up
s
"""

test_input2 = """5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *
"""

# sys.stdin = StringIO(test_input)


sys.stdin = StringIO(test_input2)


def print_matrix(matrix):
    return [print(x) for x in matrix]


def player_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "s":
                return row, col


def possible_moves(command, row, col, matrix):
    moves = {"up": (row - 1, col),
             "down": (row + 1, col),
             "left": (row, col - 1),
             "right": (row, col + 1)
             }
    next_row, next_col = moves[command]
    if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix):
        return next_row, next_col
    else:
        return row, col


def making_move(current_player_row, current_player_col, current_commands, current_matrix, amount_of_coal):
    game_over = False
    for command in current_commands:
        next_row, next_col = possible_moves(command, current_player_row, current_player_col, current_matrix)
        if current_matrix[next_row][next_col] == "c":
            amount_of_coal -= 1
            if amount_of_coal == 0:
                print(f"You collected all coal! ({next_row}, {next_col})")
                break
        elif current_matrix[next_row][next_col] == "e":
            print(f"Game over! ({next_row}, {next_col})")
            game_over = True
        current_matrix[current_player_row][current_player_col] = "*"
        current_matrix[next_row][next_col] = "s"
        current_player_row, current_player_col = next_row, next_col
    if amount_of_coal > 0 and not game_over:
        print(f"{amount_of_coal} pieces of coal left. ({current_player_row}, {current_player_col})")


##           reading inputs

size = int(input())
commands = input().split(" ")
matrix = []

##             creating matrix
coal_count = 0

for r in range(size):
    line = input().split(" ")
    for c in line:
        if c == "c":
            coal_count += 1
    matrix.append(line)

player_row, player_col = player_position(matrix)

making_move(player_row, player_col, commands, matrix, coal_count)
