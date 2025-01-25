import random
from constants import *


def is_safe(board, x, y):
    """
        Checks whether a cell and its surroundings are safe for placing a ship. Used only in function can_place_ship(), which is used for generating a random board.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            x (int): The row index of the cell to check.
            y (int): The column index of the cell to check.

        Returns:
            bool: True if the cell and its surroundings are empty, False if not.
    """
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                if board[nx][ny] != 0:
                    return False
    return True


def can_place_ship(board, x, y, size, orientation):
    """
        Checks if a ship can be placed at the specified position on the board.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            x (int): The row index where the ship placement starts.
            y (int): The column index where the ship placement starts.
            size (int): The size of the ship.
            orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).

        Returns:
            bool: True if the ship can be placed, False if not.
    """
    if orientation == 'H':
        if y + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[x][y + i] != 0 or not is_safe(board, x, y + i):
                return False
    else:
        if x + size > BOARD_SIZE:
            return False
        for i in range(size):
            if board[x + i][y] != 0 or not is_safe(board, x + i, y):
                return False
    return True


def place_ship(board, x, y, size, orientation):
    """
       Places a ship on the board at the specified position.

       Args:
           board (list[list[int]]): Two-dimensional list representing the state of the board.
           x (int): The row index where the ship placement starts.
           y (int): The column index where the ship placement starts.
           size (int): The size of the ship.
           orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).

       Returns:
           None
    """
    if orientation == 'H':
        for i in range(size):
            board[x][y + i] = size
    else:
        for i in range(size):
            board[x + i][y] = size


def generate_random_board():
    """
        Generates a random board configuration with ships placed according to game rules.

        Returns:
            list[list[int]]: A two-dimensional list representing the board with randomly placed ships.
    """
    SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for ship_size in SHIP_SIZES:
        placed = False
        total_attempts = 0
        while not placed:
            attempts = 0
            while not placed and attempts < 100:
                x = random.randint(0, BOARD_SIZE - 1)
                y = random.randint(0, BOARD_SIZE - 1)
                direction = random.choice(['H', 'V'])
                if can_place_ship(board, x, y, ship_size, direction):
                    place_ship(board, x, y, ship_size, direction)
                    placed = True
                attempts += 1
            total_attempts += 1
            if total_attempts > 10:
                board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
                break
    return board


def clear_ship_from_board(board, x, y, size, orientation):
    """
       Removes a ship from the board by resetting its occupied cells to 0.

       Args:
           board (list[list[int]]): A two-dimensional list representing the board with randomly placed ships.
           x (int): The row index where the ship starts.
           y (int): The column index where the ship starts.
           size (int): Ship size.
           orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).

       Returns:
           None
    """
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        board[nx][ny] = 0
