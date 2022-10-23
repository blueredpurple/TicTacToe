import math 
import random


class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter = self
        #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

    def get_move(self, game):
        pass    

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        #random spot for next move 
        global square
        square = random.choice(game.avaliable_moves())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = int(input(str(self.letter) + '\'s turn. Input move (0-8): '))#
            try:
                val = int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

        




    
    



