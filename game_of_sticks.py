import os



class Player:
    
    def __init__(self, name):
        self.name = name
        
        
class Game():

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.sticks = 55
        self.current_player = self.player1




    def switch_players(self):
        if self.current_player == self.player1:
            print("{} it is now your turn".format(self.player1))
            self.current_player = self.player2
        else:
            self.current_player = self.player1
            print("{} its your turn".format(self.player2))
        
    def pile(self):
        return "Pile has {} stick(s)".format(self.sticks) \
                + (" / " * self.sticks)

    def begin_game(self):
        os.system('clear')
        print(self.pile())
        self.switch_players()
        while self.sticks > 1:
            self.need_choice()
            if self.sticks <= 1:
                print("GAmE OveR! {}, WINS".format(self.current_player))
            elif self.sticks == 0:
                print("GAmE OveR! {}, is the Winner".format(self.current_player))
            else:
                self.need_choice()




    def need_choice(self):
        
        self.choice = input('How many sticks would you like to pick up?(1-3) {}:')
        try:
            int(self.choice)
        except:
            print('Please enter a valid choice(1-3)')
            self.need_choice()
        self.choice = int(self.choice)
        if self.choice > 0 and self.choice <= 3:
            how_many_sticks = self.choice
            self.sticks = self.sticks - how_many_sticks
        else:
            print('please enter a valid choice')
            self.need_choice()
        print(self.pile())
        self.switch_players()


if __name__ == '__main__':
    g1 = Game('Keith','Devil')
    g1.begin_game()
