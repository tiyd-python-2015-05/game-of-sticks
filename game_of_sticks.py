import random

class SticksGame:
    def __init__(self, p1, p2, sticks=100, silent=False):
        self.current_player = p1
        self.player_a = p1
        self.player_b = p2
        self.max_draw = 3
        self.player_a.initial = '1'
        self.player_b.initial = '2'
        self.set_sticks(sticks)
        self.player_a.won = None
        self.player_b.won = None
        self.silent = silent

    def set_sticks(self, sticks=100):
        self.sticks = sticks
        self.player_a.sticks = sticks
        self.player_b.sticks = sticks
        if sticks > 3:
            self.player_a.max_draw = 3
            self.player_b.max_draw = 3
        else:
            self.player_a.max_draw = sticks
            self.player_b.max_draw = sticks

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
            if not self.silent:
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
            self.current_player.won = True
            self.other_player().won = False
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
    def __init__(self, name='Sam', sticks=100):
        self.name = name
        self.max_draw = 3
        self.initial = 's'
        self.sticks = 100
        self.won = None
        self.hats = None

    def __repr__(self):
        return '{}: {}'.format(self.__class__, self.name)
    def choose(self, auto=None):
        if auto is not None:
            if auto<=self.max_draw:
                return auto
        return random.randint(1,self.max_draw)

    def fill_hats(self):
        if self.hats is None:
            self.hats = [{'in':[1,2,3], 'out':[]} for _ in range(self.sticks+1)]
    def learn(self):
        pass

class RandomPlayer(Player):
    pass

class AIPlayer(Player):

    def choose(self, auto=None):
        if auto is not None:
            if auto<=self.max_draw:
                return auto
        #print('self.sticks: ', self.sticks)
        #print('self.hats: ', self.hats)
        hat = self.hats[self.sticks]
        choice = random.choice(hat['in'])
        while choice > self.max_draw:
            choice = random.choice(hat['in'])
        ball = hat['in'].index(choice)
        hat['out'].append(hat['in'].pop(ball))
        #print('RandomPlayer self.hats has {} bins:\n'.format(len(self.hats)), self.hats)


        return choice
    def learn(self):
        #print(self.won)
        for sticks, hat in enumerate(self.hats):
            if self.won == True:
                self.hats[sticks]['in'].extend(hat['out'])
                self.hats[sticks]['in'].extend(hat['out'])
            self.hats[sticks]['out'] = []
            for i in range(1,4):
                if i not in hat['in']:
                    self.hats[sticks]['in'].append(i)

    def show_wisdom(self):
        print('After learning: ')
        print('Sticks\tTake1\tTake2\tTake3')
        for sticks, dictionary in enumerate(self.hats):
            c = lambda x: str(dictionary['in'].count(x) -2).replace('-1','.')
            if sticks > 20:
                break
            print('{}\t{}\t{}\t{}'.format(sticks, c(1), c(2), c(3)))



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
        self.sticks = 100
        self.human1 = HumanPlayer('Harry')
        self.human2 = HumanPlayer('Sally')
        self.npc1 = RandomPlayer('Marvin')
        self.npc2 = AIPlayer('R2')
    def h_vs_h(self):
        p1 = self.human1
        p2 = self.human2
        self.game = SticksGame(p1, p2, sticks=self.sticks)
        self.game.play()
        return self.game.check_winner()

    def h_vs_c(self):
        p1 = self.human1
        p2 = self.npc2
        self.game = SticksGame(p1, p2, sticks=self.sticks)
        p2.fill_hats()
        self.game.play()
        winner = self.game.check_winner()
        p2.learn()
        return winner


    def c_vs_c(self, silent=False):
        p1 = self.npc1
        p2 = self.npc2
        self.game = SticksGame(p1, p2, sticks=self.sticks, silent=silent)
        #p1.fill_hats()
        p2.fill_hats()
        self.game.play()
        winner = self.game.check_winner()
        #p1.learn()
        p2.learn()
        return winner

    def ai_training(self, rounds=1000):
        print('Initiating training...', end='')
        for i in range(1,rounds+1):
            if rounds % i == 20:
                print('.', end='')
            self.c_vs_c(silent=True)


class UserInterface():
    def __init__(self):
        self.my_session = Session()
    def num_sticks_menu(self):
        try:
            sticks = int(input('How many sticks are on the table? [10-100]:'))
            if 10 <= sticks <=100:
                self.my_session.sticks = sticks
                return
            return self.num_sticks_menu()
        except ValueError:
            print('Please enter a number between 10 and 100.')
            return self.num_sticks_menu()
    def num_player_menu(self):
        try:
            mode = int(input('How many human players? [0-2]: '))
        except ValueError:
            return self.num_player_menu()
        if mode == 2:

            return self.my_session.h_vs_h()
        if mode == 1:
            rounds = self_training_menu()
            self.my_session.ai_training(rounds)
            self.my_session.npc2.show_wisdom()
            return self.my_session.h_vs_c()
        if mode == 0:
            return self.my_session.c_vs_c()
        print('Please enter a number between 0 and 2.')
        return self.num_player_menu()
    def welcome_menu(self):
        print('Welcome to The Game of Sticks!')
    def game_over_menu(self):
        print('Player {} wins!'.format(self.my_session.game.check_winner().initial))
    def play_again_menu(self):
        play_again = input('Play again? [Y/n]: ' ).lower() + ' '
        return play_again[0] != 'n'
    def training_menu(self):
        try:
            rounds = int(input('How many rounds of training should the computer get? [10-100000]:'))
            if 10 <= rounds <=100000:
                return rounds
        except ValueError:
            print('Please enter a number between 10 and 100000.')
            return self.training_menu()


    def main(self):
        self.welcome_menu()
        self.num_sticks_menu()
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
