# test = list(filter(lambda x: x % 2 == 0, map(int, input().split(' '))))
# print(test)

# i = ['one', 'two', 'three', 'four', 'five', 'six']
# a, b = i.index('two'), i.index('three')
# i[b], i[a] = i[a], i[b]
# print(i)

# substring = input().split(', ')
# sentence = input()
# result = [el for el in substring if el in sentence]
# print(result)

# def next_version(version_number):
#     version_number = int(''.join(version_number)) + 1
#     result = [str(num) for num in str(version_number)]
#     print('.'.join(result))
#
#
# data = input().split('.')
# next_version(data)


# data = input().split(' ')
# result = [word for word in data if len(word) % 2 == 0]
# print('\n'.join(result))

# data = list(map(int, input().split(', ')))
#
# positive = [str(num) for num in data if num >= 0]
# negative = [str(num) for num in data if num < 0]
# even = [str(num) for num in data if num % 2 == 0]
# odd = [str(num) for num in data if num % 2 != 0]
#
# print(f"Positive: {', '.join(positive)}")
# print(f"Negative: {', '.join(negative)}")
# print(f"Even: {', '.join(even)}")
# print(f"Odd: {', '.join(odd)}")

# def office_managment(number_of_rooms):
#     left_chairs = 0
#     condition = True
#
#     for room_number in range(1, number_of_rooms + 1):
#         data = input().split(' ')
#         available_chairs = data[0]
#         visitors = int(data[1])
#
#         diff = abs(len(available_chairs) - visitors)
#
#         if len(available_chairs) < visitors:
#             condition = False
#             print(f'{diff} more chairs needed in room {room_number}')
#         elif len(available_chairs) > visitors:
#             left_chairs += diff
#     if condition:
#         print(f'Game On, {left_chairs} free chairs left')
#
#
# info = int(input())
# office_managment(info)

# def electron_distribution(number):
#     filled_shells = []
#     counter = 1
#     while True:
#         element = 2 * (counter ** 2)
#
#         if element < number:
#             number -= element
#             filled_shells.append(element)
#         else:
#             filled_shells.append(number)
#             break
#         counter += 1
#     print(filled_shells)


# data = int(input())
# electron_distribution(data)


# def representation_data(data, last_position):
#     result = [x for x in data if x == 0]
#     print(f"Cupid's last position was {last_position}.")
#     if len(result) != len(data):
#         diff = len(data) - len(result)
#         print(f"Cupid has failed {diff} places.")
#     else:
#         print("Mission was successful.")
#
#
# def heart_delivery(data):
#     current_index_position = 0
#     cupids_last_position = 0
#
#     while True:
#         command = input().split(' ')
#
#         if command[0] == 'Love!':
#             break
#         index = int(command[1]) + current_index_position
#
#         if index >= len(data):
#             index = 0
#
#         if -1 < index < len(data):
#
#             if data[index] > 0:
#                 data[index] -= 2
#
#                 if data[index] == 0:
#                     print(f"Place {index} has Valentine's day.")
#             else:
#                 print(f"Place {index} already had Valentine's day.")
#
#         cupids_last_position = index
#         current_index_position = index
#
#     representation_data(data, cupids_last_position)
#
#
# nums = list(map(int, input().split('@')))
# heart_delivery(nums)

#
# def collect_func(data, item):
#     if item not in data:
#         data.append(item)
#     return data
#
#
# def drop_func(data, item):
#     if item in data:
#         data.remove(item)
#     return data
#
#
# def combine_items_func(data, items):
#     items = items.split(':')
#     old_element = items[0]
#     new_element = items[1]
#
#     if old_element in data:
#         index_old_element = data.index(old_element)
#         data.insert(index_old_element + 1, new_element)
#     return data
#
#
# def renew_func(data, item):
#     if item in data:
#         data.remove(item)
#         data.append(item)
#     return data
#
#
# def inventory(data):
#
#     while True:
#         command = input().split(' - ')
#
#         if command[0] == 'Craft!':
#             print(', '.join(data))
#             break
#
#         current_command = command[0]
#         items = command[1]
#
#         if current_command == 'Collect':
#             data = collect_func(data, items)
#         elif current_command == 'Drop':
#             data = drop_func(data, items)
#         elif current_command == 'Combine Items':
#             data = combine_items_func(data, items)
#         elif current_command == 'Renew':
#             data = renew_func(data, items)
#
#
# info = input().split(', ')
# inventory(info)
