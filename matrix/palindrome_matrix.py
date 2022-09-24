import sys
from io import StringIO

test_input = """4 6"""
sys.stdin = StringIO(test_input)

rows, cols = [int(x) for x in input().split(" ")]

matrix = []
for row in range(rows):
    line = []
    for col in range(cols):
        line.append((chr(ord("a") + row)) + (chr(ord("a") + col + row)) + (chr(ord("a") + row)))
    matrix.append(line)

for el in matrix:
    print(*el, sep=" ")
