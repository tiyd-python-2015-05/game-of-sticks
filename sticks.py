class Game:
    #Display initial instructions
    #asks for players (1 or 2)
    #Creates and starts turn for a player
        #Asks the player how many sticks to pickup

    #Keep a tally of sticks remaining

    #checks for winner/ stops when stick ==0


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

    def make_winner(self):
        # self.switch_player()
        self.winner = self.current_player

    def remove_sticks(self, sticks_taken):
        self.sticks = self.sticks - sticks_taken

    def start(self):
        while True:
            self.number_players = self.player1.setup()
            self.sticks = self.player1.initial_sticks()
            self.player1.name = self.player1.input_name()
            self.player2.name = self.player2.input_name()
            while not self.game_over:
                sticks_taken = self.current_player.num_of_sticks()
                self.remove_sticks(sticks_taken)
                print("There are now {} sticks left".format(self.sticks))
                self.switch_player()
                self.game_over_check()
            self.make_winner()
            print("{} wins!".format(self.winner.name))
            if self.player1.play_again():
                self.start() # need to fix - already knows inputs
            else:
                break

class Player:
    def __init__(self, name='Bob'):
        self.name = name


class HumanPlayer(Player):
    def setup(self):
        print("""
              Welcome to the Game of Sticks. In the Game of Sticks
              there is a heap of sticks on a board. On your turn,
              pick up 1 to 3 sticks. The one who has to pick the final stick
              will be the loser.""")

        players = input("How many players? (pick 2)\n>")

        try:
            int(players)

            if players not in range(1,3):
                return self.setup
            else:
                return players

        except ValueError:
            print("Invalid Error")
            return self.setup()

    def input_name(self):
        player = input("{}, What is your name?\n> ".format(self.name))
        return player

    def num_of_sticks(self):
        pick_up_sticks = input("{}, How many sticks 1 - 3? ".format(self.name))

        try:
            s = int(pick_up_sticks)

            if s not in range(1,4):
                return self.num_of_sticks()

            else:
                return s

        except ValueError:
            print("Invalid Error")
            return self.num_of_sticks()


    def initial_sticks(self):
        total_sticks = input("""How many sticks do you want to start with?
            Choose between 10 - 100  """)

        try:
            s = int(total_sticks)

            if s not in range(10,101):
                return self.initial_sticks
            else:
                return s

        except ValueError:
            print("Invalid Error")
            return self.initial_sticks()

    def play_again(self):
        again = input("Would you like to play again? Y/n? \n>").lower()

        if again == "y":
            return True
        else:
            return False
        # else:
        #     return False
    # def player_name():
    #choose 1 or 2 player game
    #     input(What is your)#inputs the number of sticks
    #Ask how many sticks to play with
    #Sets number of sticks to input "How many sticks do you want to pick up"
    #choose to go again

if __name__ == '__main__':
    p1 = HumanPlayer("Player1")
    p2 = HumanPlayer("Player2")
    game = Game(p1, p2)
    game.start()
