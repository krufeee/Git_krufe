# def data_types(com, dat):
#     if com == 'int':
#         return int(dat) * 2
#     elif com == 'real':
#         return f'{(float(dat) * 1.5):.2f}'
#     elif com == 'string':
#         return f'${dat}$'
#
#
# command = input()
# data = input()
# result = data_types(command, data)
# print(result)
from math import floor

# x1, y1, x2, y2 = input(), input(), input(), input()
#
# cord1 = [x1, y1]
# cord2 = [x2, y2]
# cord1_as_float = list(map(float, cord1))
# cord1_as_int = list(map(int, cord1_as_float))
# cord1_as_abs = list(map(abs, cord1_as_int))
# cord2_as_float = list(map(float, cord2))
# cord2_as_int = list(map(int, cord2_as_float))
# cord2_as_abs = list(map(abs, cord2_as_int))
#
# if sum(cord1_as_abs) > sum(cord2_as_abs):
#     print(f"({cord2_as_int[0]}, {cord2_as_int[1]})")
# else:
#     print(f"({cord1_as_int[0]}, {cord1_as_int[1]})")
#


# def str_flo_to_list_int(x, y):
#     cord = [x, y]
#     cord_as_float = list(map(float, cord))
#     cord_as_int = list(map(int, cord_as_float))
#     cord_as_abs = list(map(abs, cord_as_int))
#     return sum(cord_as_abs)
#
#
# x1, y1, x2, y2, x3, y3, x4, y4 = \
#     input(), input(), input(), input(), input(), input(), input(), input(),
#
# cord1 = [x1, y1]
# cord2 = [x2, y2]
# cord3 = [x3, y3]
# cord4 = [x4, y4]
#
# cord1_as_float = list(map(float, cord1))
# cord1_as_int = list(map(int, cord1_as_float))
# cord1_as_abs = list(map(abs, cord1_as_int))
#
# cord2_as_float = list(map(float, cord2))
# cord2_as_int = list(map(int, cord2_as_float))
# cord2_as_abs = list(map(abs, cord2_as_int))
#
# cord3_as_float = list(map(float, cord3))
# cord3_as_int = list(map(int, cord3_as_float))
# cord3_as_abs = list(map(abs, cord3_as_int))
#
# cord4_as_float = list(map(float, cord4))
# cord4_as_int = list(map(int, cord4_as_float))
# cord4_as_abs = list(map(abs, cord4_as_int))
#
#
# result1 = sum([sum(cord1_as_abs), sum(cord2_as_abs)])
# result2 = sum([sum(cord3_as_abs), sum(cord4_as_abs)])
#
# if result1 >= result2:
#     if sum(cord1_as_abs) > sum(cord2_as_abs):
#         print(f"({cord2_as_int[0]}, {cord2_as_int[1]})({cord1_as_int[0]}, {cord1_as_int[1]})")
#     else:
#         print(f"({cord1_as_int[0]}, {cord1_as_int[1]})({cord2_as_int[0]}, {cord2_as_int[1]})")
#
# else:
#     if sum(cord3_as_abs) > sum(cord4_as_abs):
#         print(f"({cord4_as_int[0]}, {cord4_as_int[1]})({cord3_as_int[0]}, {cord3_as_int[1]})")
#     else:
#         print(f"({cord3_as_int[0]}, {cord3_as_int[1]})({cord4_as_int[0]}, {cord4_as_int[1]})")
#
#
# def str_flo_to_list_int(x, y):
#     list_from_strings = [x, y]
#     lst_from_floats = list(map(float, list_from_strings))
#     list_from_int = list(map(int, lst_from_floats))
#     list_from_abs = list(map(abs, list_from_int))
#     return sum(list_from_abs)
#
#
# def sum_of_lists(x, y, z, v):
#     return sum([str_flo_to_list_int(x, y)]+[str_flo_to_list_int(z, v)])
#
#
# def str_con(x):
#     return int(float(x))
#
#
# x1, y1, x2, y2, x3, y3, x4, y4 = \
#     input(), input(), input(), input(), input(), input(), input(), input()
#
# result1 = sum_of_lists(x1, y1, x2, y2)
# result2 = sum_of_lists(x3, y3, x4, y4)
#
# if result1 < result2:
#     if str_flo_to_list_int(x3, y3) > str_flo_to_list_int(x4, y4):
#         print(f"({str_con(x4)}, {str_con(y4)})({str_con(x3)}, {str_con(y3)})")
#     else:
#         print(f"({str_con(x3)}, {str_con(y3)})({str_con(x4)}, {str_con(y4)})")
# else:
#     if str_flo_to_list_int(x1, y1) > str_flo_to_list_int(x2, y2):
#         print(f"({str_con(x2)}, {str_con(y2)})({str_con(x1)}, {str_con(y1)})")
#     else:
#         print(f"({str_con(x1)}, {str_con(y1)})({str_con(x2)}, {str_con(y2)})")


# def string_from_list(x):
#     string = ' '.join([str(elem) for elem in x])
#     return string
#
#
# def tribonacci_seq(number):
#     result = []
#     for i in range(number):
#         if i < 2:
#             result.append(1)
#         elif i == 2:
#             result.append(2)
#         else:
#             tri_sum = (result[i - 1] + result[i - 2] + result[i - 3])
#             result.append(tri_sum)
#     return result
#
#
# number = int(input())
#
#
# print(string_from_list(tribonacci_seq(number)))


# def mult_result(x, y, z):
#     list_num = [x, y, z]
#     negative_counter = 0
#     for num in list_num:
#         if num < 0:
#             negative_counter += 1
#         elif num == 0:
#             return 'zero'
#         else:
#             continue
#     if negative_counter != 2 and negative_counter != 0:
#         return 'negative'
#     else:
#         return 'positive'
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# print(mult_result(num1, num2, num3))

