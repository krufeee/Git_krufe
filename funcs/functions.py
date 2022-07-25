# input_list = input().split(' ')
# abs_list = list()
#
# for n in input_list:
#     current_abs = abs(float(n))
#     abs_list.append(current_abs)
#
# print(abs_list)


# def grade_text():
#
#     number = float(input())
#
#     if number < 3:
#         return 'Fail'
#     elif number < 3.50:
#         return 'Poor'
#     elif number < 4.50:
#         return 'Good'
#     elif number < 5.50:
#         return 'Very Good'
#     else:
#         return 'Excellent'
#
#
# print(grade_text())


# def calculator(a, b, operator):
#     if operator == 'multiply':
#         return a * b
#     elif operator == 'divide':
#         return int(a / b)
#     elif operator == 'add':
#         return a + b
#     elif operator == 'subtract':
#         return a - b
#
#
# current_operator = input()
# first_num = int(input())
# second_num = int(input())
#
#
# print(calculator(first_num, second_num, current_operator))

# def repeater(string, count):
#     return string * count


# repeater = lambda string, counter: string * counter
#
# current_string = input()
# current_count = int(input())
#
# print(repeater(current_string, current_count))

# def calc_price(products, quantity):
#     if products == 'coffee':
#         return quantity * 1.5
#     elif products == 'coke':
#         return quantity * 1.4
#     elif products == 'water':
#         return quantity * 1
#     elif products == 'snacks':
#         return quantity * 2
#
#
# current_product = input()
# current_quantity = int(input())
# final_price = (calc_price(current_product, current_quantity))
# print(f'{final_price:.2f}')


# def area(width, height):
#     return width * height
#
#
# curr_width = int(input())
# curr_height = int(input())
#
# print(area(curr_width, curr_height))


# base_list = input().split(' ')
# final_list = list()
#
# for n in base_list:
#     final_n = round(float(n))
#     final_list.append(final_n)
#
# print(final_list)
