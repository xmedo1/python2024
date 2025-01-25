from board import generate_random_board
from constants import BOARD_SIZE
from game_logic import add_ships_from_random_board


class GameState:
    """
        Represents the current state of the game.
    """

    def __init__(self):
        self.player_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.computer_board = generate_random_board()
        self.placed_ships = []
        self.ship_drag_positions = []
        self.placed_ships_computer = []
        self.ships_to_drag = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.selected_ship = None
        self.selected_offset = (0, 0)
        self.ship_orientation = "H"
        self.current_turn = "player"
        self.game_state = "start"
        self.winner = None
        self.show_warning = False
        self.warning_timer = 0

    def reset(self):
        """
            Resets to default values.
        """
        self.player_board[:] = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.computer_board[:] = generate_random_board()
        self.placed_ships.clear()
        self.placed_ships_computer.clear()
        add_ships_from_random_board(self.computer_board, self.placed_ships_computer)
        self.ships_to_drag[:] = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.selected_ship = None
        self.selected_offset = (0, 0)
        self.ship_orientation = "H"
        self.current_turn = "player"
        self.game_state = "start"
        self.winner = None
