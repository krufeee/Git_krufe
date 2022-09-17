# def find_positive_and_negative_sums(*args):
#     positive_sum = 0
#     negative_sum = 0
#
#     for el in args:
#         if el > 0:
#             positive_sum += el
#         else:
#             negative_sum += el
#
#     return positive_sum, negative_sum
#
#
# nums = [int(x) for x in input().split()]
#
# positive_sum, negative_sum = find_positive_and_negative_sums(*nums)
#
# print(negative_sum)
# print(positive_sum)
#
# if abs(negative_sum) > positive_sum:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")


# def kwargs_length(**kwargs):
#     return len(kwargs)
#
#
# dictionary = {'name': 'Peter', 'age': 25}
#
# print(kwargs_length(**dictionary))


# def even_odd(*args):
#     filter_command = args[-1]
#     parity = 0 if filter_command == "even" else 1
#     result = []
#     for idx in range(len(args) - 1):
#         number = args[idx]
#         if number % 2 == parity:
#             result.append(number)
#
#     return result
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# def even_odd_filter(**kwargs):
#     result = {}
#
#     for key, value in kwargs.items():
#         parity = 0 if key == "even" else 1
#         filtered = [x for x in value if x % 2 == parity]
#         result[key] = filtered
#
#     return dict(sorted(result.items(), key=lambda x: -len(x[1])))
#
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
#
# print(even_odd_filter(
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
#


# def concatenate(*args, **kwargs):
#     text = "".join(args)
#     for kwarg in kwargs:
#         text = text.replace(kwarg, kwargs[kwarg])
#
#     return "".join(text)
#
#
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


# def func_executor(*args):
#     result = []
#     for func_ref, func_params in args:
#         func_result = func_ref(*func_params)
#         result.append(f"{func_ref.__name__} - {func_result}")
#     return "\n".join(result)
#
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))


# def grocery_store(**kwargs):
#     sorted_result = [f'{key}: {value}' for key, value in
#                      sorted(kwargs.items(), key=lambda x: (-x[1], - len(x[0]), x[0]))]
#     return "\n".join(sorted_result)
#

# def age_assignment(*args, **kwargs):
#     result = {}
#
#     for name in args:
#         first_letter = name[0]
#         age = kwargs[first_letter]
#         result[name] = age
#     filtered_result = [f"{name} is {age} years old." for name, age in
#                        sorted(result.items(), key=lambda x: x[0])]
#     return "\n".join(filtered_result)
#
#
# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# def palindrome(word, idx):
#     if idx >= len(word) // 2:
#         return f"{word} is a palindrome"
#
#     left = word[idx]
#     right = word[-1 - idx]
#
#     if left != right:
#         return f"{word} is not a palindrome"
#     return palindrome(word, idx + 1)
#
#
#
# print(palindrome("abcba", 0))

# def fill_the_box(height, length, width, *args):
#     volume = height * length * width
#     left_cubes = 0
#     for el in args:
#         if el == "Finish":
#             break
#         else:
#             if el <= volume:
#                 volume -= el
#             else:
#                 left_cubes += (el - volume)
#                 volume = 0
#     if volume == 0:
#         return f"No more free space! You have {left_cubes} more cubes."
#     else:
#         return f"There is free space in the box. You could put {volume} more cubes."
#
#
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
# from collections import deque
#
#
# def math_operations(*args, **kwargs):
#     nums = deque(args)
#
#     while nums:
#         number = nums.popleft()
#         kwargs["a"] += number
#
#         if not nums:
#             break
#
#         number = nums.popleft()
#         kwargs["s"] -= number
#
#         if not nums:
#             break
#
#         number = nums.popleft()
#         if number != 0:
#             kwargs["d"] /= number
#
#         if not nums:
#             break
#
#         number = nums.popleft()
#         if number != 0:
#             kwargs["m"] *= number
#
#         if not nums:
#             break
#     sorted_result = [f"{key}: {value:.1f}" for key, value in
#                      sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))]
#     return "\n".join(sorted_result)
#
#
# print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
