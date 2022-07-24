# import string
#
#
# def valid_username(data):
#     flag = 0
#     expected_elements = string.digits + string.ascii_letters + '_' + '-'
#     for name in data:
#         flag = 0
#         if len(name) < 3 or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_elements]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)
#
#
# d = input().split(', ')
# valid_username(d)


# def sum_func(first_word, second_word):
#     total_sum = 0
#     for i in range(len(first_word)):
#         if i < len(second_word):
#             total_sum += ord(first_word[i]) * ord(second_word[i])
#         else:
#             total_sum += ord(first_word[i])
#     return total_sum
#
#
# def char_multiplier(first_word, second_word):
#     result = 0
#     if len(first_word) > len(second_word):
#         result = sum_func(first_word, second_word)
#     else:
#         result = sum_func(second_word, first_word)
#     print(result)
#
#
# data = input().split(' ')
#
# char_multiplier(data[0], data[1])

# def extract_file(data):
#     needed_information = data[-1]
#     needed_information = needed_information.split('.')
#     file_name = needed_information[0]
#     extension = needed_information[1]
#     print(f'File name: {file_name}')
#     print(f'File extension: {extension}')
#
#
# d = input().split('\\')
# extract_file(d)


# def caesar_cipher(text):
#     result = [chr(ord(ch) + 3) for ch in text]
#     print(''.join(result))
#
#
# text = input()
# caesar_cipher(text)

# def emoticon_finder(data):
#     result = [text[i] + text[i+1] for i in range(len(text))
#               if text[i] == ':' and text[i+1] != ' ']
#     print('\n'.join(result))
#
#
# text = input()
# emoticon_finder(text)
# import string
#
#
# def extract_func(text):
#     current_num = [num for num in text if num.isdigit()]
#     result = 0
#
#     for i in range(len(text)):
#         if text[i].isalpha():
#             index = string.ascii_lowercase.index(text[i].lower()) + 1
#
#             if i == 0:
#                 if text[i] == text[i].lower():
#                     result = int(''.join(current_num)) * index
#                 else:
#                     result = int(''.join(current_num)) / index
#             else:
#                 if text[i] == text[i].lower():
#                     result += index
#                 else:
#                     result -= index
#     return result
#
#
# def letters_change_numbers(data):
#     result = 0
#
#     for num in data:
#         result += extract_func(num)
#
#     print(f'{result:.2f}')
#
#
# data = input().split()
# letters_change_numbers(data)


# def additional_func(partition):
#     current_max_num = 0
#     special_char = ''
#     for ch in partition:
#         if ch != special_char:
#             if current_max_num >= 6:
#                 break
#             current_max_num = 1
#             special_char = ch
#         else:
#             current_max_num += 1
#     return[current_max_num, special_char]
#
#
# def ticket_validator(ticket):
#     ticket_condition = ''
#
#     if len(ticket) != 20:
#         ticket_condition = "invalid ticket"
#     elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
#         ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
#     else:
#         data_source = ''
#         if additional_func(ticket[0:int(len(ticket) / 2)]) \
#                 > additional_func(ticket[int(len(ticket) / 2):]):
#             data_source = additional_func(ticket[int(len(ticket) / 2):])
#         else:
#             data_source = additional_func(ticket[0: int(len(ticket) / 2)])
#         number_of_special_signs = data_source[0]
#         special_sign = data_source[1]
#         if number_of_special_signs < 6 or special_sign not in '@#$^':
#             ticket_condition = f'ticket "{ticket}" - no match'
#         else:
#             ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'
#
#     return ticket_condition
#
#
# def winning_ticket(data):
#
#     for ticket in data:
#         print(ticket_validator(ticket))
#
#
# ticket_info = input()
# data = [x.strip() for x in ticket_info.split(', ')]
# winning_ticket(data)


# text = input()
# result = ""
# for ch in range(len(text)):
#     if ch == 0:
#         result += text[ch]
#     else:
#         if text[ch] != text[ch - 1]:
#             result += text[ch]
# print(result)

# def string_explosion(text):
#     result = ''
#     power = 0
#     for ch in range(len(data)):
#         if data[ch].isalpha() and power == 0:
#             result += data[ch]
#         elif data[ch] == '>':
#             result += data[ch]
#             power += int(data[ch + 1])
#         else:
#             power -= 1
#     print(result)
#
#
# data = input()
#
# string_explosion(data)

# import re
#
# message = input()
# result = ''
# counter = 0
# data = ''
#
# message = re.split('(\d+)', message)
# message = message[:-1]
#
# for i in range(1, len(message) + 1):
#     if i % 2 != 0:
#         data += data.join(message[i - 1])
#     else:
#         result += data * int(message[i - 1])
#         data = ''
#
# uniq = set(x for x in result.upper())
#
# print(f'Unique symbols used: {len(uniq)}')
# print(result.upper())


