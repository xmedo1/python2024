from board import *
import random


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


def computer_shot_hard(state):
    """
        Executes a smart shot on the board in hard mode. After hitting a ship, it targets nearby cells to try to sink the ship.

        Args:
            state (GameState): The current game state.

        Returns:
            None
    """
    if state.target_mode:
        while True:
            if state.target_direction:
                if state.target_direction == "up":
                    nx, ny = state.target_start[0] - 1, state.target_start[1]
                elif state.target_direction == "down":
                    nx, ny = state.target_start[0] + 1, state.target_start[1]
                elif state.target_direction == "left":
                    nx, ny = state.target_start[0], state.target_start[1] - 1
                elif state.target_direction == "right":
                    nx, ny = state.target_start[0], state.target_start[1] + 1

                if is_valid_target(nx, ny, state.player_board):
                    result = process_shot(state.player_board, nx, ny)
                    if result == "hit":
                        state.target_start = (nx, ny)
                        return
                    else:
                        state.checked_directions.add(state.target_direction)
                        directions = {
                            "up": "down",
                            "down": "up",
                            "left": "right",
                            "right": "left"
                        }
                        if directions[state.target_direction] not in state.checked_directions:
                            state.target_direction = directions[state.target_direction]
                            state.target_start = state.first_hit_point
                        else:
                            state.target_direction = None
                        return
                else:
                    state.checked_directions.add(state.target_direction)
                    directions = {
                        "up": "down",
                        "down": "up",
                        "left": "right",
                        "right": "left"
                    }
                    if directions[state.target_direction] not in state.checked_directions:
                        state.target_direction = directions[state.target_direction]
                        state.target_start = state.first_hit_point
                    else:
                        state.target_direction = None
                    continue
            else:
                directions = [
                    (state.target_start[0] - 1, state.target_start[1], "up"),
                    (state.target_start[0] + 1, state.target_start[1], "down"),
                    (state.target_start[0], state.target_start[1] - 1, "left"),
                    (state.target_start[0], state.target_start[1] + 1, "right")
                ]
                for nx, ny, direction in directions:
                    if is_valid_target(nx, ny, state.player_board) and direction not in state.checked_directions:
                        state.target_candidates.append((nx, ny))
                        state.target_direction = direction
                        break
                else:
                    state.target_mode = False
                    break
            return

    # Random mode
    while True:
        x = random.randint(0, BOARD_SIZE - 1)
        y = random.randint(0, BOARD_SIZE - 1)
        if is_valid_target(x, y, state.player_board):
            result = process_shot(state.player_board, x, y)
            if result == "hit":
                state.target_mode = True
                state.target_start = (x, y)
                state.first_hit_point = state.target_start
                state.checked_directions = set()
                directions = [(x - 1, y, "up"), (x + 1, y, "down"), (x, y - 1, "left"), (x, y + 1, "right")]
                for nx, ny, direction in directions:
                    if is_valid_target(nx, ny, state.player_board):
                        state.target_candidates.append((nx, ny))
                        state.target_direction = direction
                        break
            return
