from sticks_game import Game


def test_choice_is_integer():
    assert is_integer('a4') == False
    assert is_integer(2.0) == False
    assert is_integer(183)


def test_choice_is_valid():
    assert is_valid_selection(4, 6) == False
    assert is_valid_selection(2, 1) == False
    assert is_valid_selection(0, 3) == False
    assert is_valid_selection(2, 20)
    assert is_valid_selection(1, 7)


def test_remaining_sticks():
    #assert remaining_sticks(picked_sticks, initial_sticks) == 2
    assert remaining_sticks(2, 3) == 1
    assert remaining_sticks(4, 10) == 6
