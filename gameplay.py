from typing import List, Tuple
import random
from initialise_board import Chessboard, Piece

"""
This file contains the gameplay class, which is responsible for managing the core gameplay of Chessweeper.
The class will generate a specific configuration of mines, and will keep track of the game state.
"""
class Gameplay:
    def __init__(self, chessboard: Chessboard) -> None:
        self.chessboard = chessboard
        self.board_tracker = self.initialise_board_tracker()
        self.mines = self.generate_mines()
        for mine in self.mines:
            chessboard.add_piece(*mine)
        self.remaining_mines = self.mines.copy()
        self.turns_taken = 0
        # print(self.mines)
   
    def initialise_board_tracker(self):
        # Initialise array to track whether a square has been clicked or not.
        return [[0 for _ in range(8)] for _ in range(8)]
    
    def generate_mines(self) -> List[Tuple[int, int]]:
        """Generates a random configuration of mines on the chessboard."""
        coords = []
        #We generate between 2-5 different pieces
        for _ in range(random.randint(2, 5)):
            #We generate a random position
            row, col = random.randint(0, 7), random.randint(0, 7)
            while (row, col) in coords:
                row, col = random.randint(0, 7), random.randint(0, 7)
            #We add the piece to the position
            coords.append((row, col))
        return [(row, col, random.choice(Piece.piece_list())) for row, col in coords]
    
    def check_square(self, row: int, col: int) -> None:
        """Checks the square at (row, col)."""
        if self.board_tracker[row][col] >= Status.CHECKED:
            # The square has already been checked.
            return
        else:
            self.turns_taken += 1
            if self.chessboard.board[row][col] in Piece.piece_list():
                self.board_tracker[row][col] = Status.MINE
                for mine in self.remaining_mines:
                    if (mine[0], mine[1]) == (row, col):
                        self.remaining_mines.remove(mine)
                        self.chessboard.add_piece(*mine, remove=True)
                        break
                # print("Remaining mines: ", self.remaining_mines)
                if len(self.remaining_mines) == 0:
                    print("You win!")
                    print("Turns taken: ", self.turns_taken)
                    return "win"
            else:
                self.board_tracker[row][col] = Status.CHECKED

class Status:
    UNCHECKED = 0
    FLAGGED = 1
    CHECKED = 2
    MINE = 3