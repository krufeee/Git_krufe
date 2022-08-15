import io


def counter_sym(text):
    text = text.strip()
    symbols = ["-", ",", ".", "!", "?", "'"]
    counter_s = 0
    counter_ch = 0
    for ch in text:
        if ch in symbols:
            counter_s += 1
        else:
            if ch != " ":
                counter_ch += 1
    return counter_s, counter_ch


with open("./text.txt", "r") as file:
    for idx, line in enumerate(file):
        char_count = counter_sym(line)[1]
        sym_count = counter_sym(line)[0]
        result = f"Line {idx + 1}: {line.strip()} ({char_count})({sym_count})\n"
        with open("./output.txt", "a") as file2:
            file2.write(result)
