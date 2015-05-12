from game_of_sticks import *


def test_game_setup():
    p1 = Player(name='Harry')
    p2 = Player(name='Sally')
    game = SticksGame(p1, p2, sticks=100)
    assert game.sticks == 100

def test_player_has_name():
    player1 = Player(name='Harry')
    player2 = Player(name='Sally')
    assert player1.name == 'Harry'
    assert player2.name == 'Sally'
    assert player1 != player2

def test_player_can_choose_num_sticks():
    player1 = Player()
    assert player1.choose(auto=3) == 3

class AutoPlayer(Player):
    pass

class PlayerThatAlwaysPicksThree(Player):
    def choose(self):
        return 3


def test_first_turn_removes_sticks():
    p1 = PlayerThatAlwaysPicksThree()
    p2 = PlayerThatAlwaysPicksThree()
    game = SticksGame(p1, p2, sticks=100)
    game.start()
    assert game.sticks == 97

def test_switch_players():
    p1 = PlayerThatAlwaysPicksThree()
    p2 = PlayerThatAlwaysPicksThree()
    game = SticksGame(p1, p2, sticks=100)
    assert game.current_player == p1
    game.start()
    game.next_turn()
    assert game.current_player == p2

def test_winner():
    p1 = PlayerThatAlwaysPicksThree()
    p2 = PlayerThatAlwaysPicksThree()
    game = SticksGame(p1, p2, sticks=100)
    game.start()
    game.next_turn()
    game.next_turn()
    game.next_turn()
    assert game.check_winner() is None

    game = SticksGame(p1, p2, sticks=6)
    game.start()
    print('after start', game.sticks)
    game.next_turn()
    print('after next turn', game.sticks)
    assert game.check_winner() == p1

    game = SticksGame(p1, p2, sticks=9)
    game.start()
    print('after start', game.sticks)
    game.next_turn()
    print('after next turn', game.sticks)
    game.next_turn()
    print('after next next turn', game.sticks)
    assert game.check_winner() == p2

def test_invalid_choice_rejected_gracefully():
    p1 = AutoPlayer()
    p2 = AutoPlayer()
    random.seed(10)
    # This should make choices = 3, 1, 2...
    game = SticksGame(p1, p2, sticks=2)
    game.start()
    assert game.sticks == 1


class RepeatingPlayer(Player):
    def __init__(self):
        super().__init__()
        self.choice_sequence = [3,2,1]
        self.index = 0
    def choose(self):
        if self.index > 2:
            self.index = 0
        self.index += 1
        return self.choice_sequence[self.index - 1]

def test_repeating_player():
    p1 = RepeatingPlayer()
    p2 = RepeatingPlayer()
    game = SticksGame(p1, p2, sticks=100)
    game.start()
    sticks_history = [97, 94, 92, 90, 89, 88, 85, 82, 81]
    score = iter(sticks_history)
    assert game.sticks == next(score)
    for _ in range(len(sticks_history)):
        game.next_turn()
        assert game.sticks == next(score)



def test_auto_game_outcomes():
    assert False
