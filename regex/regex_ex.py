import re

# pattern = r"\d+"
#
# while True:
#     text = input()
#     if not text:
#         break
#     result = re.findall(pattern, text)
#     if len(result) > 0:
#         print(' '.join(result), end=' ')
#

# data = input()
# pattern = r"\b_[a-zA-Z0-9]+\b"
# result = re.findall(pattern, data)
# words_list = []
#
# for word in result:
#     words_list.append(word[1:])
#
# print(",".join(words_list))

#
# text = input()
# word = input()
#
# pattern = rf"\b{word}\b"
# result = re.findall(pattern, text, re.IGNORECASE)
# print(len(result))


# text = input()
#
# pattern = r"( |^)[a-zA-Z0-9]+((\-|\.|\_)[a-zA-Z0-9]+)*"
# host_pattern = r"([a-zA-Z]+(-[a-zA-Z]+)*)(\.[a-zA-Z]+(-[a-zA-Z]+)*)+"
#
# pattern_1 = rf"{pattern}@{host_pattern}"
#
# emails = re.finditer(pattern_1, text)
#
# for email in emails:
#     print(email[0].lstrip())


# def furniture_info():
#     pattern = r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"
#     spend_money = 0
#     product_list = []
#
#     while True:
#         data = input()
#
#         if data == 'Purchase':
#             break
#         result = re.match(pattern, data)
#
#         if result is not None:
#             product = result[1]
#             price = float(result[2])
#             quantity = float(result[3])
#             spend_money += price * quantity
#             product_list.append(product)
#     print('Bought furniture:')
#
#     if spend_money > 0:
#         print('\n'.join(product_list))
#     print(f"Total money spend: {spend_money:.2f}")
#
#
# furniture_info()

text = input()

pattern = r"www\.[a-zA-Z]+[0-9]*\-*[a-zA-Z]*[0-9]*(\.[a-z]+[0-9]*)+"

matches = re.findall(pattern, text)
result = []
for i in matches:
    print(i.group())
# print('/n'.join(matches))

# for i in matches:
#     result.append(str(i))
#
# print('\n'.join(result))