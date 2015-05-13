import random


class Game:
    def __init__(self):
        self.players = []

    def start(self, sticks):
        self.sticks = sticks
        self.removed_sticks = 0

    def set_players(self, *players):
        self.players = list(players)
        self.current_player = random.choice(self.players)

    def set_num_sticks(self, num):
        self.sticks = num

    def switch_player(self):
        if self.current_player is self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def is_done(self):
        return self.sticks == 0

    def remove_sticks(self, num):
        self.sticks -= num
        self.removed_sticks = num

    def turn(self):
        self.remove_sticks(self.current_player.turn(self.sticks))

    def status(self):
        return self.current_player.name, self.removed_sticks, self.sticks


class Player:
    def __init__(self, name):
        self.name = name


class Human(Player):

    def turn(self, sticks):
        num = input('How many sticks do you take (1-3)? ')

        if num.strip().isdigit():
            num = int(num)
        else:
            print('Invalid choice! Try again.')
            return self.turn(sticks)

        if 0 < num < 4 and sticks - num >= 0:
                return num
        else:
            print('Invalid choice! Try again.')
            return self.turn(sticks)


class Computer(Player):

    def __init__(self, name='Starscream'):
        super().__init__(name)

    def turn(self, sticks):
        num = random.randint(1, 3)
        while not (0 < num < 4 and sticks - num >= 0):
            num = random.randint(1, 3)
        return num
