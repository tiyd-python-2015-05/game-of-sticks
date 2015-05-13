from sticks_game import Game
from sticks_game import Player
import sys
import random


class AIPlayer(Player):
    def sticks_choice(self, available_sticks):
        sticks = random.choice([1,2,3])
        if 1 <= sticks <= 3 and sticks <= available_sticks:
            return sticks
        else:
            print("Invalid Selection")
            return self.sticks_choice(available_sticks)


class AIGame(Game):
    def play(self):
        self.welcome()
        while True:
            aiplayer = AIPlayer("Twiga")
            player = Player("Tembo")
            '''
            players = [AIPlayer("Twiga"), Player("Hilde")]
            if random.randint(0,1) == 0:
                idx1 = 0
                idx2 = 1
            else:
                idx1 = 1
                idx2 = 0

            player1 = players[idx1]
            player2 = players[idx2]
            '''
            self.available_sticks = random.randint(10,100)
            print("The game has {} sticks on board".format(self.available_sticks))
            while self.game_over(self.available_sticks):
                self.switch_player(aiplayer, player)
                if isinstance(self.current_player, AIPlayer):
                    self.available_sticks = self.remaining_sticks(aiplayer.sticks_choice(self.available_sticks), self.available_sticks)
                else:
                    print("{} is now playing".format(self.current_player))
                    self.available_sticks = self.remaining_sticks(player.sticks_choice(self.available_sticks), self.available_sticks)
                if self.available_sticks == 0:
                    print("Hey {}! You lost the game!".format(self.current_player))
                    self.game_continue()


    def __init__(self, available_sticks=0, sticks_balance=0):
        self.available_sticks = available_sticks
        self.sticks_balance = sticks_balance
        self.play()


if __name__ == '__main__':
    AIGame()
