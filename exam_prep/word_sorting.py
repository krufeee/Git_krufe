# def words_sorting(*args):
#     words_dict = {}
#     dict_sum = 0
#     end = """"""
#     for word in args:
#         sum_of_chars = 0
#         current_word = [x for x in word]
#         for ch in current_word:
#             sum_of_chars += ord(ch)
#             words_dict[word] = sum_of_chars
#         dict_sum += sum_of_chars
#     if dict_sum % 2 == 0:
#         res = dict(sorted(words_dict.items(), key=lambda item: item[0]))
#     else:
#         res = dict(sorted(words_dict.items(), key=lambda item: -item[1]))
#     for key, value in res.items():
#         end += (f"{key} - {value}" + "\n")
#     return end
#
#
# print(words_sorting('escape', 'charm', 'mythology'))


# def words_sorting(*args):
#     def calculate_word_value(word):
#         return sum(ord(x) for x in word)
#
#     words_dict = {word: calculate_word_value(word) for word in args}
#
#     total_words_value = sum(words_dict.values())
#     if total_words_value % 2 == 0:
#         result = sorted(words_dict.items())
#     else:
#         result = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
#
#     return "\n".join(f'{word} - {count}'for (word, count) in result)
#
#
# print(words_sorting('escape', 'charm', 'mythology'))
