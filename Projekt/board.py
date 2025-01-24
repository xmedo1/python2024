import random
from constants import BOARD_SIZE


def is_safe(board, x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                if board[nx][ny] != 0:
                    return False
    return True


def can_place_ship(board, x, y, size, direction):
    if direction == 'H':
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


def place_ship(board, x, y, size, direction):
    if direction == 'H':
        for i in range(size):
            board[x][y + i] = size
    else:
        for i in range(size):
            board[x + i][y] = size


def generate_random_board():
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
