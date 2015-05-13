from sticks_player_vs_AI import OnePlayerGame, AI
from begin_sticks_game import create_AI

game = OnePlayerGame()
game.start()
game.number_of_sticks = 10
the_ai = AI(game)

def test_AI_starting_dict():
    assert the_ai.turn_options == \
    {1: [1, 2, 3], 2: [1, 2, 3], 3: [1, 2, 3], 4: [1, 2, 3], 5: [1, 2, 3], 6: [1, 2, 3],
     7: [1, 2, 3], 8: [1, 2, 3], 9: [1, 2, 3], 10: [1, 2, 3]}

def test_pick_some_sticks():
    assert 0 < the_ai.pick_some_sticks(game.number_of_sticks) < 4
