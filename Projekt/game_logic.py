from board import *
import random

target_mode = False
target_start = None
target_direction = None
target_candidates = []


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


def check_victory(board, placed_ships):
    for x, y, size, orientation in placed_ships:
        if not is_ship_sunk(board, x, y, size, orientation):
            return False
    return True


def mark_surrounding_as_missed(board, x, y, size, orientation):
    for i in range(-1, size + 1):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if orientation == "H":
                    nx, ny = x + dx, y + i
                else:
                    nx, ny = x + i, y + dy
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE:
                    if board[nx][ny] == 0:
                        board[nx][ny] = -2


def is_valid_target(x, y, board):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] not in (-1, -2)


def computer_shot_hard(board):
    global target_mode, target_start, target_direction, target_candidates, first_hit_point, checked_directions
    if target_mode:
        while True:
            if target_direction:
                if target_direction == "up":
                    nx, ny = target_start[0] - 1, target_start[1]
                elif target_direction == "down":
                    nx, ny = target_start[0] + 1, target_start[1]
                elif target_direction == "left":
                    nx, ny = target_start[0], target_start[1] - 1
                elif target_direction == "right":
                    nx, ny = target_start[0], target_start[1] + 1

                if is_valid_target(nx, ny, board):
                    result = process_shot(board, nx, ny)
                    if result == "hit":
                        target_start = (nx, ny)
                        return
                    else:
                        checked_directions.add(target_direction)
                        directions = {
                            "up": "down",
                            "down": "up",
                            "left": "right",
                            "right": "left"
                        }
                        if directions[target_direction] not in checked_directions:
                            target_direction = directions[target_direction]
                            target_start = first_hit_point
                        else:
                            target_direction = None
                        return
                else:
                    checked_directions.add(target_direction)
                    directions = {
                        "up": "down",
                        "down": "up",
                        "left": "right",
                        "right": "left"
                    }
                    if directions[target_direction] not in checked_directions:
                        target_direction = directions[target_direction]
                        target_start = first_hit_point
                    else:
                        target_direction = None
                    continue
            else:
                directions = [
                    (target_start[0] - 1, target_start[1], "up"),
                    (target_start[0] + 1, target_start[1], "down"),
                    (target_start[0], target_start[1] - 1, "left"),
                    (target_start[0], target_start[1] + 1, "right")
                ]
                for nx, ny, direction in directions:
                    if is_valid_target(nx, ny, board) and direction not in checked_directions:
                        target_candidates.append((nx, ny))
                        target_direction = direction
                        break
                else:
                    target_mode = False
                    break
            return

    # Random mode
    while True:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)
        if is_valid_target(x, y, board):
            result = process_shot(board, x, y)
            if result == "hit":
                target_mode = True
                target_start = (x, y)
                first_hit_point = target_start
                checked_directions = set()
                directions = [(x - 1, y, "up"), (x + 1, y, "down"), (x, y - 1, "left"), (x, y + 1, "right")]
                for nx, ny, direction in directions:
                    if is_valid_target(nx, ny, board):
                        target_candidates.append((nx, ny))
                        target_direction = direction
                        break
            return
