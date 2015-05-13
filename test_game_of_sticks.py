from game_of_sticks import *


def test_player_has_name():
    player1 = Player()
    assert player1.name == "Arlo"


def test_game_over_check():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    assert not game1.game_over

    game1.sticks = 0
    game1.game_over_check()
    assert game1.game_over

    game1.sticks = 50
    game1.game_over_check()


def test_switch_players():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    assert game1.current_player == p1
    game1.switch_player()
    assert game1.current_player == p2
    game1.switch_player()
    assert game1.current_player == p1


def test_game_gets_winner():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    assert game1.winner is None
    game1.game_over == True
    game1.make_winner()
    assert game1.winner == p1


def test_decrement_sticks():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    game1.sticks = 100
    game1.decrement_sticks(3)
    assert game1.sticks == 97


def test_decrement_sticks_and_game_over():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    assert not game1.game_over
    game1.game_over_check()
    assert not game1.game_over
    game1.decrement_sticks(100)
    assert game1.sticks == 0
    game1.game_over_check()
    assert game1.game_over


def test_reset_game_values():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    game1.sticks = 80
    assert game1.sticks == 80
    game1.winner = "Josh"
    game1.reset_game_values()
    assert game1.sticks == 100
    assert game1.winner = None


class OnePlayer(Player):
    def __init__(self):
        super().__init__()

    def initial_setup(self):
        return 1

# def test_player_settings():
#     p1 = OnePlayer()
#     p2 = OnePlayer()
#     game1 = Game(p1, p2)
#     assert
#     p1.initial_setup()
