# n = 5
# m = 7
#
# mm = []
# for j in range(n):
#     ll = []
#     for i in range(m):
#         ll.append(i * j)
#     mm.append(ll)
#
# print(*mm, sep="\n")

# n, m = [int(x) for x in input().split(", ")]
# matrix = []
# matrix_sum = 0
# for _ in range(n):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#     matrix_sum += sum(row)
#
# print(matrix_sum)
# print(matrix)

#
# mm = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
#
# print(mm)
#
# print(
#     [[v + 1 for v in row] for row in mm]
# )
#
# print(
#     [
#         v + 1
#         for row in mm       # flattering
#         for v in row
#     ]
# )

# n = int(input())
#
# result = []
#
# for _ in range(n):
#     row = [int(x) for x in input().split(", ")]
#     result.append(
#         [x for x in row if x % 2 == 0]
#     )
# print(result)

# n = int(input())
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
# print([[x for x in row if x % 2 == 0] for row in matrix])

# flattering

# n = int(input())
# mm = [[int(x) for x in input().split(", ")] for _ in range(n)]
# print(
#     [
#         v for row in mm for v in row
#     ]
# )

# matrix = [
#     [1, 2, 3, 4],
#     [2, 3, 4, 5],
#     [3, 4, 5, 6]
# ]
#
#
# def is_even(number):
#     return number % 2 == 0
#
#
# def remove_odd(ll):
#     return [x for x in ll if is_even(x)]
#
#
# print(
#     [remove_odd(row) for row in matrix]
# )

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15]
# ]
#
#
# def matrix_sum(mm):
#     result = 0
#     n = len(mm)
#     m = len(mm[0])
#     for row_index in range(n):
#         for column_index in range(m):
#             result += int(mm[row_index][column_index])
#     return result
#
#
# print(matrix_sum(matrix))


# rows_count, columns_count = [int(x) for x in input().split(", ")]
#
#
# matrix = []
#
# for _ in range(rows_count):
#     matrix.append(
#         [int(x) for x in input().split(" ")]
#     )
#
# column_sums = [0] * columns_count
# for row_index in range(rows_count):
#     for column_index in range(columns_count):
#         column_sums[column_index] += matrix[row_index][column_index]
#
# print(*column_sums, sep="\n")

#
# def get_primary_diagonal(matrix):
#     the_sum = 0
#     n = len(matrix)
#     # for r in range(n):
#     #     for c in range(n):
#     #         if r == c:
#     #             the_sum += matrix[r][c]
#     for i in range(n):
#         the_sum += matrix[i][i]
#         # return sum(matrix[i][i] for i in range(n))
#     return the_sum
#
#
# def get_secondary_diagonal(matrix):
#     n = len(matrix)
#     return sum(matrix[i][n - i - 1] for i in range(n))
#
#
# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append(
#         [int(x) for x in input().split(" ")]
#     )
#
# print(get_primary_diagonal(matrix))

import sys
from io import StringIO

test_input = """3
ABC
DEF
X!@
!
"""

test_input2 = """4
asdd
xczc
qwee
qefw
4
"""

sys.stdin = StringIO(test_input)
# sys.stdin = StringIO(test_input2)


# def find_symbol(matrix, symbol):
#     for row_index in range(n):
#         for column_index in range(n):
#             if matrix[row_index][column_index] == symbol:
#                 return row_index, column_index
#     return None
#
#
# n = int(input())
# matrix = [input() for _ in range(n)]
# symbol = input()
# result = find_symbol(matrix, symbol)
# if result:
#     row_index, column_index = result
#     print(f"({row_index}, {column_index})")
# else:
#     print(f"{symbol} does not occur in the matrix")


# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append(input().split())
#
# squares = 0
#
# for row in range(rows - 1):
#     for col in range(cols - 1):
#         if matrix[row][col] == matrix[row][col + 1] == \
#                 matrix[row + 1][col] == matrix[row + 1][col + 1]:
#             squares += 1
#
# print(squares)

