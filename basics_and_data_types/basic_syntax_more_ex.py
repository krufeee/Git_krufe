# number = int(input())
# if number > 0:
#     number = str(number)
#     number = list(number)
#     number.sort()
#     number.reverse()
#     result = ""
#     for i in number:
#         result += i
#     print(result)
# else:
#     number = str(number)
#     number = list(number)
#     number.sort()
#     result = ""
#     for i in number:
#         result += i
#     print(result)

# word = input()
# list_one = []
# for i in range(len(word)):
#     if word[i].isupper():
#         list_one.append(i)
# print(list_one)

# line = input()
# list_one = list(line.split(", "))
#
# for i in range(1, len(list_one) + 1):
#     if list_one[i - 1] == "wolf" and i == len(list_one):
#         print("Please go away and stop eating my sheep")
#     elif list_one[i - 1] == "wolf":
#         warned_sheep = len(list_one) - i
#         print(f"Oi! Sheep number {warned_sheep}! You are about to be eaten by a wolf!")

# string = input()
# string = string.lower()
# counter = 0
# if "sand" in string:
#     counter += string.count("sand")
# if "water" in string:
#     counter += string.count("water")
# if "fish" in string:
#     counter += string.count("fish")
# if "sun" in string:
#     counter += string.count("sun")
# print(counter)
