class Game:
    def welcome():
        print("\t======WELCOME TO Game of Sticks======\n \
                Rules of the Game:\n \
                - Pick any number of sticks 1 through 3\n \
                - The one to pick the last one is the loser")


    def is_integer(num):
        '''check that the choice is an integer'''
        return isinstance(num, int)


    def is_valid_selection(choice, available_sticks):
        '''test if the choice of sticks is valid'''
        if choice < available_sticks and 1 <= choice <= 3:
            return True
        else:
            return False

    def remaining_sticks(picked_sticks, initial_sticks):
        return initial_sticks - picked_sticks





if __name__ == '__main__':
    welcome()
