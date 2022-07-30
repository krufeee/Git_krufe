friends = input().split(', ')
command = input()
blacklisted_count = 0
lost_count = 0

while command != 'Report':
    current_command = command.split(' ')
    operation = current_command[0]
    name_of_friend = current_command[1]
    if operation == 'Blacklist':
        if name_of_friend in friends:
            name_index = friends.index(name_of_friend)
            friends[name_index] = 'Blacklisted'
            print(f'{name_of_friend} was blacklisted.')
            blacklisted_count += 1
        else:
            print(f"{name_of_friend} was not found.")

    elif operation == 'Error':
        index = int(name_of_friend)
        if 0 <= index < len(friends):
            if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = 'Lost'
                lost_count += 1

    elif operation == 'Change':
        new_name = current_command[2]
        index = int(name_of_friend)
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

    command = input()

result = ' '.join(list(map(str, friends)))
print(f"Blacklisted names: {blacklisted_count}")
print(f"Lost names: {lost_count}")
print(result)





