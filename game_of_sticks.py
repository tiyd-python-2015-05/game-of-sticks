import os
import random


class SticksGame:
    # X Print out rules
    # X create and start turns
    # X remove turn sticks from pile
    # X display remaining sticks
    # X Stop when player starts turn with one stick in pile
    def __init__(self, player1, player2):
        self.pile = 20
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def display_rules(self):
        print("Welcome to the Game of Sticks!\n\
In the Game of Sticks there is a heap of sticks on a board.\n\
On their turn, each player picks up 1 to 3 sticks.\n\
The one who has to pick the final stick will be the loser.\n")

    def display_pile(self):
        return "Pile contains {} sticks.".format(self.pile)

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def remove(self):
        print("Currently {}'s turn".format(self.current_player.name))
        self.current_player.pick_up(self.pile)
        self.pile -= self.current_player.sticks
        self.current_player.sticks = 0

    def winner(self):
        if self.pile > 0:
            return None
        else:
            return self.current_player

    def menu(self):
        self.display_rules()

        go = input("Ready? (y/n) ").lower()

        if go[0] == "y":
            self.start()
        elif go[0] == "n":
            return
        else:
            self.menu()

    def start(self):
        self.pile = 20
        while not self.winner():
            os.system('clear')
            print(self.display_pile())
            self.remove()
            self.switch_players()

        self.current_player.win_state = True
        print("Game Over!")
        self.player1.win_check()
        self.player2.win_check()
        self.play_again()

    def play_again(self):
        go_again = input("Would you like to play again (y/n)? ").lower()

        if go_again[0] == "y":
            self.start()
        elif go_again[0] == "n":
            return
        else:
            self.play_again()

###############################################################################


class Player:
    # X decide how many sticks to pick up
    def __init__(self, name="Player"):
        self.name = name
        self.sticks = 0
        self.win_state = False

    def pick_up(self, remaining):
        try:
            num = int(input("How many sticks would you like to pick up? "))

            if num in [1, 2, 3]:
                self.sticks = num
            else:
                print("Invalid choice!")
                return self.pick_up(remaining)
        except ValueError:
            print("Invalid choice!")
            return self.pick_up(remaining)

    def win_check(self):
        if self.win_state:
            print("The winner is {}!".format(self.name))

    def __repr__(self):
        return self.name

###############################################################################


class AIPlayer(Player):
    def __init__(self, name="AI"):
        super().__init__(name)
        self.chosen = {}
        self.possibilities = {}
        self.tally = 0

    def choices(self, remaining):
        return self.possibilities.setdefault(remaining, [1, 2, 3])

    def pick_up(self, remaining):
        choice = random.choice(self.choices(remaining))
        self.chosen[remaining] = choice
        self.sticks = choice

    def win_check(self):
        if self.win_state:
            print("The winner is {}!".format(self.name))
            self.integrate_win()
            self.tally += 1
        else:
            self.chosen = {}

    def integrate_win(self):
        # for each choice made, add that choice into the
        # possible choices
        for key in self.chosen:
            self.possibilities[key].append(self.chosen[key])

        self.chosen = {}


###############################################################################

def menu():
    print("Welcome to the Game of Sticks!\n\
In the Game of Sticks there is a heap of sticks on a board.\n\
On their turn, each player picks up 1 to 3 sticks.\n\
The one who has to pick the final stick will be the loser.\n")

    set_up = input("Would you like to play against another [h]uman, \
a [c]omputer, or a [t]rained computer? ").lower()

    if set_up[0] == "h":
        player_name1 = input("First Player's Name: ")
        player_name2 = input("Second Player's Name: ")
        player1 = Player(player_name1)
        player2 = Player(player_name2)
        game = SticksGame(player1, player2)
        game.start()
    elif set_up[0] == "c":
        player_name = input("Your Name: ")
        player1 = Player(player_name)
        player2 = AIPlayer()
        game = SticksGame(player1, player2)
        game.start()
    elif set_up[0] == "c":
        player_name = input("Your Name: ")
        player1 = Player(player_name)
        player2 = AIPlayer()
        game = SticksGame(player1, player2)
        game.start()
    else:
        os.system('clear')
        print("Invalid choice, please try again")
        return menu()


if __name__ == '__main__':
    menu()
