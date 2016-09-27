
import random


class Game:
    # Should print initial instructions
    # Should create and start turns
    # Add turn score to player's score
    # Should stop when a player reaches 100

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1

    def start(self):
        # Loop until a player has won
        while not self.winner():
            turn = Turn(self.current_player)
            turn.start()
#Fix            print("There are now {} sticks remaining. It is now {}'s turn'".format(self.score
                                                self.current_player))
            self.switch_players()

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

#fix    def winner(self):
        if (self.player1.score < 100 and self.player2.score < 100) \
                or self.player1.score == self.player2.score:
            return None

        if self.player1.score > self.player2.score:
            return self.player1
        else:
            return self.player2


class Turn:
    # While turn is not over
    #   Roll a die
    #   Record result
    #   Tell player result
    #   Ask player if they want to go again if result was not 1

    def __init__(self, player):
        self.score = 0
        self.player = player
        self.over = False
        self.die = Die()

    def record_roll(self, roll):
        if roll == 1:
            self.score = 0
            self.over = True
        else:
            self.score += roll

    def start(self):
        while not self.over:
            self.go()

    def go(self):
        roll = self.die.roll()
        self.record_roll(roll)
        self.player.record_roll(roll)
        if not self.over:
            self.over = not self.player.go_again()


class Player:
    # Should decide whether they want to go again

    def __init__(self, name="Bojangles"):
        self.name = name
        self.score = 0
        self.rolls = []

    def record_roll(self, roll):
        self.rolls.append(roll)

    def __str__(self):
        return self.name


class ComputerPlayer(Player):
    def go_again(self):
        return sum(self.rolls) < 12


class HumanPlayer(Player):
    def record_roll(self, roll):
        super().record_roll(roll)
        print("You rolled a {}.".format(roll))

    def go_again(self):
        go = input("Do you want to go again? ")
        return go.lower()[0] == "y"


class Die:
    def roll(self):
        return random.randint(1, 6)


if __name__ == '__main__':
    p1 = HumanPlayer("Cool Person")
    p2 = ComputerPlayer("Ultron")
    game = Game(p1, p2)
    game.start()
