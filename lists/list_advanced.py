# vowels = ['a', 'o', 'u', 'e', 'i']
# text = input()
# # no_vowels_text = list()
# #
# # for ch in text:
# #     if ch not in vowels:
# #         no_vowels_text.append(ch)
# #
# # print(''.join(no_vowels_text))
#
#
# no_vowels_list = [ch for ch in text if ch not in vowels]
# print(''.join(no_vowels_list))

# number_of_wagons = int(input())
# train = [0] * number_of_wagons
# command = input()
#
# while command != 'End':
#     explode = command.split(' ')
#     current = explode[0]
#     if current == 'add':
#         num_ppl = int(explode[1])
#         train[-1] += num_ppl
#     if current == 'insert':
#         num_ppl = int(explode[2])
#         position = int(explode[1])
#         train[position] += num_ppl
#     if current == 'leave':
#         num_ppl = int(explode[2])
#         position = int(explode[1])
#         train[position] -= num_ppl
#     command = input()
#
# print(train)


# to_do = ['' for i in range(11)]
# command = input()
#
# while command != 'End':
#     explode = command.split('-')
#     priority = int(explode[0])
#     task = explode[1]
#     to_do[priority] = task
#     command = input()
#
# result = [task for task in to_do if task != '']
# print(result)


# words = input().split(' ')
# palindrome = input()
# palindrome_words = list()
#
# for word in words:
#     rev_list = reversed(word)
#     rev_word = ''.join(rev_list)
#     if rev_word == word:
#         palindrome_words.append(word)
#
# print(palindrome_words)
# palindrome_count = words.count(palindrome)
# print(f'Found palindrome {palindrome_count} times')


# names = input().split(', ')
#
# # sorted_names = sorted(names)
# # sorted_names = sorted(sorted_names, key=lambda name: -len(name))
#
# whole_sorted_names = sorted(names, key=lambda name: (-len(name), name))
#
# # print(sorted_names)
# print(whole_sorted_names)

# numbers = input().split(', ')
# numbers = list(map(int, numbers))
# even_index_numbers = []
# # even_index_numbers =  map(lambda num:)
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_index_numbers.append(i)
#
# print(even_index_numbers)
#

# employees = input().split(' ')
# employees = list(map(int, employees))
# factor = int(input())
# happy_employees = list(filter(
#     lambda emp: emp >= sum(employees) / len(employees),
#     employees))
# if len(happy_employees) >= len(employees) / 2:
#     print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
# else:
#     print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")


# def group_of_tens(nums):
#     current_max = 10
#     max_value_in_list = max(nums)
#     while nums:
#         result = []
#         for i in nums:
#             if 0 < i <= current_max:
#                 result.append(i)
#         if current_max <= max_value_in_list:
#             for i in result:
#                 nums.remove(i)
#             print(f"Group of {current_max}'s: {result}")
#         elif nums:
#             print(f"Group of {current_max}'s: {result}")
#             break
#         current_max += 10
#
#
# string_of_numbers = input().split(', ')
# nums_list = [int(x) for x in string_of_numbers]
# group_of_tens(nums_list)

# import re
#
#
# def separate_digits_from_letters_in_string(x):
#     res = re.findall('(\d+|[A-Za-z]+)', x)
#     result = []
#     for i in range(len(res)):
#         if i == 0 or i % 2 == 0:
#             char = chr(int(res[i]))
#             result.append(char)
#         else:
#             result.append((res[i] + ' '))
#     final = ''.join(x for x in result)
#     return final
#
#
# def swap_letters(x):
#     splitted_str = x.split(' ')
#     splitted_str.pop()
#     final = []
#     for y in splitted_str:
#         i = list(y)
#         i[1], i[-1] = i[-1], i[1]
#         final.append(i)
#     b = ''
#     for i in final:
#         for y in i:
#             b += y
#         b += ' '
#     b = b[:-1]
#     return b
#
#
# message = input()
# a = separate_digits_from_letters_in_string(message)
# print(swap_letters(a))

