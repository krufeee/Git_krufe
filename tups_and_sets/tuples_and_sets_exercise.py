# n = int(input())
# usernames = set()
# for _ in range(n):
#     username = input()
#     usernames.add(username)
# [print(u) for u in usernames]

# numbers = input().split(" ")
# n = int(numbers[0])
# m = int(numbers[1])
# n_set = set()
# m_set = set()
# for i in range(n + m):
#     data = input()
#     if i + 1 <= n:
#         n_set.add(data)
#     else:
#         m_set.add(data)
#
# result = n_set.intersection(m_set)
# [print(u) for u in result]

# sett = set()
# n = int(input())
# for _ in range(n):
#     elements = input().split()
#     for e in elements:
#         sett.add(e)
#
# print(*sett, sep="\n")


# text = input()
#
# symbols = {}
# for ch in text:
#     if ch not in symbols:
#         symbols[ch] = 0
#     symbols[ch] += 1
#
# for key, value in sorted(symbols.items()):
#     print(f"{key}: {value} time/s")

# n = int(input())
# best_intersection = set()
#
# for _ in range(n):
#     first_range, second_range = input().split("-")
#     first_start, first_end = [int(x) for x in first_range.split(",")]
#     second_start, second_end = [int(x) for x in second_range.split(",")]
#
#     first = set(range(first_start, first_end + 1))
#     second = set(range(second_start, second_end + 1))
#
#     current_intersection = first.intersection(second)
#
#     if len(current_intersection) > len(best_intersection):
#         best_intersection = current_intersection
#
# print(f"Longest intersection is [{', '.join([str(x) for x in best_intersection])}]"
#       f" with length {len(best_intersection)}")
#

# n = int(input())
# even = set()
# odd = set()
#
# for row in range(1, n + 1):
#     name = input()
#     name_sum = sum([ord(x) for x in name]) // row
#     if name_sum % 2 == 0:
#         even.add(name_sum)
#     else:
#         odd.add(name_sum)
#
# even_sum = sum(even)
# odd_sum = sum(odd)
#
# if even_sum == odd_sum:
#     result = odd.union(even)
# elif even_sum > odd_sum:
#     result = odd.symmetric_difference(even)
# else:
#     result = odd.difference(even)
#
# print(*result, sep=", ")
# from collections import deque
#
# cars = deque()
# green_light = int(input())
# free_window = int(input())
# passed_counter = 0
# crashed = False
# while not crashed:
#     line = input()
#     if line == "END":
#         break
#
#     if line == "green":
#         current_green = green_light
#         while cars and current_green > 0:
#             car = cars.popleft()
#             if len(car) <= current_green + free_window:
#                 passed_counter += 1
#             else:
#                 print("A crash happened!")
#                 print(f"{car} was hit at {car[current_green + free_window]}.")
#                 crashed = True
#                 break
#             current_green -= len(car)
#     else:
#         cars.append(line)
#
# if not crashed:
#     print("Everyone is safe.")
#     print(f"{passed_counter} total cars passed the crossroads.")