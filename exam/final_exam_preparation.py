# message = input()
# command = input()
#
# while command != 'Decode':
#     currennt_command = command.split('|')
#     if currennt_command[0] == 'Move':
#         number = int(currennt_command[1])
#         message = message[number:] + message[:number]
#
#     elif currennt_command[0] == 'Insert':
#         index = int(currennt_command[1])
#         value = currennt_command[2]
#         message = message[:index] + value + message[index:]
#
#     elif currennt_command[0] == 'ChangeAll':
#         substring = currennt_command[1]
#         replacement = currennt_command[2]
#         message = message.replace(substring, replacement)
#
#
#     command = input()
#
# print(f"The decrypted message is: {message}")

# import re
# text = input()
# regex = r"([=|/])([A-Z][a-zA-Z]{2,})\1"
#
# matches = re.finditer(regex, text)
# locations = []
# points = 0
# for match in matches:
#     city = match.group(2)
#     locations.append(city)
#     points += len(city)
#
# print("Destinations: " + ", ".join(locations))
# print(f"Travel Points: {points}")

# number_of_heroes = int(input())
# heroes = {}
# for hero in range(number_of_heroes):
#     current_hero = input().split(' ')
#     hero_name = current_hero[0]
#     hero_HP = int(current_hero[1])
#     hero_MP = int(current_hero[2])
#
#     current_hero_dict = {}
#     current_hero_dict["HP"] = hero_HP
#     current_hero_dict["MP"] = hero_MP
#     heroes[hero_name] = current_hero_dict
#
#     # heroes[hero_name]["HP"] = hero_HP
#     # heroes[hero_name]["MP"] = hero_MP
#
# command = input()
# while command != "End":
#     current_command = command.split(" - ")
#     action = current_command[0]
#     hero_name = current_command[1]
#     value = int(current_command[2])
#
#     if action == "CastSpell":
#         spell_name = current_command[3]
#         if heroes[hero_name]["MP"] >= value:
#             heroes[hero_name]["MP"] -= value
#             print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
#         else:
#             print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#     elif action == "TakeDamage":
#         attacker = current_command[3]
#         heroes[hero_name]["HP"] -= value
#         if heroes[hero_name]["HP"] > 0:
#             print(f'{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]["HP"]} HP left!')
#         else:
#             heroes.pop(hero_name)
#             print(f"{hero_name} has been killed by {attacker}!")
#     elif action == "Recharge":
#         if value + heroes[hero_name]["MP"] > 200:
#             value = 200 - heroes[hero_name]["MP"]
#             heroes[hero_name]["MP"] = 200
#         else:
#             heroes[hero_name]["MP"] += value
#         print(f"{hero_name} recharged for {value} MP!")
#     elif action == "Heal":
#         if value + heroes[hero_name]["HP"] > 100:
#             value = 100 - heroes[hero_name]["HP"]
#             heroes[hero_name]["HP"] = 100
#         else:
#             heroes[hero_name]["HP"] += value
#         print(f"{hero_name} healed for {value} HP!")
#
#     command = input()
#
# for h in heroes:
#     print(f"{h}")
#     print(f"  HP: {heroes[h]['HP']}")
#     print(f"  MP: {heroes[h]['MP']}")


# def plunder(c_town, c_people, c_gold, list_of_towns):
#     list_of_towns[c_town]["population"] -= c_people
#     list_of_towns[c_town]["gold"] -= c_gold
#     print(f"{c_town} plundered! {c_gold} gold stolen, {c_people} citizens killed.")
#     if list_of_towns[c_town]["population"] <= 0 or list_of_towns[c_town]["gold"] <= 0:
#         print(f"{c_town} has been wiped off the map!")
#         list_of_towns.pop(c_town)
#
#
# def prosper(c_town, c_gold, list_of_towns):
#     list_of_towns[c_town]["gold"] += c_gold
#     print(f"{c_gold} gold added to the city treasury. {c_town} now has {list_of_towns[c_town]['gold']} gold.")
#
#
# cities = {}
# data = input()
#
# while data != "Sail":
#     current_info = data.split("||")
#     city = current_info[0]
#     population = int(current_info[1])
#     gold = int(current_info[2])
#     if city not in cities.keys():
#         cities[city] = {}
#         cities[city]["population"] = population
#         cities[city]["gold"] = gold
#     else:
#         cities[city]["population"] += population
#         cities[city]["gold"] += gold
#
#     data = input()
#
# command = input()
#
# while command != "End":
#     current_command = command.split("=>")
#     action = current_command[0]
#     town = current_command[1]
#     if action == "Plunder":
#         people = int(current_command[2])
#         gold = int(current_command[3])
#         plunder(town, people, gold, cities)
#     if action == "Prosper":
#         gold = int(current_command[2])
#         if gold >= 0:
#             prosper(town, gold, cities)
#         else:
#             print("Gold added cannot be a negative number!")
#
#     command = input()
#
# if len(cities) > 0:
#     print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
#     for c in cities:
#         print(f"{c} -> Population: {cities[c]['population']} citizens, Gold: {cities[c]['gold']} kg")
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")

# message = input()
# command = input()
# while command != "Reveal":
#     c_command = command.split(":|:")
#     action = c_command[0]
#     if action == "InsertSpace":
#         index = int(c_command[1])
#         message = message[:index] + " " + message[index:]
#     elif action == "Reverse":
#         substring = c_command[1]
#         if substring in message:
#             reversed_substring = substring[::-1]
#             message = message.replace(substring, "", 1)
#             message = message + reversed_substring
#         else:
#             print("error")
#     elif action == "ChangeAll":
#         substring = c_command[1]
#         replacement = c_command[2]
#         message = message.replace(substring, replacement)
#     print(message)
#     command = input()
#
# print(f"You have a new text message: {message}")
# import re
#
# string = input()
# pattern = r"([@|#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
# result = re.finditer(pattern, string)
# val_pairs = ""
# pairs_count = 0
# for i in result:
#     pairs_count += 1
#     if i.group(2) == i.group(3)[::-1]:
#         val_pairs += f"{i.group(2)} <=> {i.group(3)}, "
# if pairs_count > 0:
#     print(f"{pairs_count} word pairs found!")
# else:
#     print("No word pairs found!")
# if len(val_pairs) > 0:
#     print("The mirror words are:")
#     val_pairs = val_pairs.rstrip(", ")
#     for pair in val_pairs:
#         print(pair, end="")
# else:
#     print("No mirror words!")
#

number_of_cars = int(input())
car_dict = {}
for c in range(number_of_cars):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    car_dict[car] = {}
    car_dict[car]["mileage"] = mileage
    car_dict[car]["fuel"] = fuel

command = input()

while command != "Stop":
    current_command = command.split(" : ")
    action = current_command[0]
    car = current_command[1]
    if action == "Drive":
        distance = int(current_command[2])
        fuel = int(current_command[3])
        if car_dict[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_dict[car]["fuel"] -= fuel
            car_dict[car]["mileage"] += distance
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
            if car_dict[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                car_dict.pop(car)

    elif action == "Refuel":
        fuel = int(current_command[2])
        if car_dict[car]["fuel"] + fuel <= 75:
            car_dict[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")

        if car_dict[car]["fuel"] + fuel > 75:
            needed_fuel = 75 - car_dict[car]["fuel"]
            car_dict[car]["fuel"] = 75
            print(f"{car} refueled with {needed_fuel} liters")

    elif action == "Revert":
        kilometers = int(current_command[2])
        if car_dict[car]["mileage"] - kilometers > 10000:
            car_dict[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
        if car_dict[car]["mileage"] <= 10000:
            car_dict[car]["mileage"] = 10000

    command = input()

for car in car_dict:
    print(f'{car} -> Mileage: {car_dict[car]["mileage"]} kms, Fuel in the tank: {car_dict[car]["fuel"]} lt.')
