# Christmas Elves


# elf_energies = deque([int(x) for x in input().split(" ")])
# boxes = [int(x) for x in input().split(" ")]
# turns_count = 0
# total_energy_spent = 0
# toys_count = 0
#
# while elf_energies and boxes:
#
#     while elf_energies and elf_energies[0] < 5:
#         elf_energies.popleft()
#
#     if not elf_energies:
#         break
#
#     box = boxes.pop()
#     elf_energy = elf_energies.popleft()
#
#     turns_count += 1
#
#     toys_to_be_created = 1
#     energy_to_be_spent = box
#     energy_increase_factor = 1
#
#     if turns_count % 3 == 0:
#         toys_to_be_created = 2
#         energy_to_be_spent *= 2
#     if turns_count % 5 == 0:
#         toys_to_be_created = 0
#         energy_increase_factor = 0
#     if energy_to_be_spent <= elf_energy:
#         toys_count += toys_to_be_created
#         total_energy_spent += energy_to_be_spent
#         elf_energies.append(elf_energy - energy_to_be_spent + energy_increase_factor)
#     else:
#         boxes.append(box)
#         elf_energies.append(elf_energy * 2)
#
# print(f"Toys: {toys_count}")
# print(f"Energy: {total_energy_spent}")
# if elf_energies:
#     elves_string = ", ".join(str(x) for x in elf_energies)
#     print(f"Elves left: {elves_string}")
# if boxes:
#     boxes_string = ", ".join(str(x) for x in boxes)
#     print(f"Boxes left: {boxes_string}")

## 2. Pawn Wars


import sys
from io import StringIO

test_input = """- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - b
- - - - - - - -
- - - - - - - -
"""

test_input1 = """- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
b - - - - - - -
- w - - - - - -
- - - - - - - -
"""

sys.stdin = StringIO(test_input)


def read_input(size):
    matrix = []
    for row in range(size):
        line = input().split()
        matrix.append(line)
    return matrix


def chessboard(size):
    chessboard_matrix = []
    for row in range(size):
        line = []
        for col in range(size):
            line.append(f"{chr(ord('a') + col)}{size - row}")
        chessboard_matrix.append(line)
    return chessboard_matrix


def print_matrix(matrix):
    for r in matrix:
        print(*r, end="\n")


def find_players_position(matrix):
    white_starts_pos = ()
    black_starts_pos = ()
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "b":
                black_starts_pos = row, col
            if matrix[row][col] == "w":
                white_starts_pos = row, col

    return white_starts_pos, black_starts_pos


def possible_moves(row, col, matrix):
    check_for_enemy_white = []
    check_for_enemy_black = []
    white_moves = (row - 1, col)
    black_moves = (row + 1, col)
    check_for_white = [
        (row - 1, col - 1),
        (row - 1, col + 1)
    ]
    check_for_black = [
        (row + 1, col - 1),
        (row + 1, col + 1)
    ]
    for e in check_for_white:
        if 0 <= e[0] < len(matrix) and 0 <= e[1] < len(matrix):
            check_for_enemy_white.append(e)
    for e in check_for_black:
        if 0 <= e[0] < len(matrix) and 0 <= e[1] < len(matrix):
            check_for_enemy_black.append(e)
    return white_moves, black_moves, check_for_enemy_white, check_for_enemy_black


def make_move():
    pass


def playing_chess(white_start, black_start, matrix):
    white_position = white_start
    black_position = black_start
    chess = chessboard(size)

    while True:
        move_turn = 0
        win = False
        if move_turn == 0 or move_turn % 2 == 0:
            current_row = white_position[0]
            current_col = white_position[1]
            check = possible_moves(current_row, current_col, matrix)[2]
            for enemy in check:
                if (enemy[0], enemy[1]) == black_position:
                    print(f"Game over! White win, capture on {chess[black_position[0]][black_position[1]]}.")
                    win = True
                    break
            white_position = possible_moves(current_row, current_col, matrix)[0]
            if white_position[0] == 0:
                print(f"Game over! White pawn is promoted to a queen at {chess[white_position[0]][white_position[1]]}.")
                win = True
            move_turn += 1
        if move_turn != 0 or move_turn % 2 != 0:
            current_row = black_position[0]
            current_col = black_position[1]
            check = possible_moves(current_row, current_col, matrix)[3]
            for enemy in check:
                if (enemy[0], enemy[1]) == white_position:
                    print(f"Game over! Black win, capture on {chess[white_position[0]][white_position[1]]}.")
                    win = True
                    break
            black_position = possible_moves(current_row, current_col, matrix)[1]
            if black_position[0] == size - 1:
                print(f"Game over! Black pawn is promoted to a queen at {chess[black_position[0]][black_position[1]]}.")
                win = True
            move_turn += 1
            if win:
                break
        if win:
            break


size = 8
matrix = read_input(size)
white_start, black_start = find_players_position(matrix)
playing_chess(white_start, black_start, matrix)
