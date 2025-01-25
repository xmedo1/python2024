from board import *
import random

# Global vars for hard mode logic
target_mode = False
target_start = None
target_direction = None
target_candidates = []


def add_ships_from_random_board(board, placed_ships):
    """
        Converts a random board's ship layout into a list of placed ships.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            placed_ships (list): A list to store information about placed ships.

        Returns:
            None
    """
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
    """
        Checks if a ship at the given position is sunk.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            x (int): The row index where the ship starts.
            y (int): The column index where the ship starts.
            size (int): Ship size.
            orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).

        Returns:
            bool: True if the ship is completely sunk, False otherwise.
    """
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        if board[nx][ny] > 0:
            return False
    return True


def process_shot(board, x, y):
    """
       Processes a shot on the board.

       Args:
           board (list[list[int]]): Two-dimensional list representing the state of the board.
           x (int): The row index of the shot.
           y (int): The column index of the shot.

       Returns:
           str: "hit" if a ship was hit, "miss" if it was a miss, None if already shot there.
    """
    if board[x][y] > 0:
        board[x][y] = -1
        return "hit"
    elif board[x][y] == 0:
        board[x][y] = -2
        return "miss"
    return None


def computer_shot_easy(board):
    """
        Executes a random shot on the board in easy mode.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.

        Returns:
            None
    """
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
    """
        Checks if all ships on the board are sunk.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            placed_ships (list): A list of placed ships.

        Returns:
            bool: True if all ships are sunk, False if not.
    """
    for x, y, size, orientation in placed_ships:
        if not is_ship_sunk(board, x, y, size, orientation):
            return False
    return True


def mark_surrounding_as_missed(board, x, y, size, orientation):
    """
        Marks the surrounding cells of a sunk ship as missed.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.
            x (int): The row index of the ship.
            y (int): The column index of the ship.
            size (int): Ship size.
            orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).

        Returns:
            None
    """
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
    """
        Checks if the given coordinates are a valid target for a shot. Used only in hard mode.

        Args:
            x (int): The row index of the target.
            y (int): The column index of the target.
            board (list[list[int]]): Two-dimensional list representing the state of the board.

        Returns:
            bool: True if the target is valid, False if not.
    """
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[x][y] not in (-1, -2)


def computer_shot_hard(board):
    """
        Executes a smart shot on the board in hard mode. After hitting a ship, it targets nearby cells to try to sink the ship.

        Args:
            board (list[list[int]]): Two-dimensional list representing the state of the board.

        Returns:
            None
    """
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
