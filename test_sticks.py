from stick import *

def test_player_name():
    player1 = Player()
    assert player1.name == "Bob"

def test_game_over_check():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    game1.sticks = 0
    assert not game1.game_over

    game1.sticks = 0
    game1.game_over_check()
    assert game1.game_over

def test_switch_player():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)

    assert game1.current_player == p1

    game1.switch_player()
    assert game1.current_player == p2

def remove_sticks():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    game1.sticks = 100
    game1.remove_sticks(3)
    assert game1.sticks == 97

def test_make_winner():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)

    assert game1.winner == None
    game1.game_over = True
    game1.make_winner()
    assert game1.winner == p1
