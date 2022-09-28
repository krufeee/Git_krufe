# first = set([int(x) for x in input().split()])
# second = set([int(x) for x in input().split()])
#
# n = int(input())
#
# for _ in range(n):
#     command_parts = input().split()
#     command = command_parts[0]
#     target_set = command_parts[1]
#     if command == "Add":
#         if target_set == "First":
#             first = first.union([int(x) for x in command_parts[2:]])
#         else:
#             second = second.union([int(x) for x in command_parts[2:]])
#     elif command == "Remove":
#         if target_set == "First":
#             first = first.difference([int(x) for x in command_parts[2:]])
#         else:
#             second = second.difference([int(x) for x in command_parts[2:]])
#     else:
#         print(first.issubset(second) or second.issubset(first))
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
# from collections import deque
# expression = input().split()
# nums = deque()
# operation = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b,
# }
# for ch in expression:
#     if ch in "+-*/":
#         while len(nums) > 1:
#             left = nums.popleft()
#             right = nums.popleft()
#             result = operation[ch](left, right)
#             nums.appendleft(int(result))
#     else:
#         nums.append(int(ch))
#
# print(nums.pop())
# from collections import deque
#
# chocolate_packages = [int(x) for x in input().split(", ")]
# milk_cups = deque([int(x) for x in input().split(", ")])
# milkshakes = 0
#
# while chocolate_packages and milk_cups and milkshakes < 5:
#     chocolate = chocolate_packages.pop()
#     milk = milk_cups.popleft()
#     if chocolate <= 0 and milk <= 0:
#         continue
#     if chocolate <= 0:
#         milk_cups.appendleft(milk)
#         continue
#     if milk <= 0:
#         chocolate_packages.append(chocolate)
#         continue
#     if chocolate == milk:
#         milkshakes += 1
#     else:
#         milk_cups.append(milk)
#         chocolate_packages.append(chocolate - 5)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# if chocolate_packages:
#     print(f"Chocolate: {', '.join([str(x) for x in chocolate_packages])}")
# else:
#     print("Chocolate: empty")
# if milk_cups:
#     print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
# else:
#     print("Milk: empty")

# from collections import deque
#
# bees = deque([int(x) for x in input().split()])
# nectars = [int(x) for x in input().split()]
# operators = deque(input().split())
#
# honey = 0
# operations = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "/": lambda a, b: a / b,
#     "*": lambda a, b: a * b,
# }
# while bees and nectars:
#     bee = bees.popleft()
#     nectar = nectars.pop()
#
#     if nectar < bee:
#         bees.appendleft(bee)
#         continue
#     if nectar == 0:
#         continue
#     operator = operators.popleft()
#     honey += abs(operations[operator](bee, nectar))
#
# print(f"Total honey made: {honey}")
#
# if bees:
#     print(f"Bees left: {', '.join([str(x) for x in bees])}")
# if nectars:
#     print(f"Nectar left: {', '.join([str(x) for x in nectars])}")


# from collections import deque
# crafted_toys = {}
# crafting_table = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
#
# materials = [int(x) for x in input().split()]
# magic_values = deque([int(x) for x in input().split()])
#
# while materials and magic_values:
#     material = materials.pop()
#     value = magic_values.popleft()
#
#     if material == 0 and value == 0:
#         continue
#     if material == 0:
#         magic_values.appendleft(value)      # ?
#         continue
#     if value == 0:
#         materials.append(material)
#         continue
#
#     result = material * value
#     if result in crafting_table:
#         toy_name = crafting_table[result]
#         if toy_name not in crafted_toys:
#             crafted_toys[toy_name] = 0
#         crafted_toys[toy_name] += 1
#         continue
#     if result < 0:
#         materials.append(material + value)      # ?
#     else:
#         materials.append(material + 15)
#
# if ("Doll" in crafted_toys and "Wooden train" in crafted_toys) or ("Teddy bear" in crafted_toys and "Bicycle" in crafted_toys):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
# if magic_values:
#     print(f"Magic left: {', '.join([str(x) for x in magic_values])}")
#
# for toy, count in sorted(crafted_toys.items()):
#     print(f"{toy}: {count}")

# from collections import deque
#
# words = deque(input().split())
# primary_colours = {"red", "yellow", "blue"}
# secondary_colours = {"orange", "purple", "green"}
# collected_colours = []
#
# while words:
#     left = words.popleft()
#     right = words.pop() if words else ''
#
#     result = left + right
#     if result in primary_colours or result in secondary_colours:
#         collected_colours.append(result)
#         continue
#     result = right + left
#     if result in primary_colours or result in secondary_colours:
#         collected_colours.append(result)
#         continue
#     left = left[:-1]
#     right = right[:-1]
#     if left:
#         words.insert(len(words) // 2, left)
#     if right:
#         words.insert(len(words) // 2, right)
#
# result = []
# forming_colours = {
#     "orange": ["red", "yellow"],
#     "purple": ["red", "blue"],
#     "green": ["yellow", "blue"]
# }
#
# for colour in collected_colours:
#     if colour in primary_colours:
#         result.append(colour)
#         continue
#     is_collected = True
#     for helper_colour in forming_colours[colour]:
#         if helper_colour not in collected_colours:
#             is_collected = False
#             break
#
#     if is_collected:
#         result.append(colour)
#
# print(result)



