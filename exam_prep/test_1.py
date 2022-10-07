# string_1 = "asdadddaadd"
#
# a = string_1.count("a")
# print(a)


# deposit_found = ["W", "M", "C"]
# deposit_found.remove("W")
# print(deposit_found)

# list_1 = [(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy')]
#
# # print(sum(x.count(3) for x in list_1))
#
#
# list_1.pop(1)
# print(list_1)


# def next_move(current_row, current_col, direction,
#               row, column):
#     directions = {
#         "up": (current_row - 1, current_col),
#         "down": (current_row + 1, current_col),
#         "left": (current_row, current_col - 1),
#         "right": (current_row, current_col + 1),
#     }
#     next_row, next_col = directions[direction]
#     if 0 <= next_row < row and 0 <= next_col < column:
#         return next_row, next_col
#     else:
#         if next_row < 0:
#             return next_row + row, next_col
#         elif next_row >= row:
#             return next_row - row, next_col
#         elif next_col < 0:
#             return next_row, next_col + column
#         else:
#             return next_row, next_col - column
#
#
# matrix = [
#     ['.' '.' '.' '.' '.'],
#     ['C' '.' '.' 'G' '.'],
#     ['.' 'C' '.' '.' '.'],
#     ['G' '.' '.' 'C' '.'],
#     ['.' 'D' '.' '.' 'D'],
#     ['Y' '.' '.' '.' 'G'],
# ]
#
# rows = 6
# cols = 5
#
# print(next_move(0, 3, "down", rows, cols))

#
# a = 5
#
# while True:
#     if a == 9:
#         break
#     a += 1
#     print(a)


# ll = ["-3", "5", "0", "444", "a"]
#
# for ch in ll:
#     if ch.isalpha():
#         print(ch)
#     else:
#         print(f"fuck {ch}")


# ll = [0, 1, 2, 3, 4, 5, 6]
# ll.append(443)
# print(ll)