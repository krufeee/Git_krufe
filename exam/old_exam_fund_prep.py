# # AD ASTRA
# import re
#
# data = input()
# pattern = r"([#\|])([\ a-zA-Z]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
# calories = 0
# result = re.finditer(pattern, data)
# food_container = dict()
#
# for match in result:
#     calories += int(match.group(4))
#     food_container[match.group(2)] = {}
#     food_container[match.group(2)]['ED'] = match.group(3)
#     food_container[match.group(2)]['Kcal'] = match.group(4)
#
# food_left = int(calories / 2000)
#
# print(f"You have food to last you for: {food_left} days!")
#
# for food in food_container:
#     print(f"Item: {food}, Best before: {food_container[food]['ED']},"
#           f" Nutrition: {food_container[food]['Kcal']}")
#

# The Pianist

# number_of_pieces = int(input())
# pieces_dict = dict()
#
# for piece in range(number_of_pieces):
#     current_info = input().split("|")
#     current_piece = current_info[0]
#     current_composer = current_info[1]
#     current_key = current_info[2]
#     pieces_dict[current_piece] = dict()
#     pieces_dict[current_piece]["composer"] = current_composer
#     pieces_dict[current_piece]["key"] = current_key
#
# command = input()
#
# while command != "Stop":
#     current_command = command.split("|")
#     action = current_command[0]
#     current_piece = current_command[1]
#     if action == "Add":
#         current_composer = current_command[2]
#         current_key = current_command[3]
#         if current_piece not in pieces_dict:
#             pieces_dict[current_piece] = dict()
#             pieces_dict[current_piece]["composer"] = current_composer
#             pieces_dict[current_piece]["key"] = current_key
#             print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
#         else:
#             print(f"{current_piece} is already in the collection!")
#     if action == "Remove":
#         if current_piece in pieces_dict:
#             pieces_dict.pop(current_piece)
#             print(f"Successfully removed {current_piece}!")
#         else:
#             print(f"Invalid operation! {current_piece} does not exist in the collection.")
#     if action == "ChangeKey":
#         current_key = current_command[2]
#         if current_piece in pieces_dict:
#             pieces_dict[current_piece]["key"] = current_key
#             print(f"Changed the key of {current_piece} to {current_key}!")
#         else:
#             print(f"Invalid operation! {current_piece} does not exist in the collection.")
#
#     command = input()
#
# for piece in pieces_dict:
#     print(f"{piece} -> Composer: {pieces_dict[piece]['composer']}, Key: {pieces_dict[piece]['key']}")

# World Tour


# destinations = input()
# command = input()
#
# while command != "Travel":
#     current_command = command.split(":")
#     action = str(current_command[0])
#     if action == "Add Stop":
#         index = int(current_command[1])
#         string = str(current_command[2])
#         if 0 <= index < len(destinations):
#             destinations = destinations[:index] + string + destinations[index:]
#     if action == "Remove Stop":
#         start_index = int(current_command[1])
#         stop_index = int(current_command[2])
#         if start_index >= 0 and stop_index < len(destinations):
#             destinations = destinations[:start_index] + destinations[stop_index+1:]
#     if action == "Switch":
#         old_string = str(current_command[1])
#         new_string = str(current_command[2])
#         if old_string in destinations:
#             while old_string in destinations:
#                 destinations = destinations.replace(old_string, new_string)
#                 if old_string not in destinations:
#                     break
#     print(destinations)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {destinations}")


# Plant Discovery

number_of_plants = int(input())
garden = {}
for _ in range(number_of_plants):
    current_info = input().split("<->")
    plant = current_info[0]
    rarity = current_info[1]
    if plant not in garden:
        garden[plant] = {}
        garden[plant]['rarity'] = rarity
    else:
        garden[plant]['rarity'] = rarity

command = input()

while command != "Exhibition":
    current_command = command.split(":")
    action = current_command[0]
    if action == "Rate":
        current_info = current_command[1].split(" - ")
        plant = current_info[0]
        rating = current_info[1]
        if plant in garden.keys():
            garden[plant]["rating"] = list()
            garden[plant]["rating"].append(rating)
        else:
            print("error")
    elif action == "Update":
        current_info = current_command[1].split(" - ")
        plant = current_info[0]
        rarity = current_info[1]
        garden[plant]["rarity"] = {}
        garden[plant]["rarity"] = rarity
    elif action == "Reset":
        current_info = current_command[1].split(" - ")
        plant = current_info[0]
        garden[plant]["rating"] = list()

    command = input()

print(garden)
