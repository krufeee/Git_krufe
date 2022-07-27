# tail = input()
# body = input()
# head = input()
# meercat = [head, body, tail]
# print(meercat)
# # meercat[0], meercat[2] = meercat[2], meercat[0] for swap elements

# number = int(input())
# empty_list = []
# for i in range(number):
#     command = input()       # empty_list.append(input())
#     empty_list.append(command)
# print(empty_list)

# number = int(input())
#
# negatives = list()
# positives = list()
# sum_of_negatives = 0
# for i in range(number):
#     current = int(input())
#     if current >= 0:
#         positives.append(current)
#     else:
#         negatives.append(current)
#         sum_of_negatives += current
# print(positives)
# print(negatives)
# print(f"Count of positives: {len(positives)}")
# print(f"Sum of negatives: {sum_of_negatives}"

# number = int(input())
# search_word = input()
# string = list()
# filtered = list()
# for i in range(number):
#     current_string = input()
#     string.append(current_string)
#     if search_word in current_string:
#         filtered.append(current_string)
# print(string)
# print(filtered)

# number = int(input())
# numbers_list = list()
# for i in range(number):
#     current = int(input())
#     numbers_list.append(current)
# filter_word = input()
# filtered = list()
# for current_number in numbers_list:
#     if filter_word == "even":
#         if current_number % 2 == 0:
#             filtered.append(current_number)
#     if filter_word == "odd":
#         if current_number % 2 != 0:
#             filtered.append(current_number)
#     if filter_word == "positive":
#         if current_number >= 0:
#             filtered.append(current_number)
#     if filter_word == "negative":
#         if current_number < 0:
#             filtered.append(current_number)
#
# print(filtered)
