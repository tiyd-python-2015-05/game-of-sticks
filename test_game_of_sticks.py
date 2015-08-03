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
    game.next_turn()  # start()
    assert game.sticks == 97


def test_switch_players():
    p1 = PlayerThatAlwaysPicksThree()
    p2 = PlayerThatAlwaysPicksThree()
    game = SticksGame(p1, p2, sticks=100)
    assert game.current_player == p1
    # start()
    game.next_turn()
    assert game.current_player == p2
    game.next_turn()
    assert game.current_player == p1
    game.next_turn()
    assert game.current_player == p2


def test_winner():
    p1 = PlayerThatAlwaysPicksThree()
    p2 = PlayerThatAlwaysPicksThree()
    game = SticksGame(p1, p2, sticks=100)
    game.next_turn()  # start()
    game.next_turn()
    game.next_turn()
    game.next_turn()
    assert game.check_winner() is None

    game = SticksGame(p1, p2, sticks=6)
    game.next_turn()  # start()
    assert game.sticks == 3
    print('after 1 turn', game.sticks)
    game.next_turn()
    print('after 2 turns', game.sticks)
    assert game.check_winner() == p1

    game = SticksGame(p1, p2, sticks=9)
    game.next_turn()  # start()
    print('after 1', game.sticks)
    game.next_turn()
    print('after 2', game.sticks)
    game.next_turn()
    print('after 3', game.sticks)
    assert game.check_winner() == p2


def test_invalid_choice_rejected_gracefully():
    p1 = AutoPlayer()
    p2 = AutoPlayer()
    random.seed(10)
    # This should make choices = 3, 1, 2...
    game = SticksGame(p1, p2, sticks=2)
    game.next_turn()  # game.start()
    assert game.sticks == 1


class RepeatingPlayer(Player):
    def __init__(self):
        super().__init__()
        self.choice_sequence = [3, 2, 1]
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
    sticks_history = [100, 97, 94, 92, 90, 89, 88, 85, 82, 80, 78, 77, 76, 73]
    # [97,94,91,89,86,85,82,79,76,74] #PTAP3, Rep x3,3,x3,2,x3,1,x3,3,x3,2
    # [98,95,92,90,89,88,86,83,80] # Auto, Repeat 2,3,3,2,1,1,2,3,3,
    # Repeating**2 [97, 94, 93, 91, 89, 88, 85, 82] # -3,-3,-1,-2,-2,-1,-3
    # game.start()
    score = iter(sticks_history)
    assert game.sticks == next(score)
    for _ in range(len(sticks_history) - 1):
        game.next_turn()
        assert game.sticks == next(score)


def test_auto_game_outcomes_p1_win():
    p1 = RepeatingPlayer()
    p2 = RepeatingPlayer()
    game = SticksGame(p1, p2, sticks=12)
    sticks_history = [12, 9, 6, 4, 2, 1, 0]
    score = iter(sticks_history)
    assert game.sticks == next(score)
    for _ in range(len(sticks_history) - 1):
        game.next_turn()
        assert game.sticks == next(score)
    assert game.check_winner() == p1


def test_auto_game_outcomes_p2_win():
    p1 = RepeatingPlayer()
    p2 = RepeatingPlayer()
    game = SticksGame(p1, p2, sticks=11)
    sticks_history = [11, 8, 5, 3, 1, 0]
    score = iter(sticks_history)
    assert game.sticks == next(score)
    for _ in range(len(sticks_history) - 1):
        game.next_turn()
        assert game.sticks == next(score)
    assert game.check_winner() == p2


def test_play():
    p1 = RepeatingPlayer()
    p2 = RepeatingPlayer()
    game = SticksGame(p1, p2, sticks=12)
    game.play()
    assert game.check_winner() == p1

    p1 = RepeatingPlayer()
    p2 = RepeatingPlayer()
    game = SticksGame(p1, p2, sticks=12)
    game.play()
    assert game.check_winner() == p1


def test_random_c_vs_c_p1_fraction():
    my_session = Session()
    my_session.npc1 = RandomPlayer('Marvin')
    my_session.npc2 = RandomPlayer('R2')
    random.seed()
    wins = ''
    for _ in range(1000):
        winner = my_session.c_vs_c()
        wins = wins + winner.initial
    assert 400 < wins.count('2') < 600


def test_ai_c_vs_c_p1_fraction():
    my_session = Session()
    my_session.sticks = 10
    my_session.npc1 = RandomPlayer('Marvin')
    my_session.npc2 = AIPlayer('R2')
    random.seed()
    wins = ''
    for _ in range(10000):
        winner = my_session.c_vs_c(silent=True)
        wins = wins + winner.initial
    print('Sticks\tTake1\tTake2\tTake3')
    for sticks, dictionary in enumerate(my_session.npc2.hats):
        c = lambda x: dictionary['in'].count(x)
        print('{}\t{}\t{}\t{}'.format(sticks, c(1), c(2), c(3)))
    assert wins.count('2') > 9000
