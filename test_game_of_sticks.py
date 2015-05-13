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
    assert game1.winner == None


def test_display_sticks():
    p1 = Player()
    p2 = Player()
    game1 = Game(p1, p2)
    game1.sticks = 20

def test_create_computer_player():
    p1 = ComputerPlayer()
    p1.name = p1.input_name()
    assert p1.name == "Numbotronic 5000"
#    assert p1.number_of_sticks(12) == 3
    assert p1.odds_hat[1] == [1, 2, 3]
    assert p1.odds_hat[99] == [1, 2, 3]
    assert p1.odds_holder[1] == []
    assert p1.odds_holder[75] == []

def test_increment_odds_holder():
    p1 = ComputerPlayer()
    assert p1.odds_holder[5] == []
    p1.increment_odds_holder(5, 1)
    assert p1.odds_holder[5] == [1]

def test_add_odds_holder_to_hat():
    p1 = ComputerPlayer()
    assert p1.odds_holder[7] == []
    p1.increment_odds_holder(7, 1)
    assert p1.odds_holder[7] == [1]
    p1.add_odds_holder_to_hat()
    assert (p1.odds_hat)[7] == [1, 2, 3, 1]

def test_sub_odds_holder_from_hat():
    p1 = ComputerPlayer()
    assert p1.odds_holder[9] == []
    p1.increment_odds_holder(9, 1)
    assert p1.odds_holder[9] == [1]
    p1.sub_odds_holder_from_hat()
    assert (p1.odds_hat)[9] == [2, 3]



#class OnePlayer(Player):
#    def __init__(self):
#        super().__init__()
#
#    def initial_setup(self):
#        return 1

# def test_player_settings():
#     p1 = OnePlayer()
#     p2 = OnePlayer()
#     game1 = Game(p1, p2)
#     assert
#     p1.initial_setup()
