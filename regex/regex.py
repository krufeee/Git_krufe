import re

text = input()
expression = r"\d+"


matches = re.findall(expression, text)
output = []
for match in matches:
    output.append(match)

print(" ".join(output))

