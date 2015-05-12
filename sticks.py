
def game():

    sticks = 10
    current_player = turn()
    while sticks != 0:
        choice = pick_up_sticks(sticks)
        sticks -= choice
        current_player = switch_players(current_player)
        print("{} sticks left!".format(sticks))

    print("{} is the winner!".format(current_player))
    return


def turn(current_player='player1'):
    print(current_player)
    return current_player


def switch_players(current_player):
    if current_player == 'player1':
        current_player = 'player2'
    else:
        current_player = 'player1'
    print("{}'s turn".format(current_player))
    return current_player

def pick_up_sticks(sticks):
    choice = \
    input("How many sticks do you want to pick up?: ")
    while not is_choice_valid(choice, sticks):
        return pick_up_sticks(sticks)
    choice = int(choice)
    return choice


def is_choice_valid(choice,sticks):

    if not choice.isnumeric():
        print("You typed something weird")
        return False
    elif int(choice) > 3 or int(choice) < 1:
        print("You entered an invalid amount.")
        return False
    elif int(choice) > sticks:
        print("There isn't that many sticks left")
        return False
    else:
        return True

# def is_there_a_winner(sticks):
#     if sticks == 0:
#         return

game()


if __name__ == '__main__':
    pass
