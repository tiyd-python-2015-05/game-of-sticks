import random

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
    def __init__(self, player1, player2, num_player):
        self.player1 = player1
        self.player2 = player2
        self.num_player = num_player
        self.sticks = 100
        self.game_over = False
        self.current_player = self.player1
        self.winner = None


    def initial_setup(self):
        print("WELCOME TO THE GAME OF STICKS. In the Game of Sticks there is " \
        "a heap of sticks on a board. On their turn, each player picks up 1 to"\
        " 3 sticks. The one who has to pick the final stick will be the " \
        "loser. GOOD LUCK. \n")


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
        self.winner = self.current_player
        print("Congratulations {}!!  You win!!!".format(self.winner.name))


    def reset_game_values(self):
        self.sticks = 100
        self.game_over = False
        self.current_player = self.player1
        self.winner = None


    def display_sticks(self):
        if self.sticks > 0:
            print("There are {} sticks left.".format(self.sticks), end="  ")
            if self.sticks > 20:
                print("}}" + "|"*20)
            else:
                print("|" * self.sticks)


    def start(self):
        while True:
            self.initial_setup()
            self.sticks = self.player1.initial_sticks()
            if self.player1.name == "Player 1":
                self.player1.name = self.player1.input_name()
            if self.player2.name == "Player 2":
                self.player2.name = self.player2.input_name()
            while not self.game_over:
                sticks_taken = self.current_player.number_of_sticks(self.sticks)
                self.decrement_sticks(sticks_taken)
                self.display_sticks()
                self.switch_player()
                self.game_over_check()
            self.make_winner()
            self.reset_game_values()
            if self.num_player == 1:
                if self.winner == self.player2:
                    self.player2.add_odds_holder_to_hat()
                if self.winner == self.player1:
                    self.player2.sub_odds_holder_from_hat()
            if not self.player1.play_again():
                break


class Player:
    def __init__(self, name="Arlo"):
        self.name = name

#Has a name/inputs name
#Chooses 1 or 2 player game
#Chooses number of sticks to start
#Chooses number of sticks on her turn
#Chooses to go again

class HumanPlayer(Player):

    def initial_sticks(self):
        try:
            print("How many sticks to start with?", end=" ")
            total_sticks = int(input("(between 10 and 100): "))
            if total_sticks not in range(10,101):
                return self.initial_sticks()
            else:
                return int(total_sticks)
        except ValueError:
            print("Numbers only!!")
            return self.initial_sticks()


    def input_name(self):
        return input("{}, What is your name?: ".format(self.name))


    def number_of_sticks(self, sticks_left):
        try:
            num_sticks = int(input("{}, how many sticks do you take? (1, 2, or 3): ".format(self.name)))
            if num_sticks not in [1, 2, 3]:
                print("You can only pick 1, 2, or 3 sticks.")
                return self.number_of_sticks(sticks_left)
            else:
                return num_sticks
        except ValueError:
            print("Numbers only!!")
            return self.number_of_sticks(sticks_left)


    def play_again(self):
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            return True
        else:
            return False


class ComputerPlayer(Player):
    #computer player creates dictionary with keys 1 to 100 and with list of values 1to3
    #for each game, saves dict with number and choice for each turn
    #if win, appends choice to key: value list
    #if lose, takes 1 instance of choice from key value list
    def __init__(self, name="Numbotronic 5000",odds_hat={i: [1, 2, 3] for i in
                range(1,100)}, odds_holder={i: [] for i in range(1,100)}):
        self.name = name
        self.odds_hat = odds_hat
        self.odds_holder = odds_holder

#    def initialize_dict(self):
#        self.odds_hat = {i: [1, 2, 3] for i in range(1,100)}

    def input_name(self):
        return "Numbotronic 5000"

    def increment_odds_holder(self, sticks_left, choice):
        (self.odds_holder[sticks_left]).append(choice)

    def number_of_sticks(self, sticks_left):
        if len(self.odds_hat[sticks_left]) > 0:
            choice = random.choice(self.odds_hat[sticks_left])
        else:
            choice = random.choice([1, 2, 3])
        print("{} takes {}.".format(self.name, choice))
        self.increment_odds_holder(sticks_left, choice)
        return choice

    def add_odds_holder_to_hat(self):
        for i, j in self.odds_holder.items():
            for a in j:
                (self.odds_hat[i]).append(a)


    def sub_odds_holder_from_hat(self):
        for i, j in self.odds_holder.items():
            for a in j:
                (self.odds_hat[i]).remove(a)





def one_or_two_player():
    try:
        players = int(input("How many human players? (1 or 2 please): "))
        if players != 1 and players != 2:
            return one_or_two_player()
        else:
            return players
    except ValueError:
        print("Numbers only!!")
        return one_or_two_player()


if __name__ == '__main__':
    num_player = one_or_two_player()
    if num_player == 1:
        p1 = HumanPlayer("Player 1")
        p2 = ComputerPlayer("Player 2")
    else:
        p1 = HumanPlayer("Player 1")
        p2 = HumanPlayer("Player 2")
    game = Game(p1, p2, num_player)
    game.start()
