size = 6
current_player, other_player = input().split(", ")
matrix = [[x for x in input().split(" ")] for x in range(size)]
skipped = {
    "Tom": False,
    "Jerry": False
}
while True:
    current_row, current_col = input().strip("()").split(", ")
    current_row = int(current_row)
    current_col = int(current_col)
    if skipped[current_player]:
        skipped[current_player] = False
        current_player, other_player = other_player, current_player
        continue

    if matrix[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[current_row][current_col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break
    elif matrix[current_row][current_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        skipped[current_player] = True
    current_player, other_player = other_player, current_player
