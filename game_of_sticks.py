import random

class SticksGame:
    def __init__(self, p1, p2, sticks=100):
        self.sticks = sticks
        self.current_player = p1
        self.player_a = p1
        self.player_b = p2
        self.max_draw = 3
        self.player_a.initial = '1'
        self.player_b.initial = '2'
        self.player_a.sticks = sticks
        self.player_b.sticks = sticks

    def play(self):
        while self.check_winner() is None:
            self.next_turn()
        return self.check_winner()

    def try_removing_sticks(self):
        turn = Turn(self.current_player)
        if self.sticks >= turn.removed_sticks:
            self.sticks -= turn.removed_sticks
            if self.player_a.max_draw > self.sticks:
                self.player_a.max_draw = self.sticks
            if self.player_a.max_draw > self.sticks:
                self.player_b.max_draw = self.sticks
            self.player_a.sticks = self.sticks
            self.player_b.sticks = self.sticks
            print('Player {} removes {} sticks. {} sticks remain.'.format(self.current_player.initial, turn.removed_sticks, self.sticks))
            return
        else:
            return self.try_removing_sticks()
    #def start(self):
    #    self.try_removing_sticks()
    def next_turn(self):
        self.try_removing_sticks()
        if self.current_player == self.player_a:
            self.current_player = self.player_b
            #turn = Turn(self.current_player)
        elif self.current_player == self.player_b:
            self.current_player = self.player_a
            #turn = Turn(self.current_player)
    def check_winner(self):
        #print('checking winner...')
        if self.sticks == 0:
            return self.current_player
        return None

    def other_player(self):
        #print("it's the other guy")
        if self.current_player is self.player_a:
        #    print(self.player_b)
            return self.player_b
        return self.player_a
        #print(self.player_a)

class Player:
    def __init__(self, name='Sam'):
        self.name = name
        self.max_draw = 3
        self.initial = 's'
        self.sticks = 100
    def __repr__(self):
        return '{}: {}'.format(self.__class__, self.name)
    def choose(self, auto=None):
        if auto is not None:
            if auto<=self.max_draw:
                return auto
        return random.randint(1,self.max_draw)

class RandomPlayer(Player):
    pass
class HumanPlayer(Player):
    def choose(self):
        choice = input("Player {}: {} sticks remain. How many sticks do you take (1-3)?".format(self.initial, self.sticks))
        if not choice.isnumeric():
            return self.choose()
        choice = int(choice)
        if choice>self.max_draw:
            return self.choose()
        return choice

class Turn:
    def __init__(self, player):
        self.player = player
        self.removed_sticks = player.choose()

class Session:
    def __init__(self):
        self.game = None
    def h_vs_h(self):
        p1 = HumanPlayer('Harry')
        p2 = HumanPlayer('Sally')
        self.game = SticksGame(p1, p2, sticks=10)
        self.game.play()
        return self.game.check_winner()

    def h_vs_c(self):
        p1 = HumanPlayer('Harry')
        p2 = RandomPlayer('Sally')
        self.game = SticksGame(p1, p2, sticks=10)
        self.game.play()
        return self.game.check_winner()


    def c_vs_c(self):
        p1 = RandomPlayer('Harry')
        p2 = RandomPlayer('Sally')
        self.game = SticksGame(p1, p2, sticks=100)
        self.game.play()
        return self.game.check_winner()

class UserInterface():
    def __init__(self):
        self.my_session = Session()
    def num_player_menu(self):
        try:
            mode = int(input('How many human players? [0-2]?'))
        except:
            return self.num_player_menu()
        if mode == 2:
            return self.my_session.h_vs_h()
        if mode == 1:
            return self.my_session.h_vs_c()
        if mode == 0:
            return self.my_session.c_vs_c()
        return self.num_player_menu()
    def welcome_menu(self):
        print('Welcome to The Game of Sticks!')
    def game_over_menu(self):
        print('Player {} wins!'.format(self.my_session.game.check_winner().initial))
    def play_again_menu(self):
        play_again = input('Play again? [Y/n]: ' ).lower() + ' '
        return play_again[0] != 'n'

    def main(self):
        self.welcome_menu()
        def loop():
            self.num_player_menu()
            self.game_over_menu()
        loop()
        while self.play_again_menu():
            loop()

if __name__ == '__main__':
    #my_session = Session()
    #my_session.h_vs_h()
    my_ui = UserInterface()
    my_ui.main()
