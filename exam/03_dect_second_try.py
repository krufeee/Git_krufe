text = input().split(" | ")
dict_words = {}
for w in text:
    data = w.split(": ")
    word = data[0]
    definition = data[1]
    if word not in dict_words:
        dict_words[word] = []
        dict_words[word].append(definition)
    else:
        dict_words[word].append(definition)

test_words = input().split(" | ")

action = input()

if action == "Hand Over":
    for w in dict_words:
        print(w, end=" ")

if action == "Test":
    for test_word in test_words:
        if test_word in dict_words:
            print(f"{test_word}:")
            for def_ in dict_words[test_word]:
                print(f" -{def_}")
