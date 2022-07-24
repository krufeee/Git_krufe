# text = input().split(' ')
#
# char_occ = {}
#
# for j in range(len(text)):
#     for i in text[j]:
#         if i not in char_occ:
#             char_occ[i] = 1
#         else:
#             char_occ[i] += 1
#
#
# for ch in char_occ.keys():
#     print(f'{ch} -> {char_occ[ch]}')

# data = input()
# result = {}
# counter = 1
# while data != 'stop':
#     if counter % 2 != 0:
#         resource = data
#         if resource not in result:
#             result[resource] = 0
#     else:
#         quantity = int(data)
#         if resource in result:
#             result[resource] += quantity
#         else:
#             result[resource] = quantity
#     counter += 1
#
#
#     data = input()
#
# for word in result:
#     print(f'{word} -> {result[word]}')


# countries = input().split(', ')
# capitals = input().split(', ')
#
# result = dict(zip(countries, capitals))
#
# for country in result.keys():
#     print(f'{country} -> {result[country]}')

# def print_func(legendary_items_dict, junk_items_dict, special_item):
#     print(f'{special_item} obtained!')
#     print(f"shards: {legendary_items_dict['shards']}")
#     print(f"fragments: {legendary_items_dict['fragments']}")
#     print(f"motes: {legendary_items_dict['motes']}")
#
#     for key, value in junk_items_dict.items():
#         print(f"{key}: {value}")
#
# def legendary_farming():
#     legendary_items_dict = {'shards' : 0, 'fragments' : 0, 'motes' : 0}
#     junk_items_dict = {}
#     while_condition = False
#
#     while True:
#         items = input().lower()
#         items = items.split(' ')
#
#         for value, material in zip(items[0::2], items[1::2]):
#             material = material.lower()
#             value = int(value)
#
#             if material in ['shards', 'fragments', 'motes']:
#                 if material not in legendary_items_dict:
#                     legendary_items_dict[material] = value
#                 else:
#                     legendary_items_dict[material] += value
#
#                 if legendary_items_dict[material] >= 250:
#                     legendary_items_dict[material] -= 250
#                     special_item =''
#                     if material == 'shards':
#                         special_item = 'Shadowmourne'
#                     elif material == 'fragments':
#                         special_item = "Valanyr"
#                     elif material == 'motes':
#                         special_item = "Dragonwrath"
#
#                     print_func(legendary_items_dict, junk_items_dict,special_item)
#                     while_condition = True
#             else:
#                 if material not in junk_items_dict:
#                     junk_items_dict[material] = value
#                 else:
#                     junk_items_dict[material] += value
#
#             if while_condition:
#                 break
#         if while_condition:
#             break
#
# legendary_farming()

# def orders_func(orders_dict, command):
#     product = command[0]
#     price = float(command[1])
#     quantity = int(command[2])
#
#     if product in orders_dict:
#         orders_dict[product] = [price, (quantity + orders_dict[product][1])]
#     else:
#         orders_dict[product] = [price, quantity]
#
#     return orders_dict
#
# def orders():
#
#     orders_dict = {}
#
#     while True:
#         command = input()
#
#         if command == 'buy':
#             break
#
#         command = command.split(' ')
#         orders_dict = orders_func(orders_dict, command)
#
#     for k in orders_dict:
#         total_sum = orders_dict[k][0] * orders_dict[k][1]
#         print(f'{k} -> {total_sum:.2f}')
#
# orders()

# def create_force_side(side, member, user_info_dict):
#     condition = [current_side for current_side in user_info_dict
#                  if member in user_info_dict[current_side]]
#
#     if len(condition) == 0:
#         condition.clear()
#         if side not in user_info_dict:
#             user_info_dict[side] = [member]
#         else:
#             user_info_dict[side].append(member)
#
#     return user_info_dict
#
#
# def create_force_user(member, side, user_info_dict):
#     for current_side in user_info_dict:
#         if member in user_info_dict[current_side]:
#             if len(user_info_dict[current_side]) > 1:
#                 user_info_dict[current_side].pop(member)
#                 break
#             else:
#                 del user_info_dict[current_side]
#                 break
#
#     if side in user_info_dict:
#         user_info_dict[side].append(member)
#     else:
#         user_info_dict[side] = [member]
#     print(f"{member} joins the {side} side!")
#
#
# def force_book():
#     user_info_dict = {}
#
#     while True:
#         command = input()
#         if command == 'Lumpawaroo':
#             break
#
#         if '|' in command:
#             command = command.split(' | ')
#             side = command[0]
#             member = command[1]
#             create_force_side(side, member, user_info_dict)
#
#         elif '->' in command:
#             command = command.split(' -> ')
#             side = command[1]
#             member = command[0]
#             create_force_user(member, side, user_info_dict)
#
#     for data in user_info_dict:
#         print(f"Side: {data}, Members: {len(user_info_dict[data])}")
#         for name in user_info_dict[data]:
#             print(f'! {name}')
#
# force_book()


# def register_car(name, number_plate):
#     if name in softuni_parking.keys():
#         print(f"ERROR: already registered with plate number {softuni_parking[name]}")
#     else:
#         softuni_parking[name] = number_plate
#         print(f"{name} registered {number_plate} successfully")
#
# def unregister_car(name):
#     if name not in softuni_parking.keys():
#         print(f"ERROR: user {name} not found")
#     else:
#         del softuni_parking[name]
#         print(f"{name} unregistered successfully")
#
#
# softuni_parking = {}
#
# number_of_commands = int(input())
#
# for command in range(number_of_commands):
#     current_command = input().split(' ')
#     operation = current_command[0]
#
#     if operation == 'register':
#         register_car(current_command[1], current_command[2])
#
#     elif operation == 'unregister':
#         unregister_car(current_command[1])
#
#
# for user in softuni_parking.keys():
#     print(f"{user} => {softuni_parking[user]}")

# students = {}
#
# while True:
#     data = input()
#
#     if data == "end":
#         break
#     else:
#         command = data.split(" : ")
#         course = command[0]
#         student_name = command[1]
#     if course not in students.keys():
#         students[course] = []
#         students[course].append(student_name)
#     else:
#         students[course].append(student_name)
#
# for key in students.keys():
#     print(f"{key}: {len(students[key])}")
#     for v in students[key]:
#         print(f"-- {v}")

# def filtered_grades():
#     for student in result.keys():
#         average = sum(result[student]) / len(result[student])
#         if average >= 4.50:
#             print(f"{student} -> {average:.2f}")
#         else:
#             continue
#
# number_of_commands = int(input())
#
# result = {}
#
# for command in range(number_of_commands):
#     name = input()
#     grade = float(input())
#     if name not in result.keys():
#         result[name] = []
#         result[name].append(grade)
#     else:
#         result[name].append(grade)
#
#
# filtered_grades()

# companies = {}
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     else:
#         current_command = command.split(" -> ")
#         company_name = current_command[0]
#         employer_id = current_command[1]
#
#     if company_name not in companies:
#         companies[company_name] = []
#         companies[company_name].append(employer_id)
#     else:
#         if employer_id not in companies[company_name]:
#             companies[company_name].append(employer_id)
#
# for company in companies.keys():
#     print(company)
#     for id in companies[company]:
#         print(f"-- {id}")
#

# exam_results = {}
# submissions = {}
#
# while True:
#     command = input()
#     if command == "exam finished":
#         break
#     else:
#         curent_command = command.split("-")
#         student = curent_command[0]
#         if curent_command[1] != "banned":
#             language = curent_command[1]
#             points = int(curent_command[2])
#     if student not in exam_results.keys():
#         exam_results[student] = {}
#         exam_results[student][language] = points
#     else:
#         if language in exam_results[student].keys():
#             if exam_results[student][language] < points:
#                 exam_results[student][language] = points
#
#     if language not in submissions.keys():
#         submissions[language] = 1
#     else:
#         if curent_command[1] != "banned":
#             submissions[language] += 1
#     if curent_command[1] == "banned":
#         exam_results[student] = {}
#
# print("Results:")
# for u in exam_results.keys():
#     for i in exam_results[u]:
#         print(f"{u} | {exam_results[u][i]}")
#
# print("Submissions:")
# for j in submissions.keys():
#     print(f"{j} - {submissions[j]}")
#





