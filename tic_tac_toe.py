print("Welcome to Tic-Tac-Toe.")
print("Choose who is going to be X, and who is going to be O.\n")


def make_board():
    print(f"     |     |     ")
    print(f"  {my_data[0][0]}  |  {my_data[0][1]}  |  {my_data[0][2]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {my_data[1][0]}  |  {my_data[1][1]}  |  {my_data[1][2]}  ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"  {my_data[2][0]}  |  {my_data[2][1]}  |  {my_data[2][2]}  ")
    print(f"     |     |     ")


def place_item(item, place):
    place[0] -= 1
    place[1] -= 1

    if my_data[place[0]][place[1]] == "X" or my_data[place[0]][place[1]] == "O":
        return False
    else:
        my_data[place[0]][place[1]] = item
        win_result = check_win()
        if win_result == True:
            make_board()
            print(f"{item} Won!")
            return "win"
        elif win_result == "tie":
            make_board()
            print("Tie")
            return "tie"
        else:
            return True


def check_win():
    for n in range(0, 3):
        if my_data[n][0] == my_data[n][1] == my_data[n][2] and my_data[n][0] != " ":
            return True
        elif my_data[0][n] == my_data[1][n] == my_data[2][n] and my_data[n][0] != " ":
            return True

    if my_data[0][0] == my_data[1][1] == my_data[2][2] and my_data[0][0] != " ":
        return True
    if my_data[0][2] == my_data[1][1] == my_data[2][0] and my_data[2][0] != " ":
        return True

    if my_data[0][0] != " " and my_data[0][1] != " " and my_data[0][2] != " " and my_data[1][0] != " " and my_data[1][1] != " " and my_data[1][2] != " " and my_data[2][0] != " " and my_data[2][1] != " " and my_data[2][2] != " ":
        return "tie"


my_data = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]


game_still_on = True
while game_still_on:
    while True:
        make_board()
        print("X, where do you want to put your X?")
        x_place = input("Enter the row number. For example, 2 would specify the 2nd row. ")
        y_place = input("Enter the column number. For example, 2 would specify the 2nd column. ")

        try:
            int_x_place = int(x_place)
            int_y_place = int(y_place)
        except ValueError:
            print("One of the numbers you put in isn't a number.")
            continue

        if int_x_place < 1 or int_x_place > 3:
            print("The row number is less than 1 or greater than 3.")
            continue
        elif int_y_place < 1 or int_y_place > 3:
            print("The column number is less than 1 or greater than 3.")
            continue

        coordinates = [int_x_place, int_y_place]
        result = place_item("X", coordinates)
        if not result:
            print("That place is already filled.")
            continue
        elif result == "win" or result == "tie":
            while True:
                continue_next_game = input("Do you want to continue to the next game? y/n ")
                if continue_next_game.lower() == "n":
                    game_still_on = False
                    exit()
                elif continue_next_game.lower() == "y":
                    game_still_on = True
                    my_data = [[" ", " ", " "],
                               [" ", " ", " "],
                               [" ", " ", " "]]
                    break
                else:
                    print("You did not type y or n.")
                    continue
        else:
            break

    while True:
        make_board()
        print("O, where do you want to put your O?")
        x_place = input("Enter the row number. For example, 2 would specify the 2nd row. ")
        y_place = input("Enter the column number. For example, 2 would specify the 2nd column. ")

        try:
            int_x_place = int(x_place)
            int_y_place = int(y_place)
        except ValueError:
            print("One of the numbers you put in isn't a number.")
            continue

        if int_x_place < 1 or int_x_place > 3:
            print("The row number is less than 1 or greater than 3.")
            continue
        elif int_y_place < 1 or int_y_place > 3:
            print("The column number is less than 1 or greater than 3.")
            continue

        coordinates = [int_x_place, int_y_place]
        result = place_item("O", coordinates)
        if not result:
            print("That place is already filled.")
            continue
        elif result == "win" or result == "tie":
            while True:
                continue_next_game = input("Do you want to continue to the next game? y/n ")
                if continue_next_game.lower() == "n":
                    game_still_on = False
                    exit()
                elif continue_next_game.lower() == "y":
                    game_still_on = True
                    my_data = [[" ", " ", " "],
                               [" ", " ", " "],
                               [" ", " ", " "]]
                    break
                else:
                    print("You did not type y or n.")
                    continue
        else:
            break
