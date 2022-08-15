from os import remove
from os.path import exists


while True:
    line = input()
    if line == "End":
        break

    command = line.split("-")
    action = command[0]
    file_name = command[1]
    if action == "Create":
        with open(f"./{file_name}", "w") as file:
            pass
    elif action == "Add":
        content = command[2]
        with open(f"./{file_name}", "a") as file:
            file.write(f"{content}\n")
    elif action == "Replace":
        old_string = command[2]
        new_string = command[3]
        if exists(f"./{file_name}"):
            with open(f"./{file_name}", "r+") as file:
                file_content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate(0)
                file.write(file_content)
        else:
            print("An error occurred")
    else:
        if exists(f"./{file_name}"):
            print(f"Delete-{file_name}")
            remove(f"./{file_name}")
        else:
            print("An error occurred")
