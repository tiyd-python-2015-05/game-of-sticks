import random

class Board():
    def __init__(self, player1, player2):
        self.state = '_'*9
        self.won = None
        self.done = False
        self.current_player = player1
        self.player1 = player1
        self.player2 = player2

    def display(self):
        print(' '.join(self.state[:3]))
        print(' '.join(self.state[3:6]))
        print(' '.join(self.state[6:9]))
    def list_marks(self, mark):
        return [i for i in range(len(self.state)) if self.state[i] == mark]
    def list_available(self):
        return self.list_marks('_')

    def switch_players(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def go(self, num_turns=9):
        i = 0
        while i < num_turns:
            #turn = Turn(self.current_player)
            #turn.available = self.available
            #turn.take()
            self.current_player.available = self.list_available()
            try:
                self.mark_slot(self.current_player.choose())
            except:
                pass  # yucks
            the_winner = self.winner()
            if the_winner is not None:
                self.won = the_winner
                self.done = True
                return False
            self.switch_players()
            i += 1

    def mark_slot(self, choice):
        slot, mark = choice
        print(self.state[:slot] + mark + self.state[slot+1:])
        self.state = self.state[:slot] + mark + self.state[slot+1:]

    def winner(self):
        combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for player in [self.player1, self.player2]:
            player_marks = self.list_marks(player.mark)
            #print(player, self.flatten(player_marks))
            for combo in combos:
                #print(self.flatten(combo))
                if self.flatten(combo) in self.flatten(player_marks):
                    return player
    def is_done(self):
        return (self.won is not None) or (len(self.available) <= 0)
    def flatten(self, marks):
        string = ''
        for letter in marks:
            string = string + str(letter)
        return string

class Player():
    def __init__(self, name='1', mark='X'):
        self.name = name
        self.mark = mark
        self.won = False
        self.available = list(range(9))
        self.hats = None

    def __repr__(self):
        return 'Player ' + self.mark
    def choose(self):
        return (random.choice(self.available), self.mark)
    def fill_hats(self):
        if self.hats is None:
            self.hats = [{'in':[1,2,3], 'out':[]} for _ in range(self.sticks+1)]
    def learn(self):
        pass

class RandomPlayer(Player):
    pass
class HumanPlayer(Player):
    pass
class AIPlayer(Player):
    def choose(self):
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

class Session:
    def __init__(self):
        self.game = None
        self.sticks = 100
        self.human1 = Player('1', 'X')
        self.human2 = Player('2', 'O')
        self.npc1 = RandomPlayer('1', X)
        self.npc2 = AIPlayer('R2', 'O')
    def c_vs_c(self, silent=False):
        p1 = self.npc1
        p2 = self.npc2
        self.game = Board(p1, p2, silent=silent)
        #p1.fill_hats()
        p2.fill_hats()
        self.game.go()
        winner = self.game.winner()
        #p1.learn()
        p2.learn()
        return winner


# class Turn():
#     def __init__(self, player):
#         #self.done = False
#         self.available=None
#     def take():
#         player.available = self.available
#         choice = player.choose()
#         return choice
