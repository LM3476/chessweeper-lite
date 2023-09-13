import pygame
import random
from initialise_board import Chessboard, Piece
from gameplay import Gameplay, Status

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

# Initialise chessboard and gameplay classes
chessboard = Chessboard()
gameplay = Gameplay()
for mine in gameplay.mines:
    chessboard.add_piece(*mine)

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
            print("Click ", x, y, "Grid coordinates: ", row, col)
            # Check the square at (row, col)
            if gameplay.check_square(chessboard, row, col) == "win":
                running = False
            print(chessboard.board[row][col])

    # Draw the chessboard and numbers/kings
    for row in range(8):
        for col in range(8):
            color = board_color[row][col]
            pygame.draw.rect(screen, color, [(SQUARE_SIZE + MARGIN) * col, (SQUARE_SIZE + MARGIN) * row, SQUARE_SIZE, SQUARE_SIZE])
            text = font.render(str(chessboard.board[row][col]), True, (255, 0, 0))
            text_rect = text.get_rect(center=((SQUARE_SIZE + MARGIN) * col + SQUARE_SIZE // 2, (SQUARE_SIZE + MARGIN) * row + SQUARE_SIZE // 2))
            if(gameplay.board_tracker[row][col] >= Status.CHECKED):
                screen.blit(text, text_rect)

    pygame.display.update()

# Quit Pygame
pygame.quit()
