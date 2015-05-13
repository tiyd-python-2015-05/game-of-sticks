from sticks_two_player import TwoPlayerGame
from sticks_player_vs_AI import OnePlayerGame, ArtIn

def do_game(ai_1, ai_2):
    '''plays through one single 15-stick game'''
    number_of_sticks = 15
    winner = None
    while number_of_sticks > 1:
        ai_choice = ai_1.pick_some_sticks(number_of_sticks)
        number_of_sticks = number_of_sticks - ai_choice
        if number_of_sticks <= 1:
            if number_of_sticks == 1:
                winner = ai_1
            else:
                winner = ai_2
            break

        ai_choice = ai_2.pick_some_sticks(number_of_sticks)
        number_of_sticks = number_of_sticks - ai_choice
        if number_of_sticks <= 1:
            if number_of_sticks == 1:
                winner = ai_2
            else:
                winner = ai_1
            break

    return winner, winner.game_choices

def create_AI(ai_1, ai_2):
    '''Trains AI by pitting two ai's against each other 1000 times.  Begins a game with
    the winningest AI'''
    print("Training AI...")
    games = 1000
    ai_1_choices = {}
    ai_2_choices = {}
    ai_1_count = 0
    ai_2_count = 0
    good_choices = {}
    while games != 0:
        winner, good_choices = do_game(ai_1, ai_2)

        if winner == ai_1:
            ai_1_count += 1
            for pair in good_choices.items():
                if pair[0] in ai_1_choices.keys():
                    ai_1_choices[pair[0]].extend(pair[1])
                else:
                    ai_1_choices[pair[0]] = pair[1]
        else:
            ai_2_count += 1
            for pair in good_choices.items():
                if pair[0] in ai_2_choices.keys():
                    ai_2_choices[pair[0]].extend(pair[1])
                else:
                    ai_2_choices[pair[0]] = pair[1]

        games -= 1

    if ai_1_count > ai_2_count:
        game = OnePlayerGame(ai_1_choices)
        game.start()
    else:
        game = OnePlayerGame(ai_2_choices)
        game.start()


if __name__ == '__main__':
    usr_choice = input("Welcome to the Game of Sticks, would you like to play against a (H)uman, (A)I, or a (T)rained AI? ").lower()
    if usr_choice == "h":
        game = TwoPlayerGame()
        game.start()
    elif usr_choice == "a":
        game = OnePlayerGame()
        game.start()
    else:
        ai_1 = ArtIn(15)
        ai_2 = ArtIn(15)
        create_AI(ai_1, ai_2)
