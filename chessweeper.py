import pygame
import random
from initialise_board import Chessboard, Piece
from gameplay import Gameplay, Status

# Initialize Pygame
pygame.init()
random.seed(1)

# Define square size and margin
SQUARE_SIZE = 50
MARGIN = 0
TOP_MARGIN = 100

# Set up the game board
screen = pygame.display.set_mode((8*SQUARE_SIZE, 8*SQUARE_SIZE + TOP_MARGIN))
pygame.display.set_caption("Chess Minesweeper")

# Define chessboard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create an 8x8 grid of squares with alternating colors
board_color = [[(BLACK if (i + j) % 2 == 0 else WHITE) for j in range(8)] for i in range(8)]

# Initialise chessboard and gameplay classes
chessboard = Chessboard()

# Gameplay class contains all the game logic
gameplay = Gameplay(chessboard)

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
            if y < TOP_MARGIN:
                continue
            col, row = x // (SQUARE_SIZE + MARGIN), (y-TOP_MARGIN) // (SQUARE_SIZE + MARGIN)
            print("Click ", x, y, "Grid coordinates: ", row, col)
            # Check the square at (row, col)
            if gameplay.check_square(row, col) == "win":
                running = False
            print(chessboard.board[row][col])

    #Draw the pieces 
    for i in range(len(gameplay.mines)):
        x = (SQUARE_SIZE + MARGIN + SQUARE_SIZE/2) * i + SQUARE_SIZE/2
        y = SQUARE_SIZE/2
        pygame.draw.rect(screen, (255,0,0), [x, y, SQUARE_SIZE, SQUARE_SIZE])
        if i < len(gameplay.remaining_mines):
            text = font.render(str(gameplay.remaining_mines[i][2]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + SQUARE_SIZE/2, y + SQUARE_SIZE/2))
        screen.blit(text, text_rect)
    # Draw the chessboard and numbers/kings
    for row in range(8):
        for col in range(8):
            color = board_color[row][col]
            pygame.draw.rect(screen, color, [(SQUARE_SIZE + MARGIN) * col, (SQUARE_SIZE + MARGIN) * row + TOP_MARGIN, SQUARE_SIZE, SQUARE_SIZE])
            text = font.render(str(chessboard.board[row][col]), True, (255, 0, 0))
            text_rect = text.get_rect(center=((SQUARE_SIZE + MARGIN) * col + SQUARE_SIZE // 2, (SQUARE_SIZE + MARGIN) * row + SQUARE_SIZE // 2 + TOP_MARGIN))
            if(gameplay.board_tracker[row][col] >= Status.CHECKED):
                screen.blit(text, text_rect)

    pygame.display.update()

# Quit Pygame
pygame.quit()
