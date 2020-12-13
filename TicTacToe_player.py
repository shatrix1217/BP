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
        pass

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass