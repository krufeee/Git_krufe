# first_name = input()
# second_name = input()
# delimiter = input()
#
# print(f"{first_name}{delimiter}{second_name}")

# meters = float(input())
# kilometers = meters / 1000
# print(f"{kilometers:.2f}")

# pounds = float(input())
# dollars = pounds * 1.31
# print(f"{dollars:.3f}")

# centuries = int(input())
# years = centuries * 100
# days = int(365.2422 * years)
# hours = days * 24
# minutes = hours * 60
# print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

# number = int(input())
# for i in range(1, number + 1):
#     working_number = i
#     digit_sum = 0
#     while working_number > 0:
#         digit_sum += working_number % 10
#         working_number = int(working_number / 10)
#     is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11
#     print(f"{i} -> {is_special}")


# year = int(input())
# is_happy_year = False
# while not is_happy_year:
#     year += 1
#     str_year = str(year)
#     set_year = set()  # set_year = set(set_year) - without for cycle
#     for i in range(len(str_year)):
#         set_year.add(str_year[i])
#     # if len(str_year) == len(set_year):
#     #     is_happy_year = True
#     is_happy_year = len(str_year) == len(set_year)
# print(year)