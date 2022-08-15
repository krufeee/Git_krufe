import io

text = """-I was quick to judge him, but it wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
"""
with open("./file_handling_demos/text.txt", "w") as file:
    file.write(text)


def replace_symbols(string):
    symbols = ["-", ",", ".", "!", "?"]
    for s in symbols:
        string = string.replace(s, "@")
    return string


with open("./file_handling_demos/text.txt" , "r") as file:
    # print(file.read())
    for idx, line in enumerate(file):
        if idx % 2 == 0:
            result = " ".join(line.strip().split()[:: -1])
            print(replace_symbols(result))