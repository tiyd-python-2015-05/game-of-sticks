from ttt import *

def test_board_creation():
    p1 = Player(name='1', mark='X')
    p2 = Player(name='2', mark='O')

    board = Board(player1=p1, player2=p2)
    assert board.list_available() == list(range(9))
    assert board.won == None
    assert board.done == False
    assert board.state == '_'*9

def test_player_creation_choose():
    p2 = Player(name='2', mark='O')
    random.seed(0)
    assert p2.choose() == (6,'O')

def test_list_marks():
    p1 = Player(name='1', mark='X')
    p2 = Player(name='2', mark='O')
    random.seed(5)

    board = Board(player1=p1, player2=p2)
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [4]
    assert board.list_marks('O') == []
    assert board.list_available() == [i for i in range(9) if i != 4]
    board.mark_slot(p2.choose())
    assert board.list_marks('X') == [4]
    assert board.list_marks('O') == [5]
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [4,8]
    assert board.list_marks('O') == [5]
    board.mark_slot(p2.choose())
    assert board.list_marks('X') == [4,8]
    assert board.list_marks('O') == [0,5]
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [4,7,8]
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [3,4,7,8]
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [0,3,4,7,8]
    board.mark_slot(p1.choose())
    assert board.list_marks('X') == [0,2,3,4,7,8]
    board.mark_slot(p1.choose())

    assert board.list_marks('X') == [0,1,2,3,4,7,8]
    board.mark_slot(p1.choose())
    # assert board.list_marks('X') == [0,1,2,3,4,7,8]
    # board.mark_slot(p1.choose())
    # assert board.list_marks('X') == [1,2,3,4,7,8]

def test_go_x_turns():
    p1 = Player(name='1', mark='X')
    p2 = Player(name='2', mark='O')
    random.seed(5)

    board = Board(player1=p1, player2=p2)
    assert board.state == '_________'
    assert board.current_player == p1
    board.go(1)
    assert board.current_player == p2
    assert board.state == '____X____'
    board.go(1)
    assert board.current_player == p1
    assert board.state == '____X_O__'
    board.go(5)
    assert board.current_player == p2
    assert board.state == 'O_X_XXOOX'
    board.go(1)
    assert board.current_player == p1
    assert board.state == 'OOX_XXOOX'
    board.go(1)
    # player doesn't switch on last turn
    assert board.current_player == p1
    assert board.state == 'OOXXXXOOX'
    # player doesn't switch after last turn, state doesn't change
    board.go(1)
    assert board.current_player == p1
    assert board.state == 'OOXXXXOOX'


def test_win_lose_or_none():
    p1 = Player(name='1', mark='X')
    p2 = Player(name='2', mark='O')
    board = Board(player1=p1, player2=p2)

    board.state = 'XXOOOXXXO'
    assert board.winner() == None

    board.state = 'OOOOOOOOO'
    assert board.winner() == p2

    board.state = 'XXXOXOOXO'
    assert board.winner() == p1

    board.state = 'OOOOOOXXX'
    # Player 1 wins in case of tie
    assert board.winner() == p1

def test_win_process():
    p1 = Player(name='1', mark='X')
    p2 = Player(name='2', mark='O')
    board = Board(player1=p1, player2=p2)
    """for i in range(100):
        random.seed(i)
        board.go(9)
        print(i)
        assert board.winner() == None
    "
    random.seed(0)
    board.go(9)
    assert board.winner()==p2
"""
