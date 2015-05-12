from sticks import Game, Human, Computer
from hard_mode import HardComputer

import os
import random

class Talker:

    def __init__(self):
        self.game = Game()
        self.get_names()
        self.play()

    def get_players(self):
        number = input('Single Player? [y]es or [n]o: ')

        if number.lower()[0] in 'yn':
            return number.lower()[0] == 'y'
        else:
            print('Try again!  Answer [yes] or [no].')
            number = self.get_players(self)

    def get_names(self):

        os.system('clear')
        players = []

        if not self.get_players():
            players.append(input('Enter Player 1\'s name: '))
            players.append(input('Enter Player 2\'s name: '))

        else:
            players.append(Human(input('Enter your name: ')))
            players.append(self.set_mode())

        self.game.set_players(*players)
        os.system('clear')

    def set_mode(self):
        mode = input('What mode? [E]asy [H]ard [U]nicron: ')
        mode = mode.lower()[0]
        if mode in 'ehu':
            if mode == 'e':
                return Computer()
            if mode == 'h':
                return HardComputer()
            if mode == 'u':

                new_game = Game()
                unicron1 = HardComputer('Unicron')
                unicron2 = HardComputer('Unicron')

                new_game.set_players(unicron1, unicron2)
                wins = {unicron1:0, unicron2:0}
                for _ in range(1000):
                    wins[self.quick_play(new_game)] += 1

                return max(wins, key=lambda x: x[1])


    def get_sticks(self):
        number = input("How many sticks are on the table (10-100)? ")
        if number.isdigit():
            if number not in list(range(10, 101)):
                number = self.get_sticks()
        else:
            number = self.get_sticks()

        return number

    def quick_play(self, game):
        game.start(random.randint(10,101))

        while not game.is_done():
            game.turn()
            game.switch_player()

        game.current_player.finish() # learn
        game.current_player.reset() # get ready for next round
        game.switch_player()
        game.current_player.reset()

        game.switch_player()
        return game.current_player


    def play(self):
        self.game.start(self.get_sticks())
        self.loop()

        while self.play_again():
            self.game.start(self.get_sticks())
            self.loop()

    def play_again(self):
        yes_no = input("Would you like to play again? [Y]es or [N]o: ")
        if yes_no.lower()[0] in 'yn':
            os.system('clear')
            return yes_no.lower()[0] == 'y'
        else:
            return self.play_again()

    def update(self, *args):
        os.system('clear')
        print("{} took {} sticks. {} left!".format(*args))

    def loop(self):

        while not self.game.is_done():

            self.game.turn()
            self.update(*self.game.status())
            self.game.switch_player()

        self.winner(self.game.current_player)

        if isinstance(self.game.current_player, HardComputer):
            self.game.current_player.finish()
            self.game.current_player.reset()

    def winner(self, player):
        print("{} won the game!".format(player.name))


if __name__ == '__main__':
    talker = Talker()
