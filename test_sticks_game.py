from sticks_game import Game
from sticks_game import Player


def test_remaining_sticks():
    game = Game()
    #assert remaining_sticks(picked_sticks, initial_sticks) == 2
    assert game.remaining_sticks(2, 3) == 1
    assert game.remaining_sticks(4, 10) == 6
