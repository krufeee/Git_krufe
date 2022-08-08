message = input()
command = input()
while command != "Finish":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Replace":
        old_char = current_command[1]
        new_char = current_command[2]
        message = message.replace(old_char, new_char)
        print(message)
    if action == "Cut":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < 0 or end_index > len(message):
            print("Invalid indices!")
        else:
            message = message[:start_index] + message[end_index + 1:]
            print(message)
    if action == "Make":
        letters_case = current_command[1]
        if letters_case == "Lower":
            message = message.lower()
        else:
            message = message.upper()
        print(message)
    if action == "Check":
        current_string = current_command[1]
        if current_string in message:
            print(f"Message contains {current_string}")
        else:
            print(f"Message doesn't contain {current_string}")
    if action == "Sum":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index < 0 or end_index > len(message):
            print("Invalid indices!")
        else:
            substring = message[start_index:end_index + 1]
            result = 0
            for char in substring:
                result += ord(char)
            print(result)

    command = input()
