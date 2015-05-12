from game_of_sticks import *


def test_game_setup():
    game = SticksGame(sticks=100)
    assert game.sticks == 100

def test_player_has_name():
    player1 = Player('Harry')
    player2 = Player(name='Sally')
    assert player1.name == 'Harry'
    assert player2.name == 'Sally'
    assert player1 != player2

def test_player_can_choose_num_sticks():
    player1 = Player()
    assert player1.choose(auto=3) == 3


def test_turn_removes_sticks():
    assert False
