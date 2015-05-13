import sys
import random

class Player:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return "{}".format(self.name)

    def sticks_choice(self, available_sticks):
        print("You have {} sticks remaining.".format(available_sticks))
        sticks = input("How many do you take (1-3)? ")
        try:
            sticks = int(sticks)
            if 1 <= sticks <= 3 and sticks <= available_sticks:
                return sticks
            else:
                print("Select a maximum of 3 sticks from {} remaining".format(available_sticks))
                return self.sticks_choice(available_sticks)
        except ValueError:
            print("Please enter a number")
            self.sticks_choice(available_sticks)


class Game:
    current_player = ''


    def welcome(self):
        print("\t======WELCOME TO Game of Sticks======\n \
                Rules of the Game:\n \
                - Pick any number of sticks 1 through 3\n \
                - The one to pick the last stick is the loser")


    def is_integer(self, num = 0):
        '''check that the choice is an integer'''
        return isinstance(num, int)


    def is_valid_selection(self, choice, available_sticks):
        '''test if the choice of sticks is valid'''
        if choice < available_sticks and 1 <= choice <= 3:
            return True
        else:
            return False


    def remaining_sticks(self, picked_sticks, initial_sticks):
        return initial_sticks - picked_sticks


    def switch_player(self, playerA, playerB):
        if self.current_player == playerA:
            self.current_player = playerB
        else:
            self.current_player = playerA


    def game_sticks(self):
        sticks = input("How many sticks are there on the table (10-100)? ")
        try:
            sticks = int(sticks)
            if 10 <= sticks <= 100:
                return sticks
            else:
                print("Sticks should be between 10 and 100")
                return self.game_sticks()
        except ValueError:
            print("Please enter a number")
            return self.game_sticks()


    def game_continue(self):
        play_again = input("Do you want to continue? Y/N ").lower()
        return True if play_again[0] == 'y' else sys.exit()


    def game_over(self, sticks_available):
        if sticks_available > 0:
            return True
        else:
            return False


    def play(self):
        self.welcome()
        while True:
            players = [Player("Sovello"), Player("Hilde")]
            if random.randint(0,1) == 0:
                idx1 = 0
                idx2 = 1
            else:
                idx = 1
                idx2 = 0

            player1 = players[idx1]
            player2 = players[idx2]

            self.available_sticks = self.game_sticks()
            while self.game_over(self.available_sticks):
                self.switch_player(player1, player2)
                print("{} is now playing".format(self.current_player))
                self.available_sticks = self.remaining_sticks(player1.sticks_choice(self.available_sticks), self.available_sticks)
                if self.available_sticks == 0:
                    print("Hey {}! You lost the game!".format(self.current_player))
                    self.game_continue()


    def __init__(self, available_sticks=0, sticks_balance=0):
        self.available_sticks = available_sticks
        self.sticks_balance = sticks_balance
        self.play()


if __name__ == '__main__':
    Game()
