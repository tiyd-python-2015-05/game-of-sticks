from game_of_sticks import SticksGame, Player, AIPlayer


def test_SticksGame_has_pile():
    game = SticksGame("p1", "p2")
    assert game.pile == 20


class TestGame(SticksGame):
    def play_again(self):
        return None


def test_SticksGame_ends():
    game = TestGame("p1", "p2")
    assert not game.winner() == "p1"
    assert not game.winner() == "p2"
    game.pile = 0
    assert game.winner() == "p1"
    assert not game.winner() == "p2"


def test_SticksGame_displays_pile():
    game = SticksGame("p1", "p2")
    assert game.display_pile() == "Pile contains 20 sticks."
    game.pile = 3
    assert game.display_pile() == "Pile contains 3 sticks."


def test_SticksGame_switches_players():
    game = SticksGame("p1", "p2")
    game.switch_players()
    assert game.current_player == "p2"
    game.switch_players()
    assert game.current_player == "p1"


class TestPlayer(Player):
    def __init__(self):
        super().__init__()
        self.check = 2

    def pick_up(self, remaining):
        if self.check in [1, 2, 3]:
            self.sticks = self.check


def test_player_decides_how_many_sticks_to_take():
    player = TestPlayer()
    assert player.sticks == 0
    player.pick_up(1)
    assert player.sticks == 2
    player.check = 1
    player.pick_up(1)
    assert player.sticks == 1
    player.check = 3
    player.pick_up(1)
    assert player.sticks == 3
    player.check = 4
    player.pick_up(1)
    assert not player.sticks == 4


def test_SticksGame_removes_sticks_from_pile():
    player = TestPlayer()
    game = SticksGame(player, player)
    assert game.pile == 20
    game.remove()
    assert game.pile == 18
    player.check = 4
    game.remove()
    assert game.pile == 18


def test_SticksGame_goes_until_winner():
    p1 = TestPlayer()
    p2 = TestPlayer()
    game = TestGame(p1, p2)
    game.start()
    print(game.pile)
    print(game.current_player)
    assert game.winner() is not None


def test_AI_test_game():
    ai = AIPlayer()
    ai.pick_up(17)
    ai.pick_up(12)
    ai.pick_up(3)
    ai.integrate_win()
    assert len(ai.choices(17)) == 4
    ai.pick_up(17)
    ai.pick_up(10)
    ai.integrate_win()
    assert len(ai.choices(17)) == 5
    assert len(ai.choices(10)) == 4
    ai.pick_up(17)
    ai.pick_up(10)
    ai.win_check()
    assert len(ai.choices(17)) == 5
    assert len(ai.choices(10)) == 4


def test_AI_choices():
    """An initial player should have 1, 2, 3 as choices for all numbers."""
    ai = AIPlayer()
    assert ai.choices(13) == [1, 2, 3]
