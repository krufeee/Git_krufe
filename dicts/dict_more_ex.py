# from collections import OrderedDict
#
# contest = {}
# user_points = {}
#
# while True:
#     command = input()
#     if command == "end of contests":
#         break
#     else:
#         current_command = command.split(":")
#         course = current_command[0]
#         password = current_command[1]
#         contest[course] = {password: {}}
#
# while True:
#     command = input()
#     if command == "end of submissions":
#         break
#     else:
#         current_command = command.split("=>")
#         course = current_command[0]
#         password = current_command[1]
#         username = current_command[2]
#         points = int(current_command[3])
#     if course in contest.keys():
#         if password in contest[course]:
#             if username not in contest[course][password]:
#                 contest[course][password][username] = points
#             else:
#                 if contest[course][password][username] < points:
#                     contest[course][password][username] = points
#
# for cour in contest:
#     for passw in contest[cour]:
#         for user in contest[cour][passw]:
#             if user not in user_points:
#                 user_points[user] = contest[cour][passw][user]
#             else:
#                 user_points[user] += contest[cour][passw][user]
#
# max_value = max(user_points.values())
# best_one = ''
# for name, score in user_points.items():
#     if score == max_value:
#         best_one = name
#
# print(f"Best candidate is {best_one} with total {max_value} points.")
# print("Ranking:")
# user_score = {}
# for c in contest:
#     for p in contest[c]:
#         for u in contest[c][p]:
#             if u not in user_score:
#                 user_score[u] = {}
#                 user_score[u][c] = int(contest[c][p][u])
#             else:
#                 user_score[u][c] = int(contest[c][p][u])
#
# user_score = OrderedDict(sorted(user_score.items(), key=lambda item: item[0]))
# user_score = {key: dict(sorted(val.items(), key=lambda ele: ele[1], reverse=True)) for key, val in user_score.items()}
#
# for n in user_score:
#     print(n)
#     for c2 in user_score[n]:
#         print(f"#  {c2} -> {user_score[n][c2]}")


contest_by_user = {}
statistic = {}
contest_by_course = {}
# ----------------------- creating  nested dict from input -----------------------------
while True:
    command = input()
    if command == "no more time":
        break
    else:
        current_command = command.split(' -> ')
        username = current_command[0]
        course = current_command[1]
        points = int(current_command[2])
    if username not in contest_by_user:
        contest_by_user[username] = {}
        contest_by_user[username][course] = points
    else:
        if course not in contest_by_user[username]:
            contest_by_user[username][course] = points
        else:
            if contest_by_user[username][course] == points:
                contest_by_user[username][course] += points
            if contest_by_user[username][course] < points:
                contest_by_user[username][course] = points

# ------------ creating another nested dict from first one (replacing keys) -----------------------
for user in contest_by_user:
    for course in contest_by_user[user]:
        if course not in contest_by_course:
            contest_by_course[course] = {}
            contest_by_course[course][user] = contest_by_user[user][course]
        else:
            contest_by_course[course][user] = contest_by_user[user][course]

# ------------------------------------- sorting dictionaries --------------------------------------
sorted_contest_by_course = {key: dict(sorted(val.items(), key=lambda x: x[0]))
                            for key, val in contest_by_course.items()}

sorted_contest_by_course = {key: dict(sorted(val.items_vault(), key=lambda x: x[1], reverse=True))
                            for key, val in sorted_contest_by_course.items()}

statistic = {k: v for k, v in sorted(statistic.items(), key=lambda item: item[0], reverse=False)}

statistic = {k: v for k, v in sorted(statistic.items(), key=lambda item: item[1], reverse=True)}
# ------------------------------------ printing result -----------------------------------------------
for c in sorted_contest_by_course:
    print(f"{c}: {len(sorted_contest_by_course[c])} participants")
    counter = 1
    for u in sorted_contest_by_course[c]:
        print(f"{counter}. {u} <::> {sorted_contest_by_course[c][u]}")
        counter += 1

print("Individual standings:")

sums = {}

for c in sorted_contest_by_course:
    for u in sorted_contest_by_course[c]:
        if u not in sums:
            sums[u] = sorted_contest_by_course[c][u]
        else:
            sums[u] += sorted_contest_by_course[c][u]

counter2 = 1
for u in sums:
    print(f"{counter2}. {u} -> {sums[u]}")
    counter2 += 1



