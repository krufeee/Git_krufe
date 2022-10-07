import sys

from io import StringIO

test_input = """105 20 30 25
120 60 11 400 10 1
"""
test_input1 = """30 5 21 6 0 91
15 9 5 15 8
"""
test_input2 = """200
5 15 32 20 10 5
"""

sys.stdin = StringIO(test_input)


from collections import deque

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

materials = deque([int(x) for x in input().split(" ")])  # last
magic_levels = deque([int(x) for x in input().split(" ")])  # first
counter = 0
while materials and magic_levels:
    if counter <= 1:
        current_material = materials.pop()
        current_magic_level = magic_levels.popleft()
        product = current_material + current_magic_level
        if 0 < product < 100 and counter == 0:
            if product % 2 == 0:
                current_material *= 2
                current_magic_level *= 3
            else:
                current_material *= 2
                current_magic_level *= 2
            counter += 1
            materials.append(current_material)
            magic_levels.appendleft(current_magic_level)
            continue
        elif 100 <= product <= 199:
            gifts["Gemstone"] += 1
            counter = 0
        elif 200 <= product <= 299:
            gifts["Porcelain Sculpture"] += 1
            counter = 0
        elif 300 <= product <= 399:
            counter = 0
            gifts["Gold"] += 1
        elif 400 <= product <= 499:
            counter = 0
            gifts["Diamond Jewellery"] += 1
        elif product >= 500 and counter == 0:
            current_material /= 2
            current_magic_level /= 2
            counter += 1
            materials.append(current_material)
            magic_levels.appendleft(current_magic_level)
            continue
        counter = 0
    else:
        counter = 0
        continue

crafting_successful = False

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or \
        gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    crafting_successful = True

if crafting_successful:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: ", end="")
    print(", ".join(str(x) for x in materials))

if magic_levels:
    print(f"Magic left: ", end="")
    print(", ".join(str(x) for x in magic_levels))

sorted_gifts = {key: value for key, value in (sorted(gifts.items(), key=lambda x: x[0]))}

for key, value in sorted_gifts.items():
    if value > 0:
        print(f"{key}: {value}")
