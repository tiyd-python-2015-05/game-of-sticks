

class SticksGame:
    def __init__(self, p1, p2, sticks=100):
        self.sticks = sticks
        self.current_player = p1
        self.player_a = p1
        self.player_b = p2
    def start(self):
        turn = Turn(self.current_player)
        self.sticks -= turn.removed_sticks
    def next_turn(self):
        if self.current_player == self.player_a:
            self.current_player = self.player_b
            turn = Turn(self.current_player)
            self.sticks -= turn.removed_sticks
            self.check_win()
        if self.current_player == self.player_a:
            self.current_player = self.player_b
            turn = Turn(self.current_player)
            self.sticks -= turn.removed_sticks
            self.check_win()
    def check_win(self):
        return True


class Player:
    def __init__(self, name='Sam'):
        self.name = name
    def choose(self, auto=None):
        if auto is not None:
            return auto
        return something_else

class Turn:
    def __init__(self, player):
        self.player = player
        self.removed_sticks = player.choose()
