import random
import math


class player:
   def __init__(self, letter):
    #letter = x or o
    self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + ' \'s turn. Input move(0-8):')
            #check if the input if valid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                print("Invalid square. Please try again.")

        return val

class Unbeatable_ComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())

        else:
            #where the calculation happens
            square = self.Minimax(game, self.letter)

        return square

    def Minimax(self, state, player):
        max_player = self.letter
        other_player = "O" if self.letter == "X" else "X"
        
        #first check if there's a winner
        if self.current_winner == other_player:
            return {"position" : None, "score" : 1*(state.num_empty_squares() + 1) if other_player == max_player else -1*(state.num_empty_squares() + 1)}
            
        elif not state.empty_squares():
            return {"position" : None, "score" : 0}







