# # fruits = ['apple', 'banana', 'cherry', 'apple']
# # index = (i for i, value in enumerate(fruits) if value == 'apple')
# # print(list(index))
#
#
# # nums = input().split(' ')
# # new_list = []
# # for num in nums:
# #     if int(num) > 0:
# #         new_list.append(-int(num))
# #     else:
# #         new_list.append(abs(int(num)))
# # print(new_list)
#
# # list_comprehension
# # nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(' ')))]
# # print(nums)
#
#
# # num1 = int(input())
# # num2 = int(input())
# # new_list = []
# # for num in range(1, num2 + 1):
# #     new_list.append(num * num1)
# #
# # print(new_list)
#
# info = input().split(' ')
# team_a_player = 11
# team_b_player = 11
# player_loses = []
# condition = False
# for card in info:
#     if card not in player_loses:
#         player_loses.append(card)
#         if 'A' in card:
#             team_a_player -= 1
#         else:
#             team_b_player -= 1
#         if team_b_player < 7 or team_a_player < 7:
#             condition = True
#             break
#
# print(f'Team A - {team_a_player}; Team - {team_b_player}')
# if condition:
#     print('Game was terminated')

# num = input().split(' ')
# copy_num = list(map(int, num))
# count = int(input())
# for _ in range(count):
#     current_min_element = min(copy_num)
#     num.remove(str(current_min_element))
#     copy_num.remove(current_min_element)
# print(', '.join(num))

# fire_cells = input().split('#')
# water_amount = int(input())
# effort = 0
# total_fire = 0
# condition = False
# print('Cells:')
# for current_fire in fire_cells:
#     fire_info = current_fire.split(' = ')
#     type_of_fyre = fire_info[0]
#     value_of_fire = int(fire_info[1])
#     condition = False
#     if type_of_fyre == 'High':
#         if 81 <= value_of_fire <= 125:
#             condition = True
#     if type_of_fyre == 'Medium':
#         if 51 <= value_of_fire <= 80:
#             condition = True
#     if type_of_fyre == 'Low':
#         if 1 <= value_of_fire <= 50:
#             condition = True
#     if condition:
#         if water_amount >= value_of_fire:
#             water_amount -= value_of_fire
#             effort += value_of_fire * 0.25
#             total_fire += value_of_fire
#             print(f' - {value_of_fire}')
#
# print(f'Effort: {effort:.2f}')
# print(f'Total Fire: {total_fire}')

# items = input().split('|')
# budget = int(input())
# profit = 0
# new_item_prices = []
# data_prices = []
# condition = False
# for item in items:
#     current_item_info = item.split('->')
#     type_of_product = current_item_info[0]
#     price = float(current_item_info[1])
#     condition = False
#
#     if type_of_product == 'Clothes':
#         if price <= 50:
#             condition = True
#     elif type_of_product == 'Shoes':
#         if price <= 35:
#             condition = True
#     elif type_of_product == 'Accessories':
#         if price <= 20.50:
#             condition = True
#
#     if condition:
#         if budget >= price:
#             budget -= price
#             profit += price * 0.40
#             new_prices = price + price * 0.40
#             new_item_prices.append(new_prices)
#             data_prices.append(f'{new_prices:.2f}')
#
# print(' '.join(data_prices))
# print(f'Profit: {profit:.2f}')
#
# total_sum = budget + sum(new_item_prices)
# if total_sum >= 150:
#     print('Hello, France!')
# else:
#     print('Not enough money.')

# events = input().split('|')
# energy = 100
# coins = 100
# close_condition = False
# for event in events:
#     current_event_elements = event.split('-')
#     command = current_event_elements[0]
#     number = int(current_event_elements[1])
#
#     if command == 'rest':
#         if energy >= 100:
#             energy = 100
#             print(f'You gained 0 energy.')
#         else:
#             energy += number
#             print(f'You gained {number} energy.')
#
#         print(f'Current energy: {energy}.')
#
#     elif command == 'order':
#         if energy >= 30:
#             print(f'You earned {number} coins.')
#             energy -= 30
#             coins += number
#         else:
#             energy += 50
#             print(f'You had to rest!')
#
#     else:
#         if coins >= number:
#             print(f'You bought {command}.')
#             coins -= number
#         else:
#             print(f'Closed! Cannot afford {command}.')
#             close_condition = True
#             break
# if not close_condition:
#     print('Day completed!')
#     print(f'Coins: {coins}')
#     print(f'Energy: {energy}')

# numbers = input().split(', ')
# beggars = int(int(input()))
# numbers_copy = numbers.copy()
# temporary_data = []
# beggars_data = []
# for beggar in range(beggars):
#     temporary_data.append(numbers_copy[beggar])
#     temporary_data.append(numbers_copy[beggar + 1])
#     print(temporary_data)

# numbers_list = [int(x) for x in input().split(", ")]
# number_of_beggars = int(input())
#
# beggars_list = [0] * number_of_beggars
#
# for num in range(len(beggars_list)):
#     current_beggar = num
#     for n in range(len(numbers_list)):
#         current_num = n % number_of_beggars
#         if current_num == current_beggar:
#             if beggars_list[num] == 0:
#                 if numbers_list[n] == 0:
#                     beggars_list[current_num] = 0
#                     break
#                 beggars_list[current_num] = numbers_list[n]
#             else:
#                 beggars_list[current_num] += numbers_list[n]
#
# print(beggars_list)


# money = input().split(', ')
# beggars = int(input())
# result_list = [0] * beggars
# beggars_turn = 0
# for coin in money:
#     result_list[beggars_turn] += int(coin)
#     beggars_turn += 1
#     if beggars_turn == beggars:
#         beggars_turn = 0
# print(result_list)

# cards = input().split(' ')
# shuffles = int(input())
# first_card = cards[0]
# last_card = cards[-1]
# first_half = []
# second_half = []
# result = []
# for card in range(1, int(len(cards) / 2)):
#     first_half.append(cards[card])
# for card in range(int(len(cards) / 2), len(cards) - 1):
#     second_half.append(cards[card])
# for i in range(len(first_half)):
#     for s in range(shuffles):


# ---------------------------------------------------
# string = input()
# shuffles = int(input())
# string_list = string.split()
# shuffled_list = []
# length = int(len(string_list) / 2)
#
# for n in range(shuffles):
#     first_half = string_list[:length]
#     second_half = string_list[length:]
#     for item in range(len(first_half)):
#         shuffled_list.append(first_half[item])
#         shuffled_list.append(second_half[item])
#     string_list = shuffled_list
#     shuffled_list = []
#
# print(string_list)

# starting_string = input()
# shuffles = int(input())
#
# first_char = starting_string[0]
# last_char = starting_string[-1]
#
# starting_list = starting_string.split(" ")
#
# changeable_list = starting_list
# first_list = []
# second_list = []
#
# half = int(len(starting_list) / 2)
#
# for n in range(shuffles):
#     first_list = changeable_list[1:half]
#     second_list = changeable_list[half:-1]
#     changeable_list = []
#     for num in range(len(second_list)):
#         if num == 0:
#             changeable_list.append(starting_list[0])
#         changeable_list.append(second_list[num])
#         changeable_list.append(first_list[num])
#         if num == (len(second_list) - 1):
#             changeable_list.append(starting_list[-1])
#
# print(changeable_list)


# gifts = input().split(' ')
# command = input()
# working_list = gifts.copy()
# result = ''
# while command != 'No Money':
#     current_command = command
#     current_command = current_command.split(' ')
#     current_value = current_command[0]
#     current_gift = current_command[1]
#
#     if current_value == 'OutOfStock':
#         if current_gift in working_list:
#             for index, item in enumerate(working_list):
#                 if item == current_gift:
#                     working_list[index] = 'None'
#     elif current_value == 'Required':
#         current_index = int(current_command[2])
#         if len(working_list) - 1 >= current_index >= 0:
#             working_list[current_index] = current_gift
#     elif current_value == 'JustInCase':
#         working_list[-1] = current_gift
#     command = input()
#
# for index, item in enumerate(working_list):
#     if item == 'None':
#         working_list.pop(index)
#
# for i in working_list:
#     result += f'{i} '
# result = result[:-1]
# print(result)