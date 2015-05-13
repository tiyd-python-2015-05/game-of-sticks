import random


def pdf_sample(hat):
    N = sum(hat)
    c = random.randrange(N)
    for i in range(3):
        if c < sum(hat[:i+1]):
            return i+1


class Game:
    ''' Set game up with number of sticks
        Bounce back and forth between players
        Keeps track of sticks
        Returns which player is the winner
    '''

    def __init__(self, player1, player2, print_flag=True):
        self.player1 = player1
        self.player2 = player2
        self.player1.start_history()
        self.player2.start_history()
        self.print_flag = print_flag
        self.current_player = self.player1

    def loser(self):
        if self.sticks >= 1:
            return None
        else:
            return self.current_player

    def other_player(self):
        if self.current_player is self.player1:
            return self.player2
        else:
            return self.player1

    def start(self):
        self.sticks = self.current_player.set_sticks()
        if self.print_flag:
            print(" ")
            print("Welcome to the game of sticks!")

        while self.sticks >= 1:
            if self.print_flag:
                print(" ")
                print("There are "+str(self.sticks)+" sticks on the board.")
            self.next_turn()

        if self.print_flag:
            print(str(self.current_player)+", you lose.")
            print(" ")
        self.current_player.lost()
        self.other_player().won()

    def next_turn(self):
        self.current_player = self.other_player()
        n = self.current_player.choose_sticks(self.sticks)
        if self.print_flag:
            print(self.current_player.name + " chooses to remove " +
                  str(n) + " sticks.")
        self.sticks -= n


class Player:
    ''' Returns name of player
        Chooses the number of sticks'''

    def __init__(self, name):
        self.name = name
        self.n_win = 0
        self.n_lose = 0

    def __str__(self):
        return self.name


class HumanPlayer(Player):

    def set_sticks(self):
        print(" ")
        n = int(input("How many number of initial sticks are there? \
                (10-100) "))
        while n < 10 or n > 100:
            n = int(input("Please enter a number between 10 and 100. "))
        return n

    def choose_sticks(self, N_sticks):
        n = int(input(self.name+", how many sticks do you take? (1-3) "))
        while n < 1 or n > 3:
            n = int(input("Please enter a number between 1 and 3. "))
        return n

    def start_history(self):
        pass

    def won(self):
        self.n_win += 1

    def lost(self):
        self.n_lose += 1


class ComputerPlayer(Player):
    ''' Chooses number of sticks
        Draws from hats
        Extra function changes hat contents'''

    def __init__(self, name):
        self.name = name
        self.n_win = 0
        self.n_lose = 0

    def start_history(self):
        self.dist = [[1 for j in range(3)] for i in range(100)]
        self.hist_list = []

    def set_sticks(self):
        return random.choice(range(10, 100))

    def choose_sticks(self, N_sticks):
        n = pdf_sample(self.dist[N_sticks-1])
        self.tally_dist(n, N_sticks)
        return n

    def tally_dist(self, n, N_sticks):
        self.hist_list.append([N_sticks, n])

    def won(self):
        self.n_win += 1
        for event in self.hist_list:
            i = event[0]
            j = event[1]
            self.dist[i-1][j-1] += 2

    def lost(self):
        self.n_lose += 1
        for event in self.hist_list:
            i = event[0]
            j = event[1]
            self.dist[i-1][j-1] -= 1
            if self.dist[i-1][j-1] < 1:
                self.dist[i-1][j-1] = 1


if __name__ == '__main__':
    p1 = ComputerPlayer("Cool Person")
    p2 = ComputerPlayer("Ultron")
    game = Game(p1, p2, False)
    for i in range(1000):
        game.start()
    print(p1.name+" won: "+str(p1.n_win))
    print(p2.name+" won: "+str(p2.n_win))
    p1 = HumanPlayer("User")
    game = Game(p1, p2, True)
    game.start()
