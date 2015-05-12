from sticks import Game, Human, Computer

import nose


def test_set_remove_sticks():
    game = Game()

    game.set_num_sticks(5)
    assert game.sticks == 5

    game.remove_sticks(1)
    assert game.sticks == 4

def test_set_switch_players():
    player1 = Human('Elf')
    player2 = Computer()
    game = Game()
    game.set_players(player1, player2)

    assert game.players[0] is player1
    assert game.players[1] is player2

    if game.current_player is not player1:
        game.switch_player()
        assert game.current_player is player1

    if game.current_player is not player2:
        game.switch_player()
        assert game.current_player is player2

def test_game_is_done():
    game = Game()
    game.set_num_sticks(5)
    assert not game.is_done()
    game.set_num_sticks(0)
    assert game.is_done()

def test_game_status():
    game = Game()
    game.set_num_sticks(5)
    player1 = Human('Alf')
    player2 = Human('Bertram')
    game.set_players(player1, player2)
    game.remove_sticks(2)
    assert list(game.status()) == [game.current_player.name, 2, 3]

def test_turn():
    game = Game()
    game.set_num_sticks(5)
    player1 = Computer()
    player2 = Computer()
    game.set_players(player1, player2)
    game.turn()
    assert 2 <= game.sticks <=4


if __name__ == '__main__':
    nose.main()
