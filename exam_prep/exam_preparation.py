# line = input()
# net_price = 0
#
# while line != 'special' and line != 'regular':
#     current_price = float(line)
#     if current_price > 0:
#         net_price += current_price
#     else:
#         print("Invalid price!")
#
#     line = input()
#
# if net_price <= 0:
#     print("Invalid order!")
# else:
#     taxes = net_price * 0.2
#     final_price = net_price + taxes
#     print("Congratulations you've just bought a new computer!")
#     print(f'Price without taxes: {net_price:.2f}$')
#     print(f'Taxes: {taxes:.2f}$')
#     print('-----------')
#     if line == 'special':
#         final_price = final_price * 0.9
#
#     print(f"Total price: {final_price:.2f}$")


# numbers = input().split(' ')
# numbers = list(map(int, numbers))
# line = input()
#
# while line != 'end':
#     if line == 'decrease':
#         numbers = list(map(lambda n: n-1, numbers))
#     else:
#         explode = line.split(' ')
#         command = explode[0]
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#
#         if command == 'swap':
#             numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
#
#         elif command == 'multiply':
#             numbers[index1] = numbers[index1] * numbers[index2]
#
#     line = input()
# numbers = list(map(str, numbers))
# result = ', '.join(numbers)
# print(result)


# targets = input().split(' ')
# targets = list(map(int, targets))
#
# line = input()
#
# while line != 'End':
#     command_list = line.split(' ')
#     command = command_list[0]
#     index = int(command_list[1])
#     value = int(command_list[2])
#
#     if command == 'Shoot' and 0 <= index < len(targets):
#         current_target = targets[index]
#         current_target -= value
#         if current_target <= 0:
#             targets.pop(index)
#         else:
#             targets[index] = current_target
#
#     elif command == 'Add':
#         if 0 <= index < len(targets):
#             targets.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     elif command == 'Strike':
#         if index - value >= 0 and index + value < len(targets):
#             targets = targets[:index - value] + targets[index + value + 1:]
#         else:
#             print('Strike missed!')
#
#     line = input()
#
# targets = list(map(str, targets))
# result = '|'.join(targets)
# print(result)
#

