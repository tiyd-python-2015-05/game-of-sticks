from sticks_two_player import Player, Game

p1 = Player("One")
p2 = Player("Two")
game = Game(p1, p2)

def test_current_player():

    assert game.current_player == p1

    game.switch_players()
    assert game.current_player == p2

    game.switch_players()
    assert game.current_player == p1

def test_game_continues_until_winner():
    game.start()
    assert game.winner is not None

def test_get_winner():
    game.get_winner()
    assert game.winner == "Two"
