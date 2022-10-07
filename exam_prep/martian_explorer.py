import sys
from io import StringIO

test_input = """- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left"""

test_input1 = """R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right
"""

test_input2 = """R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left"""

sys.stdin = StringIO(test_input2)


def print_matrix(the_matrix):
    for r in the_matrix:
        print(*r, end="\n")


def get_player_position(the_matrix):
    result = ()
    for row in range(len(the_matrix)):
        for col in range(len(the_matrix)):
            if the_matrix[row][col] == "E":
                result = row, col
    return result


def next_move(current_row, current_col, command, the_matrix):
    direction = {
        "up": (current_row - 1, current_col),
        "down": (current_row + 1, current_col),
        "left": (current_row, current_col - 1),
        "right": (current_row, current_col + 1),
    }
    next_row, next_col = direction[command]
    if 0 <= next_row < len(the_matrix) and 0 <= next_col < len(the_matrix):
        return next_row, next_col
    else:
        if next_row < 0:
            return next_row + len(the_matrix), next_col
        elif next_row >= len(the_matrix):
            return next_row - len(the_matrix), next_col
        elif next_col < 0:
            return next_row, next_col + len(the_matrix)
        else:
            return next_row, next_col - len(the_matrix)


def driving_rover(moves, the_matrix):
    deposit_types = {
        "W": "Water",
        "M": "Metal",
        "C": "Concrete"
    }
    deposit_found = ["W", "M", "C"]
    current_row, current_col = get_player_position(the_matrix)
    for command in moves:
        next_row, next_col = next_move(current_row, current_col, command, the_matrix)
        if the_matrix[next_row][next_col] == "R":
            print(f"Rover got broken at ({next_row}, {next_col})")
            break
        elif the_matrix[next_row][next_col] in deposit_types.keys():
            current_deposit = deposit_types[the_matrix[next_row][next_col]]
            print(f"{current_deposit} deposit found at ({next_row}, {next_col})")
            if the_matrix[next_row][next_col] in deposit_found:
                deposit_found.remove(f"{the_matrix[next_row][next_col]}")
        current_row, current_col = next_row, next_col

    if deposit_found:
        print("Area not suitable to start the colony.")
    else:
        print("Area suitable to start the colony.")


COLUMNS_COUNT = 6
ROWS_COUNT = 6

matrix = [input().split(" ") for _ in range(ROWS_COUNT)]
commands = input().split(", ")

driving_rover(commands, matrix)
