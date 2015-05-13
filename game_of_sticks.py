
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.sticks = 0
        self.pick_sticks = 0

    def start(self):
        self.num_sticks()
        print(self.sticks)
        while self.sticks > 1:
            self.pick_num_sticks()
            self.decrement_sticks()
            self.loser()


    def num_sticks(self):
        print("Welcome to the Game of Sticks!")
        sticks = int(input("How many sticks are on the table initially (10 - 100)? "))
        while sticks < 10 or sticks > 100:
            print ("Please enter a number between 10 and 100.")
            sticks = int(input("How many sticks are on the table initially (10 - 100)? "))
        return sticks


    def pick_num_sticks(self):
        pick_sticks = int(input("How many sticks do you take (1-3)? "))
        while pick_sticks < 1 or pick_sticks > 3:
            print("Please enter a number between 1 and 3.")
            pick_sticks = int(input("How many sticks do you take (1-3)? "))
        return pick_sticks


    def decrement_sticks(self):
        self.sticks -= self.pick_sticks


    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def loser(self):
         if self.total_sticks == 1:
             self.current_player = self.player1
         else:
             self.current_player = self.player2


class Player:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    p1 = Player("Player1")
    p2 = Player("Player2")
    game = Game(p1, p2)
    game.start()
