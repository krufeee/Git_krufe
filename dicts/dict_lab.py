# data = input().split(' ')
# search_data = input().split(' ')
# bakery = dict()
#
# for i in range(0, len(data), 2):
#     food = data[i]
#     quantity = int(data[i + 1])
#     bakery[food] = quantity
#
# for search_term in search_data:
#     if search_term in bakery.keys():
#         print(f"We have {bakery[search_term]} of {search_term} left")
#     else:
#         print(f"Sorry, we don't have {search_term}")
#
#

# text = input()
# store = dict()
#
# while text != 'statistics':
#     text = text.split(': ')
#     product = text[0]
#     quantity = int(text[1])
#
#     if product in store.keys():
#         store[product] += quantity
#     else:
#         store[product] = quantity
#
#     text = input()
#
# count = len(store.keys())
# total = sum(store.values())
#
# print('Products in stock:')
# for p in store:
#     print(f"- {p}: {store[p]}")
# print(f"Total Products: {count}")
# print(f"Total Quantity: {total}")

# text = input()
# courses = {}
#
# while ':' in text:
#
#     data = text.split(':')
#     name = data[0]
#     id = data[1]
#     course = data[2]
#
#     if course not in courses.keys():
#         courses[course] = {}
#
#     courses[course][id] = name
#
#     text = input()
#
# text = text.replace('_', ' ')
#
# for id in courses[text]:
#     print(f"{courses[text][id]} - {id}")

# characters = input().split(', ')
#
# char_dict = {char: ord(char) for char in characters}
# print(char_dict)

# words = input().split(' ')
# words = list(map(lambda w: w.lower(), words))
#
# occurrences = {}
#
# for word in words:
#     if word not in occurrences:
#         occurrences[word] = 1
#     else:
#         occurrences[word] += 1
#
# odd_words = []
#
# for w in occurrences.keys():
#     if occurrences[w] % 2 != 0:
#         odd_words.append(w)
#
# print(' '.join(odd_words))

# count = int(input())
# dict = {}
#
# for i in range(count):
#     word = input()
#     synonym = input()
#
#     if word not in dict:
#         dict[word] = []
#
#     dict[word].append(synonym)
#
# for word in dict:
#     synonyms = ', '.join(dict[word])
#     print(f'{word} - {synonyms}')