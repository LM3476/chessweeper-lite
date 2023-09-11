from typing import List, Tuple

class Chessboard:
    def __init__(self, pieces: List[Tuple[int, int, str]] = []):
        self.board = self.initialize_chessboard()
        for row, col, piece in pieces:
            self.add_piece(self.board, row, col, piece)
    
    def initialize_chessboard(self):
        # Initialize an 8x8 chessboard with all zeros.
        return [[0 for _ in range(8)] for _ in range(8)]

    def is_valid_square(self, row, col):
        # Check if the square (row, col) is within the bounds of the chessboard.
        return 0 <= row < 8 and 0 <= col < 8
    
    def is_occupied(self, chessboard, row, col):
        # Check if the square (row, col) is not occupied by a piece.
        return chessboard[row][col] in ["K", "Q", "R", "B", "N"]
    
    def add_piece(self, chessboard, row, col, piece):
        #if square is not a number then return
        if self.is_occupied(chessboard, row, col):
            # There's already a piece in the specified square.
            return

        if piece == Piece.KING:
            # Add a King to the specified square.
            chessboard[row][col] = "K"

            # Iterate through adjacent squares (including diagonals).
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_row, new_col = row + i, col + j
                    if self.is_valid_square(new_row, new_col) and not self.is_occupied(chessboard, new_row, new_col):
                        # Increment adjacent squares without a piece.
                        chessboard[new_row][new_col] += 1

        elif piece == Piece.QUEEN:
            # Add a Queen to the specified square.
            chessboard[row][col] = "Q"

            # Increment all squares in the same row, column, and diagonals.
            for i in range(8):
                if not self.is_occupied(chessboard, row, i):
                    chessboard[row][i] += 1
                if not self.is_occupied(chessboard, i, col):
                    chessboard[i][col] += 1

            for i in range(1, 8):
                for j in [-1, 1]:
                    for k in [-1, 1]:
                        new_row, new_col = row + i * k, col + i * j
                        if self.is_valid_square(new_row, new_col) and not self.is_occupied(chessboard, new_row, new_col):
                            chessboard[new_row][new_col] += 1

        elif piece == Piece.ROOK:
            # Add a Rook to the specified square.
            chessboard[row][col] = "R"

            # Increment all squares in the same row and column.
            for i in range(8):
                if not self.is_occupied(chessboard, row, i):
                    chessboard[row][i] += 1
                if not self.is_occupied(chessboard, i, col):
                    chessboard[i][col] += 1

        elif piece == Piece.BISHOP:
            # Add a Bishop to the specified square.
            chessboard[row][col] = "B"

            # Increment all squares in the diagonals.
            for i in range(1, 8):
                for j in [-1, 1]:
                    for k in [-1, 1]:
                        new_row, new_col = row + i * k, col + i * j
                        if self.is_valid_square(new_row, new_col) and not self.is_occupied(chessboard, new_row, new_col):
                            chessboard[new_row][new_col] += 1

        elif piece == Piece.KNIGHT:
            # Add a Knight to the specified square.
            chessboard[row][col] = "N"

            # Define the eight possible knight move offsets.
            knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

            # Increment squares reachable by the knight.
            for move in knight_moves:
                new_row, new_col = row + move[0], col + move[1]
                if self.is_valid_square(new_row, new_col) and not self.is_occupied(chessboard, new_row, new_col):
                    chessboard[new_row][new_col] += 1

    def print_chessboard(self, chessboard):
        for row in chessboard:
            print(" ".join(map(str, row)))


class Piece:
    KING = "K"
    QUEEN = "Q"
    ROOK = "R"
    BISHOP = "B"
    KNIGHT = "N"