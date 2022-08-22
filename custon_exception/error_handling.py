# numbers_list = input().split(", ")
#
# result = 1
# for i in range(len(numbers_list)):
#     number = int(numbers_list[i])
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(int(result))


# class ValueTooSmallException(Exception):
#     pass
#
#
# value = int(input())
#
# if value < 10:
#     raise ValueTooSmallException(
#         f"{value} should be equal or greater than 10")
# import random
#
#
# def raise_exception():
#     chance = 0.7
#     if random.random() < chance:
#         raise ValueError("Invalid value")
#
#
# for _ in range(100):
#     try:
#         raise_exception()
#         print("No exception")
#     except ValueError:
#         print("Value error handled")
# import sys
# from io import StringIO
#
# # test_input1 = """Hello
# # Bye
# # """
#
# test_input2 = """Hello
# 2
# """
#
# sys.stdin = StringIO(test_input2)
#
# text = input()
# try:
#     times = int(input())
#     print(text * times)
# except ValueError:
#     print("Variable times must be an integer")