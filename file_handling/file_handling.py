import os
import re
from io import open

# def print_contents(file_path):
#     print(f"------Opening {file_path}---")
#     file = open(file_path)
#     print(file.read())


# # Relative
# print_contents("./demo.txt")
# print_contents("./file_handling.py")
# print_contents("../pythonProject/.idea/inspectionProfiles/profiles_settings.xml")
#
#
# # Absolute
#
# print_contents("C:/Users/Krufe/PycharmProjects/pythonProject/demo.txt")
#
# print(os.path.abspath("./demo.txt"))

# print(os.sep)


# file_path = "./demo.txt"
# # try:
# #     open(file_path, "r")
# #     print("File found")
# # except FileNotFoundError:
# #     print("File not found")
#
# file = open(file_path, "r")
# print(file.read(2))


# file = open("./numbers.txt", "r")
# the_sum = 0
#
# for line in file:
#     the_sum += int(line)
#
# print(the_sum)

# file = open("./file_handling_demos/w_demos", "w")
# file.write("It works !")
# file.write(os.linesep)
# file.write(str(time.time()))
#
from os.path import exists, join, abspath

file_path = "../demo.txt"


#
# file1 = open(file_path, "a")
# file2 = open(file_path, "a")
#
# file1.write("file 1")
# file2.write("file 2")
# file2.close()
# file1.close()
#
# with open("../demo.txt", "w") as file2:
#     pass
# open(file_path, "w").close()
# if exists(file_path):
#     os.remove(file_path)
#     print("file deleted")
# else:
#     print("no my man")


# os.mkdir(directory_path)
# os.rmdir(directory_path)
# files_and_dirs = os.listdir(directory_path)
#
# files_and_dirs_name = [
#     abspath(join(directory_path, f)) for f in files_and_dirs
# ]
#
# [print(f) for f in files_and_dirs]
# [print(f) for f in files_and_dirs_name]
#
#


# file = open("./words_count_files/input.txt", "a")
# file.close()
#
# def read_words():
#     with open("./words_count_files/words.txt", "r") as file:
#         return file.read().split(" ")
#
#
# def count_words_in_file(words):
#     words_counts = {
#         word: 0 for word in words
#     }
#     with open("./words_count_files/input.txt", "r") as file:
#         for line in file:
#             words_in_line = [w.lower() for w in re.findall(r"\b\S+\b", line)]
#             for word in words:
#                 words_counts[word] += words_in_line.count(word.lower())
#     return words_counts
#
#
# words_count = (
#     count_words_in_file(read_words())
# )
#
# words_count_sorted = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
#
# [
#     print(f"{w} - {c}") for w, c in words_count_sorted
# ]

