chat = []
line = input()
while line != 'end':
    current_line = line.split(' ')
    command = current_line[0]
    message = current_line[1]
    if command == 'Chat':
        chat.append(message)
    elif command == 'Delete':
        if message in chat:
            chat.remove(message)
    elif command == 'Edit':
        new_message = current_line[2]
        if message in chat:
            index = chat.index(message)
            chat[index] = new_message
    elif command == 'Pin':
        temp = ''
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif command == 'Spam':
        spam = current_line[1:]
        chat.extend(spam)
    line = input()

for m in chat:
    print(m)


