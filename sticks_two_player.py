class TwoPlayerGame:
    '''Contains the gameplay for a two-person game of sticks'''
    def __init__(self):
        self.player1 = Player(input("Player 1, what is your name?: "))
        self.player2 = Player(input("Player 2, what is your name?: "))
        self.current_player = self.player1
        self.number_of_sticks = 0
        self.winner = None
        self.choice = 0

    def start(self):
        self.get_sticks()
        while self.number_of_sticks > 1:
            self.get_choice()
            self.number_of_sticks = self.number_of_sticks - self.choice
            if self.number_of_sticks != 1:
                print("There are {} sticks left on the board".format(self.number_of_sticks))
            self.switch_players()
        if self.number_of_sticks <= 0:
            print("{} wins".format(self.current_player))
        else:
            self.get_winner()
            print("There is one stick left on the board, {} wins".format(self.winner))

        self.play_again = input("Do you want to play again (Y/N)?").lower()
        if self.play_again == "y":
            self.start()
        else:
            quit()


    def get_choice(self):
        self.usr_choice = input("{}, how many sticks would you like to pick up (1,2,3)? ".format(self.current_player))
        try:
            int(self.usr_choice)
        except:
            print("Not a valid choice")
            self.get_choice()
        self.usr_choice = int(self.usr_choice)
        if self.usr_choice > 0 and self.usr_choice < 4:
            self.choice = self.usr_choice
        else:
            print("Not a valid choice")
            self.get_choice()


    def get_sticks(self):
        self.usr_choice = input("How many sticks would you like to play with? ")
        try:
            int(self.usr_choice)
            self.number_of_sticks = int(self.usr_choice)
        except:
            print("Not a valid choice")
            self.get_sticks()


    def get_winner(self):
        if self.current_player == self.player1:
            self.winner = self.player2
        else:
            self.winner = self.player1


    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

class Player:
    def __init__(self, name="Player__"):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

if __name__ == '__main__':
    game = TwoPlayerGame()
    game.start()
