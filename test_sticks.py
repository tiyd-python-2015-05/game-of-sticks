from sticks import *

def test_turn():
    assert turn('player1') == 'player1'
    assert turn('player2') == 'player2'

def test_switch_players():
    assert switch_players('player1') == 'player2'
    assert switch_players('player2') == 'player1'

def test_is_choice_valid():
    assert is_choice_valid('3',5)
    assert not is_choice_valid('3',2)
    assert not is_choice_valid('a',2)
    assert not is_choice_valid('4',2)
