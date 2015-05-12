class Game:
#Displays initial instructions
#Asks for number of players (1 or 2)
#Asks for number of sticks
#Sets number of sticks to choice
#Creates and starts turn
#   Asks player for stick choice
#Keep of tally of sticks remaining
#Checks winner/Stops when sticks reach 0
#Switch player
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.sticks = 100
        self.game_over = False
        self.current_player = self.player1
        self.winner = None
        self.number_players = 2


    def game_over_check(self):
        if self.sticks <= 0:
            self.game_over = True


    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def decrement_sticks(self, player_choice):
        self.sticks -= player_choice


    def make_winner(self):
#        self.switch_player()
# fixed logic, fix tests
        self.winner = self.current_player


    def start(self):
        while True:
            self.number_players = self.player1.initial_setup()
            self.sticks = self.player1.initial_sticks()
            self.player1.name = self.player1.input_name()
            self.player2.name = self.player2.input_name()
            while not self.game_over:
#                print(self.game_over)
                sticks_taken = self.current_player.number_of_sticks()
                self.decrement_sticks(sticks_taken)
                print("There are now {} sticks left.".format(self.sticks))
                self.switch_player()
                self.game_over_check()
            self.make_winner()
            print("Congratulations {}".format(self.winner.name))
            if not self.player1.play_again():
                break






#class Turn:
#    pass
#Asks player how many sticks they want to choose
#Switches current player

class Player:
    def __init__(self, name="Arlo"):
        self.name = name

#Has a name/inputs name
#Chooses 1 or 2 player game
#Chooses number of sticks to start
#Chooses number of sticks on her turn
#Chooses to go again

class HumanPlayer(Player):
    def initial_setup(self):
        print("""WELCOME TO THE GAME OF STICKS. In the Game of Sticks there is
        a heap of sticks on a board. On their turn, each player picks up 1 to 3
        sticks. The one who has to pick the final stick will be the loser.""")
        try:
            players = int(input("How many human players? (1 or 2 please): "))
            if players != 1 and players != 2:
                return self.initial_setup()
            else:
                return players
        except ValueError:
            print("Numbers only!!")
            return self.initial_setup()

    def initial_sticks(self):
        try:
            total_sticks = int(input("""How many sticks to start with?
            (between 10 and 100):"""))
#fix error
            if total_sticks not in range(10,101):
                return self.initial_sticks()
            else:
                return int(total_sticks)
        except ValueError:
            print("Numbers only!!")
            return self.initial_sticks()

    def input_name(self):
        return input("{}, What is your name?: ".format(self.name))

    def number_of_sticks(self):
        try:
            num_sticks = int(input("{}, how many sticks do you take? (1, 2, or 3): ".format(self.name)))
            if num_sticks not in [1, 2, 3]:
                return self.number_of_sticks
            else:
                return int(num_sticks)
        except ValueError:
            print("Numbers only!!")
            return self.number_of_sticks
    def play_again(self):
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            return True
        else:
            return False

if __name__ == '__main__':
    p1 = HumanPlayer("Player 1")
    p2 = HumanPlayer("Player 2")
    game = Game(p1, p2)
    game.start()
