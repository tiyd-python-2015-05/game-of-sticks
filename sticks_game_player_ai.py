from sticks_game import Game
from sticks_game import Player
import sys
import random


class AIPlayer(Player):
    def __init__(self, name="Sungura", hat=0):
        super().__init__(name)
        self.hat = hat


    def sticks_choice(self, available_sticks):
        sticks = random.choice([1,2,3])
        if 1 <= sticks <= 3 and sticks <= available_sticks:
            return sticks
        else:
            print("Invalid Selection")
            return self.sticks_choice(available_sticks)


class AIGame(Game):

    def game_sticks(self):
        return random.randint(10,100)


    def play(self):
        self.welcome()
        while True:
            aiplayer = AIPlayer("Twiga")
            player = Player("Tembo")
            self.available_sticks =self.game_sticks()
            print("The game has {} sticks on board".format(self.available_sticks))
            while self.game_over(self.available_sticks):
                self.switch_player(aiplayer, player)
                if not isinstance(self.current_player, AIPlayer):
                    print("{} is now playing".format(self.current_player))
                self.available_sticks = self.remaining_sticks(self.current_player.sticks_choice(self.available_sticks),
                                            self.available_sticks)
                if self.available_sticks == 0:
                    print("Hey {}! You lost the game!".format(self.current_player))
                    self.game_continue()


if __name__ == '__main__':
    #AIGame()
    player = AIPlayer()
    print(player)
