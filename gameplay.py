from typing import List, Tuple
import random
from initialise_board import Chessboard
from pieces import Piece
from globals import BOARD_DIMENSION, MIN_MINES, MAX_MINES, NUMS_ON_MINES

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
        self.revealed_mines = []
        self.turns_taken = 0
        # print(self.mines)
   
    def initialise_board_tracker(self):
        # Initialise array to track whether a square has been clicked or not.
        return [[0 for _ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]
    
    def generate_mines(self) -> List[Tuple[int, int]]:
        """Generates a random configuration of mines on the chessboard."""
        coords = []
        #We generate between 2-5 different pieces
        for _ in range(random.randint(MIN_MINES, MAX_MINES)):
            #We generate a random position
            row, col = random.randint(0, BOARD_DIMENSION-1), random.randint(0, BOARD_DIMENSION-1)
            while (row, col) in coords:
                row, col = random.randint(0, BOARD_DIMENSION-1), random.randint(0, BOARD_DIMENSION-1)
            #We add the piece to the position
            coords.append((row, col))
        return [(row, col, random.choice(Piece.piece_list())) for row, col in coords]
    
    def check_if_coord_in_remaining_mines(self, row: int, col: int) -> bool:
        """Checks if the square at (row, col) contains a mine."""
        #Don't need to check if NUMS_ON_MINES is False
        if not NUMS_ON_MINES:
            return False
        for mine in self.remaining_mines:
            if (mine[0], mine[1]) == (row, col):
                return True
        return False
    
    def check_square(self, row: int, col: int) -> None:
        """Checks the square at (row, col)."""
        if self.board_tracker[row][col] >= Status.CHECKED:
            # The square has already been checked.
            return
        else:
            self.turns_taken += 1
            if self.chessboard.board[row][col] in Piece.piece_list() or self.check_if_coord_in_remaining_mines(row, col):
                self.board_tracker[row][col] = Status.MINE
                for mine in self.remaining_mines:
                    if (mine[0], mine[1]) == (row, col):
                        self.remaining_mines.remove(mine)
                        self.revealed_mines.append(mine)
                        self.chessboard.add_piece(*mine, remove=True)
                        break
                # print("Remaining mines: ", self.remaining_mines)
                if len(self.remaining_mines) == 0:
                    print("You win!")
                    print("Turns taken: ", self.turns_taken)
                    return "win"
            else:
                # Comment out the following line if you don't want to clear adjacent empty squares.
                # self.clear_adjacent_empty_squares(row, col)
                self.board_tracker[row][col] = Status.CHECKED
    
    def clear_adjacent_empty_squares(self, row: int, col: int) -> None:
        """Clears all adjacent empty squares to the square at (row, col)."""
        if self.chessboard.is_valid_square(row, col) and self.chessboard.board[row][col] == 0 and self.board_tracker[row][col] < Status.CHECKED:
            self.board_tracker[row][col] = Status.CHECKED
            self.clear_adjacent_empty_squares(row - 1, col)
            self.clear_adjacent_empty_squares(row + 1, col)
            self.clear_adjacent_empty_squares(row, col - 1)
            self.clear_adjacent_empty_squares(row, col + 1)

class Status:
    UNCHECKED = 0
    FLAGGED = 1
    CHECKED = 2
    MINE = 3