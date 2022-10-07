import sys
from io import StringIO

test_input = """6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End"""

test_input1 = """5, 6
. . . . . .
. . . . . .
Y C D D . .
. . . C . .
. . . C . .
right-3
down-3"""

test_input2 = """5, 2
. .
. .
. Y
. .
. G
up-1
left-11
down-10
End"""

sys.stdin = StringIO(test_input2)


def print_matrix(the_matrix):
    for r in the_matrix:
        print(*r, end="\n")


def count_items(the_matrix, the_rows, the_cols):
    result = 0
    santa_position = ()
    for row in range(the_rows):
        for col in range(the_cols):
            if the_matrix[row][col] not in "Y, .":
                result += 1
            elif the_matrix[row][col] == "Y":
                santa_position = (row, col)
    return result, santa_position


def next_move(the_row, the_col, the_direction,
              max_row, max_column):
    directions = {
        "up": (the_row - 1, the_col),
        "down": (the_row + 1, the_col),
        "left": (the_row, the_col - 1),
        "right": (the_row, the_col + 1),
    }
    next_row, next_col = directions[the_direction]
    if 0 <= next_row < max_row and 0 <= next_col < max_column:
        return next_row, next_col
    else:
        if next_row < 0:
            return next_row + max_row, next_col
        elif next_row >= max_row:
            return next_row - max_row, next_col
        elif next_col < 0:
            return next_row, next_col + max_column
        else:
            return next_row, next_col - max_column


rows, cols = [int(x) for x in input().split(", ")]

matrix = [input().split(" ") for _ in range(rows)]

number_of_items = count_items(matrix, rows, cols)[0]

items_vault = {
    "D": 0,
    "G": 0,
    "C": 0
}

items_names = {
    "D": "Christmas decorations",
    "G": "Gifts",
    "C": "Cookies"
}

player_row, player_col = count_items(matrix, rows, cols)[1]
command = input()
while command != "End" and number_of_items > 0:
    current_command = command.split("-")
    direction = current_command[0]
    steps = int(current_command[1])
    for step in range(steps):
        if number_of_items > 0:
            current_row, current_col = next_move(player_row, player_col, direction, rows, cols)
            current_item = matrix[current_row][current_col]
            if current_item in items_vault.keys():
                items_vault[current_item] += 1
                number_of_items -= 1
            matrix[current_row][current_col] = "Y"
            matrix[player_row][player_col] = "x"
            player_row, player_col = current_row, current_col
        else:
            print("Merry Christmas!")
            break
    if number_of_items > 0:
        command = input()
    else:
        break

print("You've collected:")

for item, value in items_vault.items():
    print(f"- {value} {items_names[item]}")

print_matrix(matrix)
