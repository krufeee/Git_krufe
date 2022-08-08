import re

text = input()

pattern = r"[@|#]+([a-z]{3,})[@|#]+[^a-zA-Z0-9]*[\/]+([0-9]+)[\/]+"

result = re.finditer(pattern, text)

for match in result:
    color = match.group(1)
    amount = match.group(2)
    print(f"You found {amount} {color} eggs!")
