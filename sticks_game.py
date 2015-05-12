
class Player:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return "Player: {}".format(self.name)


class Game:

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


    def play(self):
        while True:
            get_sticks = int(input("How many sticks are there on the table (10-100)? "))
            sticks = int(input("How many sticks do you take? "))
            if self.is_valid_selection(sticks, get_sticks):
                if self.remaining_sticks(sticks, get_sticks) == 0:
                    print("Done")


if __name__ == '__main__':
    player1 = Player("Sovello")
    player2 = Player("Hilde")

    game = Game()
    #game.play()
