import pygame
import random
from initialise_board import Chessboard
from pieces import Piece
from gameplay import Gameplay, Status
from flag import Flag
from globals import BOARD_DIMENSION, SQUARE_SIZE, MARGIN, TOP_MARGIN

# Initialize Pygame
pygame.init()
random.seed()

# Set up the game board
screen = pygame.display.set_mode((BOARD_DIMENSION*SQUARE_SIZE, BOARD_DIMENSION*SQUARE_SIZE + TOP_MARGIN))
pygame.display.set_caption("Chess Minesweeper")

# Define chessboard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create an BOARD_DIMENSIONxBOARD_DIMENSION grid of squares with alternating colors
board_color = [[(BLACK if (i + j) % 2 == 0 else WHITE) for j in range(BOARD_DIMENSION)] for i in range(BOARD_DIMENSION)]

# Initialise chessboard and gameplay classes
chessboard = Chessboard()

# Gameplay class contains all the game logic
gameplay = Gameplay(chessboard)

# Flag class contains all the flagging logic
flag = Flag()

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
            if event.button == 1:
                if gameplay.check_square(row, col) == "win":
                    running = False
                print(chessboard.board[row][col])
            elif event.button == 3:
                flag.flag_square(row, col)
            elif event.button == 2:
                flag.clear_flags()

    #Draw the pieces that need to be found 
    for i in range(len(gameplay.mines)):
        square_size = min(BOARD_DIMENSION*SQUARE_SIZE/(3*len(gameplay.mines)+1)*2, SQUARE_SIZE)
        x = (square_size + MARGIN + square_size/2) * i + square_size/2
        y = square_size/2
        pygame.draw.rect(screen, (255,0,0), [x, y, square_size, square_size])
        if i < len(gameplay.remaining_mines):
            text = font.render(str(gameplay.remaining_mines[i][2]), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + square_size/2, y + square_size/2))
        screen.blit(text, text_rect)

    # Draw the chessboard and numbers/kings
    for row in range(BOARD_DIMENSION):
        for col in range(BOARD_DIMENSION):
            color = board_color[row][col]
            #Draw the squares
            pygame.draw.rect(screen, color, [(SQUARE_SIZE + MARGIN) * col, (SQUARE_SIZE + MARGIN) * row + TOP_MARGIN, SQUARE_SIZE, SQUARE_SIZE])
            #Draw the revealed squares
            text = font.render(str(chessboard.board[row][col]), True, (255, 0, 0))
            text_rect = text.get_rect(center=((SQUARE_SIZE + MARGIN) * col + SQUARE_SIZE // 2, (SQUARE_SIZE + MARGIN) * row + SQUARE_SIZE // 2 + TOP_MARGIN))
            if(gameplay.board_tracker[row][col] >= Status.CHECKED):
                screen.blit(text, text_rect)
            #Draw the flags
            small_font = pygame.font.Font(None, 24)  # Change the font size as needed
            text = small_font.render(str(flag.flagged.board[row][col]), True, (255, 0, 0))
            if flag.flagged.board[row][col] is not 0:
                screen.blit(text, ((SQUARE_SIZE + MARGIN) * col + MARGIN,(SQUARE_SIZE + MARGIN) * row + MARGIN + TOP_MARGIN))


    pygame.display.update()

# Quit Pygame
pygame.quit()
