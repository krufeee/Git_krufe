import sys
from io import StringIO

test_input = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""

test_input2 = """2, 4
0, 3, 5, 0
1, 0, 4, 0
"""

# sys.stdin = StringIO(test_input)


sys.stdin = StringIO(test_input2)


def square_finder(matrix, row, col):
    res = 0
    nums = [[0, 0], [0, 0]]
    a = matrix[row][col]
    b = matrix[row][col + 1]
    c = matrix[row + 1][col]
    d = matrix[row + 1][col + 1]
    res_sum = (a + b + c + d)
    res_nums = [[a, b], [c, d]]
    if res_sum > res:
        res = res_sum
        nums = res_nums
    return res, nums


## reding and creating matrix

matrix = []
rows, cols = [int(x) for x in input().split(", ")]
for _ in range(rows):
    line = [int(x) for x in input().split(", ")]
    matrix.append(line)

result_sum = 0
result_nums = [[0, 0], [0, 0]]

## main_solution
for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum, current_nums = square_finder(matrix, row, col)
        if current_sum > result_sum:
            result_sum = current_sum
            result_nums = current_nums

## formating print
for s in result_nums:
    print(*s, end="\n")

print(result_sum)
