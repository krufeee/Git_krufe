import sys
from io import StringIO

test_input = """o e a o e a i
p r s x r"""

test_input1 = """a a a
x r l t p p"""

test_input2 = """u a o i u y o e d w d w w d d d
 """

sys.stdin = StringIO(test_input2)

from collections import deque

flowers = ["rose", "tulip", "lotus", "daffodil"]
flowers_len = [len(x) for x in flowers]

vowels = deque(input().split(" "))
consonants = input().split(" ")
flower_found = False
used_chars = []

while vowels and consonants and not flower_found:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for index, flower in enumerate(flowers):
        if current_vowel in flower and current_vowel not in used_chars:
            occurrences = flower.count(current_vowel)
            flowers_len[index] -= occurrences
            used_chars.append(current_vowel)
        if current_consonant in flower and current_consonant not in used_chars:
            occurrences = flower.count(current_consonant)
            flowers_len[index] -= occurrences
            used_chars.append(current_consonant)
        if flowers_len[index] == 0:
            flower_found = True
            print(f"Word found: {flowers[index]}")
            break
    if flower_found:
        break

if not flower_found:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
