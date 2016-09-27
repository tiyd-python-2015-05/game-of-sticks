from pig import Die, Player, Turn, Game
import random


def test_die_rolling():
    die = Die()
    rolls = [die.roll() for _ in range(100)]
    for i in [1, 2, 3, 4, 5, 6]:
        assert i in rolls


def test_turn_collect_rolls():
    player = Player()
    turn = Turn(player)
    assert turn.score == 0

    turn.record_roll(3)
    assert turn.score == 3

    turn.record_roll(5)
    assert turn.score == 8


def test_turn_score_is_zero_on_roll_of_one():
    player = Player()
    turn = Turn(player)
    turn.score = 10

    turn.record_roll(1)
    assert turn.score == 0


def test_player_has_initial_score_of_zero():
    player = Player()
    assert player.score == 0


def test_game_winner():
    p1 = Player()
    p2 = Player()
    game = Game(p1, p2)
    p1.score = 90
    p2.score = 101
    assert game.winner() == p2


def test_current_player():
    p1 = Player()
    p2 = Player()
    game = Game(p1, p2)

    assert game.current_player == p1

    game.switch_players()
    assert game.current_player == p2

    game.switch_players()
    assert game.current_player == p1


def test_turn_ends_on_a_roll_of_one():
    player = Player()
    turn = Turn(player)

    assert not turn.over

    turn.record_roll(1)

    assert turn.over


class TestPlayer(Player):
    def __init__(self):
        super().__init__()
        self._go_again = False

    def go_again(self):
        return self._go_again


class StopAtThreePlayer(Player):
    def __init__(self):
        super().__init__()

    def go_again(self):
        return len(self.rolls) < 3


def test_turn_repeats_until_player_stops():
    # This should result in a rolls of [2, 4, 4].
    random.seed(100)

    player = StopAtThreePlayer()
    turn = Turn(player)
    turn.start()
    assert turn.over
    assert turn.player.rolls == [2, 4, 4]


def test_turn_tells_player_roll():
    # This should result in a roll of 4.
    random.seed(0)

    player = TestPlayer()
    turn = Turn(player)
    turn.go()
    assert player.rolls == [4]


def test_game_goes_until_there_is_a_winner():
    random.seed()
    p1 = StopAtThreePlayer()
    p2 = TestPlayer()
    game = Game(p1, p2)

    game.start()
    assert game.winner() is not None
