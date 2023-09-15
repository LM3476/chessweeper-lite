from initialise_board import Chessboard
from pieces import Piece
"""
Class for implementing simple flagging functionality.
"""
class Flag:
    def __init__(self):
        self.flagged = Chessboard()
        self.pieces = {}

    def flag_square(self, row, col):
        piece_types = Piece.piece_list()
        if (row, col) in self.pieces:
            current_piece_index = piece_types.index(self.pieces[(row, col)])
            if current_piece_index == len(piece_types) - 1:
                del self.pieces[(row, col)]
            else:
                self.pieces[(row, col)] = piece_types[current_piece_index + 1]
        else:
            self.pieces[(row, col)] = piece_types[0]
        
        #Wipe all the previous flags before updating with new ones
        self.flagged.board = self.flagged.initialize_chessboard()
        for (row, col), piece in self.pieces.items():
            self.flagged.add_piece(row, col, piece)
        print(self.flagged.board)

    def clear_flags(self):
        self.pieces = {}
        self.flagged.board = self.flagged.initialize_chessboard()
