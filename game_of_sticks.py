import random

class SticksGame:
    def __init__(self, p1, p2, sticks=100):
        self.sticks = sticks
        self.current_player = p1
        self.player_a = p1
        self.player_b = p2

    def play(self):
        while self.check_winner() is None:
            self.next_turn()

    def try_removing_sticks(self):
        turn = Turn(self.current_player)
        if self.sticks >= turn.removed_sticks:
            self.sticks -= turn.removed_sticks
            return
        else:
            return self.try_removing_sticks()
    #def start(self):
    #    self.try_removing_sticks()
    def next_turn(self):
        if self.current_player == self.player_a:
            self.current_player = self.player_b
            #turn = Turn(self.current_player)
            self.try_removing_sticks()
        elif self.current_player == self.player_b:
            self.current_player = self.player_a
            #turn = Turn(self.current_player)
            self.try_removing_sticks()
    def check_winner(self):
        print('checking winner...')
        if self.sticks == 0:
            return self.current_player
        return None

    def other(self):
        print("it's the other guy")
        if self.current_player is self.player_a:
            print(self.player_b)
            return self.player_b
        return self.player_a
        print(self.player_a)

class Player:
    def __init__(self, name='Sam'):
        self.name = name
    def __repr__(self):
        return '{}: {}'.format(self.__class__, self.name)
    def choose(self, auto=None):
        if auto is not None:
            return auto
        return random.randint(1,3)

class Turn:
    def __init__(self, player):
        self.player = player
        self.removed_sticks = player.choose()
