from sticks import *


def make_game():
    p1 = ComputerPlayer("Ultron")
    p2 = ComputerPlayer("ultron's friend")
    game = Game(p1,p2, False)
    return game


def test_sample():
    assert pdf_sample([1,0,0]) == 1
    assert pdf_sample([0,1,0]) == 2


def test_loser():
    game = make_game()
    game.current_player = game.player1
    game.sticks = 0
    assert game.loser() == game.player1
