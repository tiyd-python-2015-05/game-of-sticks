from sticks_game import Game
from sticks_game import Player




def test_choice_is_integer():
    game = Game()
    assert game.is_integer('a4') == False
    assert game.is_integer(2.0) == False
    assert game.is_integer(183)


def test_choice_is_valid():
    game = Game()
    assert game.is_valid_selection(4, 6) == False
    assert game.is_valid_selection(2, 1) == False
    assert game.is_valid_selection(0, 3) == False
    assert game.is_valid_selection(2, 20)
    assert game.is_valid_selection(1, 7)


def test_remaining_sticks():
    game = Game()
    #assert remaining_sticks(picked_sticks, initial_sticks) == 2
    assert game.remaining_sticks(2, 3) == 1
    assert game.remaining_sticks(4, 10) == 6
