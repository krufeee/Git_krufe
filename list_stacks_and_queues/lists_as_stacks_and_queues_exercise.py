# text = input().split()
#
# while text:
#     last_number = text.pop()
#     print(last_number, end=" ")


# number = int(input())
# s = []
# for i in range(number):
#     command = input()
#     if command == "2":
#         if len(s) > 0:
#             s.pop()
#     elif command == "3":
#         if len(s) > 0:
#             print(max(s))
#     elif command == "4":
#         if len(s) > 0:
#             print(min(s))
#     elif command.startswith("1"):
#         c_command = command.split(' ')
#         s.append(c_command[1])


# stack = []
# queries_count = int(input())
# for _ in range(queries_count):
#     queries_parts = [int(x) for x in input().split()]
#     command = queries_parts[0]
#     if command == 1:
#         number = queries_parts[1]
#         stack.append(number)
#     elif command == 2 and stack:
#         stack.pop()
#     elif command == 3 and stack:
#         print(max(stack))
#     elif command == 4 and stack:
#         print(min(stack))
#
# reversed_stack = []
# while stack:
#     reversed_stack.append(str(stack.pop()))
#
# print(', '.join(reversed_stack))

# clothes = [int(x) for x in input().split()]
# rack_capacity = int(input())
# current_rack_capacity = rack_capacity
# rack_counter = 1
#
# while clothes:
#     piece_of_clothing = clothes[-1]
#     if piece_of_clothing <= current_rack_capacity:
#         current_rack_capacity -= piece_of_clothing
#         clothes.pop()
#     else:
#         rack_counter += 1
#         current_rack_capacity = rack_capacity
#
# print(rack_counter)
# from collections import deque
#
# number_of_pumps = int(input())
# pumps = deque()
# for _ in range(number_of_pumps):
#     pumps.append([int(x) for x in input().split()])
#
# for attempt in range(number_of_pumps):
#     trunk = 0
#     failed = False
#     for petrol, distance in pumps:
#         trunk = trunk + petrol - distance
#         if trunk < 0:
#             failed = True
#             break
#     if failed:
#         pumps.append(pumps.popleft())
#     else:
#         print(attempt)
#         break

# expression = input()
#
# pairs = {
#     "(": ")",
#     "[": "]",
#     "{": "}"
# }
#
# opening_brackets = []
#
# balanced = True
# for ch in expression:
#     if ch in "[{(":
#         opening_brackets.append(ch)
#     elif not opening_brackets:
#         balanced = False
#     else:
#         last_opening_bracket = opening_brackets.pop()
#         if pairs[last_opening_bracket] != ch:
#             balanced = False
#     if not balanced:
#         break
#
# if balanced:
#     print("YES")
# else:
#     print("NO")
# from collections import deque
#
# food_quantity = int(input())
# orders = deque([int(x) for x in input().split()])
# orders_list = list(orders)
# max_order = max(orders)
#
# for client in orders_list:
#     if client <= food_quantity:
#         food_quantity -= client
#         orders.popleft()
#     else:
#         break
# print(max_order)
# if orders:
#     left_orders = [str(x) for x in orders]
#     print('Orders left:'+' '+' '.join(left_orders))
# else:
#     print('Orders complete')


# from collections import deque
#
#
# def to_str_time(time_in_seconds_):
#     hours = time_in_seconds_ // 3600
#     minutes = (time_in_seconds_ % 3600) // 60
#     seconds = (time_in_seconds_ % 3600) % 60
#     return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#
#
# def read_products():
#     result = deque()
#     while True:
#         line = input()
#         if line == "End":
#             break
#         result.append(line)
#     return result
#
#
# def to_seconds(hours, minutes, seconds):
#     return hours * 3600 + minutes * 60 + seconds
#
# l,3
# def read_robots():
#     result = {}
#     robots_input = input().split(";")
#     for robot_input in robots_input:
#         robot_details = robot_input.split("-")
#         name = robot_details[0]
#         processing_time = int(robot_details[1])
#         result[name] = processing_time
#     return result
#
#
# robots = read_robots()
# available_robots = [k for k in robots.keys()]
# processing_robots = {}
#
# starting_time_parts = [int(x) for x in input().split(":")]
# time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts [2])
#
# products = read_products()
#
# while products:
#     time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
#
#     for robot_name in [k for k in processing_robots.keys()]:
#         processing_robots[robot_name] -= 1
#         if processing_robots[robot_name] <= 0:
#             processing_robots.pop(robot_name)
#
#     current_product = products.popleft()
#     for robot_name in available_robots:
#         if robot_name not in processing_robots:
#             print(f"{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]")
#             processing_robots[robot_name] = robots[robot_name]
#             break
#     else:
#         products.append(current_product)

# def passing_car(car):
#     current_car = deque(str(x) for x in car)
from collections import deque

bullet_prise = int(input())
size_of_barrel = int(input())
bullets_stack = [int(x) for x in input().split(" ")]
locks = deque([int(x) for x in input().split(" ")])
intelligence = int(input())
barrel = size_of_barrel
while True:
    if not bullets_stack:
        break
    if not locks:
        break
    if intelligence - bullet_prise <= 0:
        break
    if barrel > 0:
        current_lock = locks.popleft()
        current_bullet = bullets_stack.pop()
        if current_lock >= current_bullet:
            print("Bang!")
        else:
            locks.appendleft(current_lock)
            print("Ping!")
        barrel -= 1
        intelligence -= bullet_prise
    if barrel == 0 and bullets_stack:
        print("Reloading!")
        barrel = size_of_barrel

if not locks:
    print(f"{barrel} bullets left."
          f" Earned ${intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
