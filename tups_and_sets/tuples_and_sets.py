#
# numbers_string = input()
# dd = {}
# numbers = [float(x) for x in numbers_string.split(" ")]
#
# for number in numbers:
#     if number not in dd:
#         dd[number] = 0
#
#     dd[number] += 1
#
#
# for number, count in dd.items():
#     print(f"{number:.1f} - {count} times")
#

# number_of_students = int(input())
#
#
# students_grades = {}
#
# for _ in range(number_of_students):
#     students = input()
#     data = students.split(" ")
#     student = data[0]
#     evaluation = float(data[1])
#     if student not in students_grades:
#         students_grades[student] = []
#     students_grades[student].append(evaluation)
#
# for s in students_grades:
#     average = sum(students_grades[s]) / len(students_grades[s])
#     print(f"{s} -> ", end='')
#     for e in students_grades[s]:
#         print(f'{e:.2f} ', end='')
#     print(f'(avg: {average:.2f})')

# unique_names = set()
# number_of_names = int(input())
# for _ in range(number_of_names):
#     names = input()
#     unique_names.add(names)
#
# [print(name) for name in unique_names]

# n = int(input())
# parking_lot_logs = [input().split(", ") for _ in range(n)]
# parking_lot = set()
# for direction, car_number in parking_lot_logs:
#     if direction == "IN":
#         parking_lot.add(car_number)
#     else:
#         parking_lot.remove(car_number)
#
# if parking_lot:
#     [print(car_number) for car_number in parking_lot]
# else:
#     print("Parking Lot is Empty")


# def is_vip(guest):
#     return guest[0].isdigit()
#
#
# n = int(input())
#
# vip_guests = set()
# regular_guests = set()
# for _ in range(n):
#     reservation = input()
#     if is_vip(reservation):
#         vip_guests.add(reservation)
#     else:
#         regular_guests.add(reservation)
#
# while True:
#     guest = input()
#     if guest == "END":
#         break
#     if is_vip(guest):
#         vip_guests.remove(guest)
#     else:
#         regular_guests.remove(guest)
#
# print(len(vip_guests) + len(regular_guests))
# [print(guest) for guest in sorted(vip_guests)]
# [print(guest) for guest in sorted(regular_guests)]

# list_of_numbers = [int(x) for x in input().split(" ")]
# target = int(input())
# counter = 0
# pairs = set()
#
# for i in range(len(list_of_numbers)):
#     for j in range(i + 1, len(list_of_numbers)):
#         counter += 1
#         if list_of_numbers[i] + list_of_numbers[j] == target:
#             print(f"{list_of_numbers[i]} + {list_of_numbers[j]} = {target}")
#             pairs.add((list_of_numbers[i], list_of_numbers[j]))
#
# print(f"Iterations done: {counter}")
# [print(pair) for pair in pairs]

