from constants import *
import random


def is_safe_to_place(board, x, y, size, orientation):
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        if ny >= BOARD_SIZE or nx >= BOARD_SIZE or board[nx][ny] != 0:
            return False
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                cx, cy = nx + dx, ny + dy
                if 0 <= cx < BOARD_SIZE and 0 <= cy < BOARD_SIZE and board[cx][cy] != 0:
                    return False
    return True


def clear_ship_from_board(board, x, y, size, orientation):
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        board[nx][ny] = 0


def add_ships_from_random_board(board, placed_ships):
    placed_ships.clear()
    visited = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] > 0 and not visited[x][y]:
                size = board[x][y]
                visited[x][y] = True
                if y + 1 < BOARD_SIZE and board[x][y + 1] == size:
                    orientation = "H"
                    for i in range(size):
                        visited[x][y + i] = True
                    placed_ships.append((x, y, size, orientation))
                elif x + 1 < BOARD_SIZE and board[x + 1][y] == size:
                    orientation = "V"
                    for i in range(size):
                        visited[x + i][y] = True
                    placed_ships.append((x, y, size, orientation))
                else:
                    placed_ships.append((x, y, size, "H"))


def is_ship_sunk(board, x, y, size, orientation):
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        if board[nx][ny] > 0:
            return False
    return True


def process_shot(board, x, y):
    if board[x][y] > 0:  # Hit
        board[x][y] = -1
        return "hit"
    elif board[x][y] == 0:  # Miss
        board[x][y] = -2
        return "miss"
    return None  # Already shot


def computer_shot(board):
    while True:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)

        if board[x][y] == 0:
            board[x][y] = -2
            break
        elif board[x][y] > 0:
            board[x][y] = -1
            break
