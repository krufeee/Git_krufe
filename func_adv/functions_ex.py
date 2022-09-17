# def small_number(a, b, c):
#     return min(a, b, c)
#
#
# num1, num2, num3 = int(input()), int(input()), int(input())
# print(small_number(num1, num2, num3))


# def sum_numbers(a, b):
#     return a + b
#
#
# def subtract(current_sum, c):
#     return current_sum - c
#
#
# a, b, c = int(input()), int(input()), int(input())
# result = subtract(sum_numbers(a, b), c)
# print(result)

# def char_in_range(ch1, ch2):
#     for i in range(ord(ch1) + 1, ord(ch2)):
#         print(chr(i), end=' ')
#
#
# char1 = input()
# char2 = input()
# char_in_range(char1, char2)

# def odd_even_sum(nums):
#     odd_sum = 0
#     even_sum = 0
#     for i in nums:
#         if i % 2 == 0:
#             even_sum += i
#         else:
#             odd_sum += i
#     print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# numbers = map(int, list(input()))
# odd_even_sum(numbers)


# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
# print(result)
#
#
# def check_even(number):
#     if number % 2 == 0:
#         return True
#
#     return False
#
#
# result = filter(check_even, list(map(int, input().split(' '))))
# print(list(result))

# result = sorted(list(map(int, input().split(' '))))
# print(result)


# def sort_func(nums):
#     return sorted(nums)
#
#
# numbers = list(map(int, input().split(' ')))
# print(sort_func(numbers))


# def min_max_sum_func(nums):
#     print(f'The minimum number is {min(nums)}')
#     print(f'The maximum number is {max(nums)}')
#     print(f'The sum number is: {sum(nums)}')
#
#
# numbers = list(map(int, input().split(' ')))
# min_max_sum_func(numb

# def palindrome_func(nums):
#
#     for num in nums:
#         if num == num[::-1]:
#             print('True')
#         else:
#             print('False')
#
#
# numbers = input().split(', ')
# palindrome_func(numbers)


# def loading_bar(num):
#     if num == 100:
#         print('100% Complete!')
#         print('[%%%%%%%%%%]')
#     else:
#         loading_status = f"[{(num // 10) * '%'}{((10 - (num // 10)) * '.')}]"
#         print(f'{num}% {loading_status}')
#         print('Still loading...')
#
#
# number = int(input())
# loading_bar(number)


# def factorial(num):
#     return 1 if num == 0 or num == 1 else num * factorial(num - 1)
#
#
# num1 = int(input())
# num2 = int(input())
#
# result = factorial(num1) / factorial(num2)
# print(f'{result:.2f}')


# def password_validator(password):
#     valid = True
#     for i in password:
#         if i.isalnum():
#             valid = True
#         else:
#             valid = False
#             print("Password must consist only of letters and digits")
#             break
#     digit_counter = 0
#     for j in password:
#         if j.isdigit():
#             digit_counter += 1
#     if digit_counter < 2:
#         valid = False
#         print("Password must have at least 2 digits")
#     if not 6 <= len(password) <= 10:
#         valid = False
#         print("Password must be between 6 and 10 characters")
#     if valid:
#         print('Password is valid')
#
#
# passw = input()
# password_validator(passw)


# def perfect_number(num):
#     result = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             result += i
#     if result / num == 2:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#
#
# number = int(input())
# perfect_number(number)

