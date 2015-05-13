
class Player:


    def __init__(self, name):
        self.name = name





class Game():

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.sticks = 20
        #self.switch_players = self.player1
        self.winner = False


    # def switch_players(self):
    #     if self.current_player == self.player1:
    #         self.current_player = self.player2
    #     else:
    #         self.current_player = self.player1
            #Explain this logic
    def begin_game(self):
        while self.sticks > 0:
            self.need_choice()
            #self.switch_players()
    # def winner(self):
    #
    #     if self.sticks == 0:
    #         return need_choice()
    #     else:
    #         self.need_choice()



    def need_choice(self):
        self.choice = input('how many sticks(1-3): ')
        try:
            int(self.choice)
        except:
            print('please enter a valid choice')
            self.need_choice()
        self.choice = int(self.choice)
        if self.choice > 0 and self.choice <= 3:
            how_many_sticks = self.choice
            self.sticks = self.sticks - how_many_sticks
        elif self.sticks == 0:
            print('you lose')
        else:
            print('please enter a valid choice')
            self.need_choice()



if __name__ == '__main__':
    g1 = Game('Keith','Devil')
    g1.begin_game()
