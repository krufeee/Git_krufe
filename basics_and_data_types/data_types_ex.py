# number_one = int(input())
# number_two = int(input())
# number_three = int(input())
# number_four = int(input())
#
# result = int((number_one + number_two) / number_three) * number_four
# print(result)

# char_one = input()
# char_two = input()
# char_three = input()
#
# result = char_one + char_two + char_three
# print(result)

# number = int(input())
# total_sum = 0
# for _ in range(number):
#     char = input()
#     total_sum += ord(char)
#
# print(f"The sum equals: {total_sum}")

# start_index = int(input())
# end_index = int(input())
# for i in range(start_index, end_index + 1):
#     print(chr(i), end=" ")

# lines = int(input())
# volume = 0
# for i in range(lines):
#     added_volume = int(input())
#
#     if added_volume + volume <= 255:
#         volume += added_volume
#         continue
#     print("Insufficient capacity!")
# print(volume)


# number_of_snowballs = int(input())
# best_snowball_quality = 0
# best_snowball_data = ""
# for i in range(number_of_snowballs):
#     weight = int(input())
#     time = int(input())
#     quality = int(input())
#
#     result = (weight / time) ** quality
#     if result > best_snowball_quality:
#         best_snowball_quality = result
#         best_snowball_data = f"{weight} : {time} = {int(result)} ({quality})"
#
# print(best_snowball_data)

# lost_fights = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
# expenses = 0
#
# for fight in range(1, lost_fights + 1):
#     if fight % 2 == 0:
#         expenses += helmet_price
#     if fight % 3 == 0:
#         expenses += sword_price
#     if fight % 3 == 0 and fight % 2 == 0:
#         expenses += shield_price
#     if fight % 12 == 0:
#         expenses += armor_price
#
# print(f"Gladiator expenses: {expenses:.2f} aureus")

# number_of_ppl = int(input())
# capacity = int(input())
#
# result = number_of_ppl // capacity
# if number_of_ppl % capacity != 0:
#     result += 1
# print(result)


# number = int(input())
# for i in range(0, number):
#     for n in range(0, number):
#         for f in range(0, number):
#             print(f"{chr(97 + i)}{chr(97 + n)}{chr(97 + f)}")


# group_size = int(input())
# days_of_adventure = int(input())
# all_coins = 0
#
# for i in range(1, days_of_adventure + 1):
#     if i % 10 == 0:
#         group_size -= 2
#     if i % 15 == 0:
#         group_size += 5
#     all_coins += 50 - group_size * 2
#     if i % 3 == 0:
#         all_coins -= group_size * 3
#     if i % 5 == 0:
#         all_coins += group_size * 20
#         if i % 3 == 0:
#             all_coins -= group_size * 2
#
# coins_per_companion = all_coins / group_size
# print(f"{group_size} companions received {int(coins_per_companion)} coins each.")
