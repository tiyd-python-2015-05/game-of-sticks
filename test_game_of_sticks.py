from game_of_sticks import *


def test_game_setup():
    game = SticksGame(sticks=100)
    assert game.sticks == 100
