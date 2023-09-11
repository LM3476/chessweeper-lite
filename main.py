import pygame
import random
from initialise_board import Chessboard, Piece

# Initialize Pygame
pygame.init()

# Set up the game board
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chess Minesweeper")

# Define chessboard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create an 8x8 grid of squares with alternating colors
board_color = [[(BLACK if (i + j) % 2 == 0 else WHITE) for j in range(8)] for i in range(8)]

# Place kings randomly on the board
chessboard = Chessboard()
chessboard.add_piece(chessboard.board, random.randint(0, 7), random.randint(0, 7), Piece.KING)
chessboard.add_piece(chessboard.board, random.randint(0, 7), random.randint(0, 7), Piece.QUEEN)
chessboard.add_piece(chessboard.board, random.randint(0, 7), random.randint(0, 7), Piece.ROOK)
chessboard.add_piece(chessboard.board, random.randint(0, 7), random.randint(0, 7), Piece.BISHOP)
chessboard.add_piece(chessboard.board, random.randint(0, 7), random.randint(0, 7), Piece.KNIGHT)

# Define square size and margin
SQUARE_SIZE = 50
MARGIN = 0

# Set up fonts for displaying numbers
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col, row = x // (SQUARE_SIZE + MARGIN), y // (SQUARE_SIZE + MARGIN)
            if chessboard.board[row][col] == 'K':
                chessboard.board[row][col] = 'K'  # Show 'K' if there is a king
            else:
                chessboard.board[row][col] = str(chessboard.board[row][col])  # Show the number of kings nearby as a string
            print(chessboard.board[row][col])

    # Draw the chessboard and numbers/kings
    for row in range(8):
        for col in range(8):
            color = board_color[row][col]
            pygame.draw.rect(screen, color, [(SQUARE_SIZE + MARGIN) * col, (SQUARE_SIZE + MARGIN) * row, SQUARE_SIZE, SQUARE_SIZE])
            text = font.render(str(chessboard.board[row][col]), True, (255, 0, 0))
            text_rect = text.get_rect(center=((SQUARE_SIZE + MARGIN) * col + SQUARE_SIZE // 2, (SQUARE_SIZE + MARGIN) * row + SQUARE_SIZE // 2))
            screen.blit(text, text_rect)

    pygame.display.update()

# Quit Pygame
pygame.quit()

'''
Create a class called Square that represents a square on the chessboard.
The class should have the following attributes:
    - piece: a string representing the piece on the square (e.g. 'K' for king)
    - number_target: a string representing the number of pieces targeting that square
    - clicked: a boolean representing whether the square has been clicked on
    - flag: a boolean representing whether the square has been flagged
'''
class Square:
    def __init__(self, piece, number_target, clicked):
        self.piece = piece
        self.number_target = number_target
        self.clicked = clicked
        self.flag = False

    def __str__(self):
        return self.piece + self.number_target + self.clicked
    
