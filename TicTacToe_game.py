from TicTacToe_player import HumanPlayer, RandomComputerPlayer

class Tic_Tac_Toe:
    def __init__(self):
        #use a single list to represent 3x3 board
        self.board = [" " for _ in range(9)]
        #keep track of if there's a winner
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| ", " | ".join(row) + " |" )

    def print_board_nums():
        #0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3:(j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| ", " | ".join(row) + " |" )

    def available_moves(self):
        return[i for i,spot in enumerate(self.board) if spot == " "]
       """  moves = []
        for (i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)

        return moves """

    def empty_squares(self):
        return " " in self.board #return a boolean to check if there's empty space

    def num_empty_squares(self):
        return self.board.count(" ")
        # or return len(self.available_moves())

    def make_move(self,square,letter):
        if self.board[square] == " ":
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        #check row, column and diagonal
        #check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3]for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #[2,4,6 or 0,4,8]
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0,4,8]]
            if all ([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2,4,6]]
            if all ([spot == letter for spot in diagonal_2]):
                return True
        return False
        
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    #iterate while there's empty space. If there's a winner then break the loop
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #define a function to get move.

        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}" )
                game.print_board()
                print(" ") # print an empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + "wins!")
                return letter 


            #after we made our move, alternate letters
            letter = "O" if letter == "X" else "X"
         """    if letter == "X":
                letter = "O"
            else:
                letter = "X" """

        if print_game:
            print("it\'s a tie!")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = Tic_Tac_Toe()
    play(t, x_player, o_player, print_game = True)

        







            



