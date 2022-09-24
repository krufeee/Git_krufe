# sublists = input().split("|")
# result = []
# for idx in range(len(sublists) - 1, - 1, - 1):
#     current_elements = sublists[idx].strip().split()
#     result.extend(current_elements)
#
# print(" ".join(result))

# size = int(input())
# matrix = []
# for _ in range(size):
#     matrix.append([int(x) for x in input().split()])
#
# while True:
#     line = input()
#     if line == "END":
#         break
#     parts = line.split()
#     command = parts[0]
#     row, col, value = [int(x) for x in parts[1:]]
#
#     if row < 0 or col < 0 or row >= size or col >= size:
#         print("Invalid coordinates")
#         continue
#     if command == "Add":
#         matrix[row][col] += value
#     else:
#         matrix[row][col] -= value
#
# for row in matrix:
#     print(*row, sep=" ")


# def find_count(matrix, row, col):
#     mooves = [
#         [row - 2, col - 1],
#         [row - 2, col + 1],
#         [row - 1, col - 2],
#         [row - 1, col + 2],
#         [row + 1, col - 2],
#         [row + 1, col + 2],
#         [row + 2, col - 1],
#         [row + 2, col + 1]
#     ]
#     result = 0
#     for r, c in mooves:
#         if 0 <= r < len(board) and 0 <= c < len(board)  and board[r][c] == "K":
#             result += 1
#     return result
#
#
# size = int(input())
#
# board = []
# removed_knights_counter = 0
# for h in range(size):
#     board.append(list(input()))
#
# while True:
#     best_count = 0
#     knight_row = 0
#     knight_col = 0
#     for row in range(size):
#         for col in range(size):
#             if board[row][col] == "0":
#                 continue
#             count = find_count(board, row, col)
#             if count > best_count:
#                 best_count = count
#                 knight_row = row
#                 knight_col = col
#
#     if best_count == 0:
#         break
#     board[knight_row][knight_col] = "0"
#     removed_knights_counter += 1
#
# print(removed_knights_counter)


# size = int(input())
# matrix = []
#
# bunny_row = 0
# bunny_col = 0
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "B":
#             bunny_row = row
#             bunny_col = col
#     matrix.append(row_elements)
#
# directions = {
#     "right": lambda r, c: (r, c + 1),
#     "left": lambda r, c: (r, c - 1),
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
# }
#
# best_dir = ""
# best_sum = float("-inf")
# best_path = []
#
# for direction in directions:
#     current_sum = 0
#     row, col = directions[direction](bunny_row, bunny_col)
#     current_path = []
#
#     while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
#         current_sum += int(matrix[row][col])
#         current_path.append([row, col])
#         row, col = directions[direction](row, col)
#
#     if current_sum > best_sum and current_path:
#         best_sum = current_sum
#         best_dir = direction
#         best_path = current_path
#
# print(best_dir)
# print(*best_path, sep="\n")
# print(best_sum)


# def get_next_pos(row, col, direction):
#     if direction == "up":
#         return row - 1, col
#     if direction == "down":
#         return row + 1, col
#     if direction == "left":
#         return row, col - 1
#     if direction == "right":
#         return row, col + 1
#
#
# size = int(input())
# matrix = []
# alice_row = 0
# alice_col = 0
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "A":
#             alice_row = row
#             alice_col = col
#     matrix.append(row_elements)
#
# tea_bags = 0
#
# while tea_bags < 10:
#     matrix[alice_row][alice_col] = "*"
#     direction = input()
#     next_row, next_col = get_next_pos(alice_row, alice_col, direction)
#
#     if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
#         break
#     alice_row, alice_col = next_row, next_col
#
#     if matrix[alice_row][alice_col] == "." or matrix[alice_row][alice_col] == "*":
#         continue
#
#     if matrix[alice_row][alice_col] == "R":
#         break
#
#     tea_bags += int(matrix[alice_row][alice_col])
#
# matrix[alice_row][alice_col] = "*"
#
# if tea_bags >= 10:
#     print("She did it! She went to the party.")
# else:
#     print("Alice didn't make it to the tea party.")
#
# for row in matrix:
#     print(*row, sep=" ")


# def get_next_pos(row, col, direction, steps):
#     if direction == "up":
#         return row - steps, col
#     if direction == "down":
#         return row + steps, col
#     if direction == "left":
#         return row, col - steps
#     if direction == "right":
#         return row, col + steps
#
#
# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
# size = 5
#
# player_row = 0
# player_col = 0
# targets = 0
# matrix = []
# hitted_targets = []
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "A":
#             player_row = row
#             player_col = col
#         elif row_elements[col] == "x":
#             targets += 1
#     matrix.append(row_elements)
#
# matrix[player_row][player_col] = "."
# hitted_targets = []
# n = int(input())
#
# for _ in range(n):
#     commands_parts = input().split()
#     command = commands_parts[0]
#     direction = commands_parts[1]
#
#     if command == "move":
#         steps = int(commands_parts[2])
#         next_row, next_col = get_next_pos(player_row, player_col, direction, steps)
#
#         if is_inside(next_row, next_col, size) and matrix[next_row][next_col] == ".":
#             player_row, player_col = next_row, next_col
#     else:
#         bullet_row, bullet_col = get_next_pos(player_row, player_col, direction, 1)
#         while is_inside(bullet_row, bullet_col, size):
#             if matrix[bullet_row][bullet_col] == "x":
#                 targets -= 1
#                 matrix[bullet_row][bullet_col] = "."
#                 hitted_targets.append([bullet_row, bullet_col])
#                 break
#             bullet_row, bullet_col = get_next_pos(bullet_row, bullet_col, direction, 1)
#         if targets == 0:
#             break
#
# if targets == 0:
#     print(f"Training completed! All {len(hitted_targets)} targets hit.")
# else:
#     print(f"Training not completed! {targets} targets left.")
#
# print(*hitted_targets, sep="\n")

#
# def get_next_pos(row, col, direction):
#     if direction == "up":
#         return row - 1, col
#     if direction == "down":
#         return row + 1, col
#     if direction == "left":
#         return row, col - 1
#     if direction == "right":
#         return row, col + 1
#
#
# def is_inside(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# def get_around_kids(matrix, row, col):
#     result = []
#     if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == "X" or \
#             matrix[row][col - 1] == "V":
#         result.append([row, col - 1])
#     if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == "X" or \
#             matrix[row][col + 1] == "V":
#         result.append([row, col + 1])
#     if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == "X" or \
#             matrix[row - 1][col] == "V":
#         result.append([row - 1, col])
#     if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == "X" or \
#             matrix[row + 1][col] == "V":
#         result.append([row + 1, col])
#
#     return result
#
#
# gifts = int(input())
# size = int(input())
# matrix = []
# santa_row = 0
# santa_col = 0
# nice_kids = 0
#
# for row in range(size):
#     row_elements = input().split()
#     for col in range(size):
#         if row_elements[col] == "S":
#             santa_row = row
#             santa_col = col
#         elif row_elements[col] == "V":
#             nice_kids += 1
#     matrix.append(row_elements)
# nice_kids_gifted = 0
# while gifts > 0:
#     line = input()
#     if line == "Christmas morning":
#         break
#
#     matrix[santa_row][santa_col] = "-"
#     santa_row, santa_col = get_next_pos(santa_row, santa_col, line)
#
#     if matrix[santa_row][santa_col] == "V":
#         gifts -= 1
#         nice_kids_gifted += 1
#     elif matrix[santa_row][santa_col] == "C":
#         around_kids = get_around_kids(matrix, santa_row, santa_col)
#         for kid_row, kid_col in around_kids:
#             if matrix[kid_row][kid_col] == "V":
#                 nice_kids_gifted += 1
#             gifts -= 1
#             matrix[kid_row][kid_col] = "-"
#             if gifts == 0:
#                 break
#
#     matrix[santa_row][santa_col] = "S"
#
# if nice_kids_gifted != nice_kids and gifts == 0:
#     print("Santa ran out of presents!")
#
# for row in matrix:
#     print(*row, sep=" ")
#
# if nice_kids_gifted == nice_kids:
#     print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")