from game_of_sticks import *


def test_game_setup():
    p1 = Player(name='Harry')
    p2 = Player(name='Sally')
    game = SticksGame(p1, p2, sticks=100)
    assert game.sticks == 100

def test_player_has_name():
    player1 = Player(name='Harry')
    player2 = Player(name='Sally')
    assert player1.name == 'Harry'
    assert player2.name == 'Sally'
    assert player1 != player2

def test_player_can_choose_num_sticks():
    player1 = Player()
    assert player1.choose(auto=3) == 3

class AutoPlayer(Player):
    def choose(self, auto=3):
        return auto

def test_first_turn_removes_sticks():
    p1 = AutoPlayer()
    p2 = AutoPlayer()
    game = SticksGame(p1, p2, sticks=100)
    game.start()
    assert game.sticks == 97

def test_switch_players():
    p1 = AutoPlayer()
    p2 = AutoPlayer()
    game = SticksGame(p1, p2, sticks=100)
    assert game.current_player == p1
    game.start()
    game.next_turn()
    assert game.current_player == p2
