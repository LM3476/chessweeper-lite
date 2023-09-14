
"""
Class containing information about what the player sees.
This is the player's interface with the game.
player_board will be what is displayed to the player on the game board in the following way:
    If a square is undiscovered player_board will contain a zero at that square, and nothing will be displayed.
    If a square is flagged player_board will contain a one at that square, and a flag will be displayed.

"""
class Player:
    player_board = [[0 for _ in range(8)] for _ in range(8)]

    """
    Initializes the player's board.
    """
    def __init__(self) -> None:
        pass
