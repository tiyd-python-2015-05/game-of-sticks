import random

class OnePlayerGame:
    '''Contains the majority of the gameplay for a player Vs AI game'''
    def __init__(self, trained_choices = {}):
        self.player = Player(input("What is your name?: "))
        self.current_player = self.player
        self.number_of_sticks = 0
        self.winner = None
        self.choice = 0
        self.the_choices = trained_choices

    def start(self):
        self.get_sticks()
        self.the_ai = ArtIn(self.number_of_sticks, self.the_choices)
        while self.number_of_sticks > 1:
            self.get_choice()
            self.number_of_sticks = self.number_of_sticks - self.choice
            if self.number_of_sticks <= 1:
                if self.number_of_sticks == 1:
                    self.winner = self.player
                else:
                    self.winner = self.the_ai
                break
            print("There are {} sticks on the board".format(self.number_of_sticks))
            self.switch_players()

            ai_choice = self.the_ai.pick_some_sticks(self.number_of_sticks)
            self.number_of_sticks = self.number_of_sticks - ai_choice
            print("The AI took {} sticks".format(ai_choice))
            if self.number_of_sticks <= 1:
                if self.number_of_sticks == 1:
                    self.winner = self.the_ai
                else:
                    self.winner = self.player
                break
            print("There are {} sticks on the board".format(self.number_of_sticks))
            self.switch_players()

        if self.number_of_sticks <= 0:
            print("{} wins".format(self.winner))
        else:
            print("There is one stick left on the board, {} wins".format(self.winner))

        if self.winner == self.the_ai:
            for pair in self.the_ai.game_choices.items():
                if pair[0] in self.the_choices.keys():
                    self.the_choices[pair[0]].extend(pair[1])
                else:
                    self.the_choices[pair[0]] = pair[1]

        #print(self.the_choices)
        self.play_again = input("Do you want to play again (Y/N)?").lower()
        if self.play_again == "y":
            self.start()
        else:
            quit()


    def get_choice(self):
        self.usr_choice = input("{}, how many sticks would you like to pick up (1,2,3)? ".format(self.player))
        try:
            int(self.usr_choice)
        except:
            print("Not a valid choice")
            self.get_choice()
        self.usr_choice = int(self.usr_choice)
        if self.usr_choice > 0 and self.usr_choice < 4:
            self.choice = self.usr_choice
        else:
            print("Not a valid choice")
            self.get_choice()


    def get_sticks(self):
        self.usr_choice = input("How many sticks would you like to play with? ")
        try:
            int(self.usr_choice)
            self.number_of_sticks = int(self.usr_choice)
        except:
            print("Not a valid choice")
            self.get_sticks()


    def switch_players(self):
        if self.current_player == self.player:
            self.current_player = self.the_ai
        else:
            self.current_player = self.player

class ArtIn:
    '''Artificial intelligence class, creates a learning AI character which
    improves with each round of play'''
    def __init__(self, sticks, the_choices={}):
        self.game_choices = {}
        self.start_sticks = sticks
        self.old_choices = the_choices
        self.turn_options = {i+1: [1,2,3] for i in range(self.start_sticks)}
        if self.old_choices != {}:
            for pair in self.old_choices.items():
                if pair[0] in self.turn_options.keys():
                    self.turn_options[pair[0]].extend(pair[1])
        #print(self.turn_options)

    def __repr__(self):
        return "The AI"

    def pick_some_sticks(self, sticks):
        self.no_of_sticks = sticks
        self.choice = random.choice(self.turn_options[self.no_of_sticks])
        self.game_choices[self.no_of_sticks] = [self.choice]
        return self.choice

class Player:
    def __init__(self, name="Player__"):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

if __name__ == '__main__':
    game = OnePlayerGame()
    game.start()
