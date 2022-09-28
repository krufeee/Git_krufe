# s = []
# s.append(1)
# s.append(2)
# s.append(3)
# s.append(4)
# s.append(5)
# s.append(6)
# s.append(7)
# s.append(8)
# print(s)
# print(s[-1])
# s.pop()
# print(s)
# s.append(9)
# print(s)
# pri nt(len(s))


# text = input()
# s = []
#
# for c in text:
#     s.append(c)
#
# reversed_text = ""
#
# while s:
#     reversed_text += s.pop()
#
# print(reversed_text)

# expression = input()
#
# s = []
# for i in range(len(expression)):
#     if expression[i] == "(":
#         s.append(i)
#     elif expression[i] == ")":
#         start_index = s.pop()
#         end_index = i + 1
#         print(expression[start_index:end_index])

#
# q = deque()
#
# while True:
#     command = input()
#     if command == "End":
#         print(f"{len(q)} people remaining.")
#         break
#     elif command == "Paid":
#         while q:
#             print(q.popleft())
#     else:
#         q.append(command)
# from collections import deque
#
# ppl = deque()
# vol = int(input())
# while True:
#     command = input()
#     if command == "Start":
#         break
#     ppl.append(command)
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     elif command.startswith("refill "):
#         params = command.split(" ")
#         vol += int(params[1])
#     else:
#         person = ppl.popleft()
#         wanted_watter = int(command)
#         if wanted_watter <= vol:
#             print(f"{person} got water")
#             vol -= wanted_watter
#         else:
#             print(f"{person} must wait")
# print(f"{vol} liters left")

# from collections import deque
# kids_string = input()
# count = 0
# toss_as_string = input()
# tosses_count = int(toss_as_string)
# kids = deque(kids_string.split(" "))
#
# while len(kids) > 1:
#     count += 1
#     kid = kids.popleft()
#     if count < tosses_count:
#         kids.append(kid)
#     else:
#         print(f"Removed {kid}")
#         count = 0
#
# print(f"Last is {kids[0]}")