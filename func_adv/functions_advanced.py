# def multiply(*args):
#     product = 1
#     for v in args:
#         product *= v
#     return product

# def get_info(name, town, age):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# info1 = {
#     "name": "Pesho",
#     "town": "Varna",
#     "age": 34,
# }
#
# info2 = {
#     "name": "Ivan",
#     "town": "Stara Zagora",
#     "age": 48,
# }
#
#
# print(f(**info1))
# print(f(**info2))


# def sorting_cheeses(**kwargs):
#     sorted_cheeses = sorted(
#         kwargs.items(),
#         key=lambda x: (-len(x[1]), x[0])
#     )
#
#     result = []
#
#     for name, pieces_counts in sorted_cheeses:
#         result.append(name)
#         result.extend(sorted(pieces_counts, reverse=True))
#
#     return "\n".join([str(x) for x in result])
#
#
# print(
#     sorting_cheeses(
#         Parmesan=[102, 120, 135],
#         Camembert=[100, 100, 105, 500, 430],
#         Mozzarella=[50, 125],
#     )
# )

# def rectangle(length, width):
#     def area():
#         return length * width
#
#     def perimeter():
#         return 2 * (length + width)
#
#     if not isinstance(length, int) \
#             or not isinstance(width, int):
#         return "Enter valid values!"
#
#     return f"""Rectangle area: {area()}
# Rectangle perimeter: {perimeter()}"""
#
#
# print(rectangle(2, 10))
# print(rectangle('2', 10))


# def operate(operation, *args):
#     def add(*args):
#         return sum(args)
#
#     def subtract(x, *args):
#         return x + sum(-y for y in args)
#
#     def multiply(*args):
#         result = 1
#         for v in args:
#             result *= v
#         return result
#
#     def divide(x, *args):
#         result = x
#         for v in args:
#             result /= v
#         return result
#
#     if operation == "+":
#         return add(*args)
#     elif operation == "-":
#         return subtract(*args)
#     elif operation == "*":
#         return multiply(*args)
#     elif operation == "/":
#         return divide(*args)
#
#
# print(operate("*", -1, -2, 3, 5))
# print(operate("/", -3, 4, -2, 3))


def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)

