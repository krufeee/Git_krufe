# ----------------2. Diagonals-------------------


size = int(input())
# creating matrix
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])
# finding primary diagonal
primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])

# finding secondary diagonal

for idx in range(size):
    secondary.append(matrix[idx][size - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")

# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# max_sum = float("-inf")
# start_row = 0
# start_col = 0
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + \
#                       matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + \
#                       matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
#         if current_sum > max_sum:
#             max_sum = current_sum
#             start_row = row
#             start_col = col
#
# print(f"Sum = {max_sum}")
# print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]} \n"
#       f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]} \n"
#       f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}")


# def is_outside(r, c, row, col):
#     return r < 0 or c < 0 or r >= row or c >= col
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([x for x in input().split()])
#
# while True:
#     line = input()
#     if line == "END":
#         break
#     line_parts = line.split()
#
#     if len(line_parts) != 5 or line_parts[0] != "swap":
#         print("Invalid input!")
#         continue
#
#     row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]
#
#     if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
#         print("Invalid input!")
#         continue
#
#     matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#     for row in matrix:
#         print(*row, sep=" ")

# rows, cols = [int(x) for x in input().split()]
# word = input()
# matrix = []
# idx = 0
# for row in range(rows):
#     elements = [0] * cols
#     start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
#     for col in range(start, end, step):
#         elements[col] = word[idx % len(word)]
#         idx += 1
#
#     print("".join(elements))


# def get_children(matrix, row, col):
#     possible_children_cords = [
#         [row - 1, col - 1],
#         [row - 1, col],
#         [row - 1, col + 1],
#         [row, col - 1],
#         [row, col + 1],
#         [row + 1, col - 1],
#         [row + 1, col],
#         [row + 1, col + 1]
#     ]
#     result = []
#
#     for child_row, child_col in possible_children_cords:
#         if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) \
#                 and matrix[child_row][child_col] > 0:
#             result.append([child_row, child_col])
#     return result
#
#
# size = int(input())
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# bombs = input().split()
# for bomb in bombs:
#     row, col = [int(x) for x in bomb.split(",")]
#     power = matrix[row][col]
#
#     if power <= 0:
#         continue
#
#     matrix[row][col] = 0
#     children = get_children(matrix, row, col)
#     for child_row, child_col in children:
#         matrix[child_row][child_col] -= power
#
# alive_cells_count = 0
# alive_cells_sum = 0
#
# for row in matrix:
#     for el in row:
#         if el > 0:
#             alive_cells_count += 1
#             alive_cells_sum += el
#
# print(f"Alive cells: {alive_cells_count}")
# print(f"Sum: {alive_cells_sum}")
#
# for el in matrix:
#     print(*el, sep=" ")


# def get_next_pos(row, col, command):
#     if command == "U":
#         return row - 1, col
#     if command == "D":
#         return row + 1, col
#     if command == "L":
#         return row, col - 1
#     if command == "R":
#         return row, col + 1
#
#
# def is_outside(row, col, rows, cols):
#     return row < 0 or col < 0 or row >= rows or col >= cols
#
#
# def get_children(row, col, rows, cols):
#     possible_children = [
#         [row - 1, col],
#         [row, col - 1],
#         [row, col + 1],
#         [row + 1, col]
#     ]
#
#     result = []
#
#     for child_row, child_col in possible_children:
#         if not is_outside(child_row, child_col, rows, cols):
#             result.append([child_row, child_col])
#
#     return result
#
#
# rows, cols = [int(x) for x in input().split()]
# bunnies = set()
# player_row = 0
# player_col = 0
#
# matrix = []
#
# for row in range(rows):
#     row_elements = list(input())
#     for col in range(cols):
#         if row_elements[col] == "P":
#             player_row = row
#             player_col = col
#         elif row_elements[col] == "B":
#             bunnies.add(f"{row} {col}")
#     matrix.append(row_elements)
#
# commands = input()
#
# won = False
# dead = False
#
# for command in commands:
#     next_row, next_col = get_next_pos(player_row, player_col, command)
#     matrix[player_row][player_col] = "."
#     if is_outside(next_row, next_col, rows, cols):
#         won = True
#     elif matrix[next_row][next_col] == "B":
#         dead = True
#         player_row, player_col = next_row, next_col
#     else:
#         matrix[next_row][next_col] = "P"
#         player_row, player_col = next_row, next_col
#     new_bunnies = set()
#     for bunny in bunnies:
#         bunny_row, bunny_col = [int(x) for x in bunny.split()]
#         children = get_children(bunny_row, bunny_col, rows, cols)
#         for child_row, child_col in children:
#             new_bunnies.add(f"{child_row} {child_col}")
#             matrix[child_row][child_col] = "B"
#             if child_row == player_row and child_col == player_col:
#                 dead = True
#
#     bunnies = bunnies.union(new_bunnies)
#
#     if won or dead:
#         break
#
# for row in matrix:
#     print("".join(row))
#
# if won:
#     print(f"won: {player_row} {player_col}")
# else:
#     print(f"dead: {player_row} {player_col}")
