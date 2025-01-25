from game_logic import *
from game_state import *
from gui import *


def handle_rules_screen(screen, state):
    """
        Handles the rules screen rendering and logic.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
            state (GameState): The current game state.

        Returns:
            bool: False if the user quits, True if not.
    """
    screen.fill(WHITE)
    font_title = pygame.font.SysFont(None, 48)
    text_title = font_title.render("Game Rules", True, BLACK)
    text_title_rect = text_title.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(text_title, text_title_rect)
    font_text = pygame.font.SysFont(None, 32)

    for i, line in enumerate(RULES):
        text_rule = font_text.render(line, True, BLACK)
        screen.blit(text_rule, (50, 150 + i * 40))

    button_back = draw_button(screen, "Go back", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button_back.collidepoint(mouse_x, mouse_y):
                state.game_state = "start"
    return True


def handle_start_screen(screen, state):
    """
        Handles the rendering and events for the start screen.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
            state (GameState): The current game state.

        Returns:
            bool: False if the user quits, True if not.
    """
    screen.fill(WHITE)
    font_large = pygame.font.SysFont(None, 250)
    text_battleships = font_large.render("Battleships", True, BLACK)
    text_battleships_rect = text_battleships.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    screen.blit(text_battleships, text_battleships_rect)

    button_easy = draw_button(screen, "Easy Mode", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
    button_hard = draw_button(screen, "Hard Mode", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 75, 200, 50)
    button_rules = draw_button(screen, "Rules", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button_easy.collidepoint(mouse_x, mouse_y):
                print("Easy Mode selected")
                state.computer_shot_mode = "easy"
                state.game_state = "setup"
            elif button_hard.collidepoint(mouse_x, mouse_y):
                print("Hard Mode selected")
                state.computer_shot_mode = "hard"
                state.game_state = "setup"
            elif button_rules.collidepoint(mouse_x, mouse_y):
                print("Rules selected")
                state.game_state = "rules"
    return True


def handle_setup_screen(screen, state):
    """
        Handles the rendering and events for the setup screen.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
            state (GameState): The current game state.

        Returns:
            bool: False if the user quits, True if not.
    """
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 36)
    text_player_board = font.render("Your board", True, BLACK)
    text_computer_board = font.render("Computer's board", True, BLACK)
    screen.blit(text_player_board, (300 + BOARD_SIZE * CELL_SIZE // 2 - text_player_board.get_width() // 2, 25))
    screen.blit(text_computer_board,
                (SCREEN_WIDTH // 2 + 200 + BOARD_SIZE * CELL_SIZE // 2 - text_computer_board.get_width() // 2, 25))
    draw_board(screen, state.player_board, 300, 100)
    draw_board(screen, state.computer_board, SCREEN_WIDTH // 2 + 200, 100, hide_ships=True)
    button_randomize = draw_button(screen, "Randomize", 300, SCREEN_HEIGHT - 100, 150, 40)

    if len(state.ships_to_drag) == 0:
        button_start_game = draw_button(screen, "Start game", 650, SCREEN_HEIGHT - 100, 150, 40, color=GREEN)
    else:
        button_start_game = draw_button(screen, "Start game", 650, SCREEN_HEIGHT - 100, 150, 40, color=GRAY)

    draw_ships_side(screen, state.ships_to_drag, state.ship_drag_positions)

    for placed_ship in state.placed_ships:
        x, y, size, orientation = placed_ship
        for i in range(size):
            rect = pygame.Rect(
                300 + (y + i) * CELL_SIZE if orientation == "H" else 300 + y * CELL_SIZE,
                100 + x * CELL_SIZE if orientation == "H" else 100 + (x + i) * CELL_SIZE,
                CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(screen, BLUE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

    if state.selected_ship:
        ship_index, rect, is_from_board, size, orientation = state.selected_ship
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rect = pygame.Rect(
            mouse_x - state.selected_offset[0], mouse_y - state.selected_offset[1],
            size * CELL_SIZE if orientation == "H" else CELL_SIZE,
            CELL_SIZE if orientation == "H" else size * CELL_SIZE
        )
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

    if state.show_warning:
        font_warning = pygame.font.SysFont(None, 28)
        text_warning = font_warning.render("You have to place all your ships!", True, RED)
        text_warning_rect = text_warning.get_rect(center=(725, SCREEN_HEIGHT - 50))
        screen.blit(text_warning, text_warning_rect)

        state.warning_timer -= 1
        if state.warning_timer <= 0:
            state.show_warning = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if button_randomize.collidepoint(mouse_x, mouse_y):
                state.player_board = generate_random_board()
                add_ships_from_random_board(state.player_board, state.placed_ships)
                state.ships_to_drag.clear()

            elif button_start_game.collidepoint(mouse_x, mouse_y):
                if len(state.ships_to_drag) == 0:
                    state.game_state = "gameplay"
                else:
                    state.show_warning = True
                    state.warning_timer = 300

            # Handle ship selection
            for idx, (x, y, size, orientation) in enumerate(state.placed_ships):
                for i in range(size):
                    rect = pygame.Rect(
                        300 + (y + i) * CELL_SIZE if orientation == "H" else 300 + y * CELL_SIZE,
                        100 + x * CELL_SIZE if orientation == "H" else 100 + (x + i) * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE
                    )
                    if rect.collidepoint(mouse_x, mouse_y):
                        state.selected_ship = (idx, rect, True, size, orientation)
                        state.selected_offset = (mouse_x - rect.x, mouse_y - rect.y)
                        clear_ship_from_board(state.player_board, x, y, size, orientation)
                        state.placed_ships.pop(idx)
                        break

            # Handle dragging ships
            for i, rect in enumerate(state.ship_drag_positions):
                if rect.collidepoint(mouse_x, mouse_y):
                    state.selected_ship = (i, rect, False, state.ships_to_drag[i], state.ship_orientation)
                    state.selected_offset = (mouse_x - rect.x, mouse_y - rect.y)
                    break

        # Rotate ship
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and state.selected_ship:
                ship_index, rect, is_from_board, size, orientation = state.selected_ship
                new_orientation = "V" if orientation == "H" else "H"
                state.selected_ship = (ship_index, rect, is_from_board, size, new_orientation)

        # Place ship on the board
        elif event.type == pygame.MOUSEBUTTONUP:
            if state.selected_ship:
                mouse_x, mouse_y = event.pos
                ship_index, rect, is_from_board, size, orientation = state.selected_ship
                grid_x = (mouse_x - 300) // CELL_SIZE
                grid_y = (mouse_y - 100) // CELL_SIZE

                if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE:
                    if can_place_ship(state.player_board, grid_y, grid_x, size, orientation):
                        for j in range(size):
                            nx, ny = (grid_y, grid_x + j) if orientation == "H" else (grid_y + j, grid_x)
                            state.player_board[nx][ny] = size
                        state.placed_ships.append((grid_y, grid_x, size, orientation))
                        if not is_from_board:
                            state.ships_to_drag.pop(ship_index)
                    else:
                        if is_from_board:
                            state.ships_to_drag.append(size)
                else:
                    if is_from_board:
                        state.ships_to_drag.append(size)
                state.selected_ship = None
    return True


def handle_gameplay_screen(screen, state):
    """
        Handles the rendering and events for the gameplay screen.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
            state (GameState): The current game state.

        Returns:
            bool: False if the user quits, True if not.
    """
    screen.fill(WHITE)
    if state.winner is None:
        if check_victory(state.computer_board, state.placed_ships_computer):
            state.winner = "player"
            state.game_state = "end"
        elif check_victory(state.player_board, state.placed_ships):
            state.winner = "computer"
            state.game_state = "end"
    font = pygame.font.SysFont(None, 36)
    text_player_board = font.render("Your board", True, BLACK)
    text_computer_board = font.render("Computer's board", True, BLACK)
    screen.blit(text_player_board, (50 + BOARD_SIZE * CELL_SIZE // 2 - text_player_board.get_width() // 2, 25))
    screen.blit(text_computer_board, (
        SCREEN_WIDTH // 2 + BOARD_SIZE * CELL_SIZE // 2 - text_computer_board.get_width() // 2, 25))
    draw_board(screen, state.player_board, 50, 100, is_player=True)
    draw_board(screen, state.computer_board, SCREEN_WIDTH // 2, 100, hide_ships=True)
    sorted_ships = sorted(state.placed_ships_computer, key=lambda ship: ship[2], reverse=True)
    fill_colors = []
    for x, y, size, orientation in sorted_ships:
        if is_ship_sunk(state.computer_board, x, y, size, orientation):
            fill_colors.append(RED)
        else:
            fill_colors.append(BLUE)

    font = pygame.font.SysFont(None, 24)
    text_remaining_ships = font.render("Remaining ships:", True, BLACK)
    text_rect = text_remaining_ships.get_rect(center=(SCREEN_WIDTH - 150 + CELL_SIZE // 2, 60))
    screen.blit(text_remaining_ships, text_rect)

    for i, ship_size in enumerate([ship[2] for ship in sorted_ships]):
        draw_ships_side(screen, [ship_size], [], offset_x=SCREEN_WIDTH - 225,
                        offset_y=100 + i * (CELL_SIZE + 10), fill_color=fill_colors[i])

    for x, y, size, orientation in state.placed_ships_computer:
        if is_ship_sunk(state.computer_board, x, y, size, orientation):
            highlight_sunk_ship(screen, x, y, size, orientation, SCREEN_WIDTH // 2, 100)
            mark_surrounding_as_missed(state.computer_board, x, y, size, orientation)

    for x, y, size, orientation in state.placed_ships:
        if is_ship_sunk(state.player_board, x, y, size, orientation):
            highlight_sunk_ship(screen, x, y, size, orientation, 50, 100)
            mark_surrounding_as_missed(state.player_board, x, y, size, orientation)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and state.current_turn == "player":
            mouse_x, mouse_y = event.pos
            grid_x = (mouse_x - (SCREEN_WIDTH // 2)) // CELL_SIZE
            grid_y = (mouse_y - 100) // CELL_SIZE
            if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE:
                if state.computer_board[grid_y][grid_x] in (-1, -2):
                    print("You already shot here!")
                else:
                    process_shot(state.computer_board, grid_y, grid_x)
                    state.current_turn = "computer"
    if state.current_turn == "computer":
        if state.computer_shot_mode == "easy":
            computer_shot_easy(state.player_board)
        elif state.computer_shot_mode == "hard":
            computer_shot_hard(state)
        state.current_turn = "player"
    return True


def handle_end_screen(screen, state):
    """
        Handles the rendering and events for the end screen.

        Args:
            screen (pygame.Surface): The screen surface to draw on.
            state (GameState): The current game state.

        Returns:
            bool: False if the user quits, True if not.
    """
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 72)
    if state.winner == "player":
        text = font.render("You Won!", True, GREEN)
    else:
        text = font.render("You Lost!", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    screen.blit(text, text_rect)
    button_retry = draw_button(screen, "Play again", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
    button_exit = draw_button(screen, "Exit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if button_retry.collidepoint(mouse_x, mouse_y):
                state.reset()

            elif button_exit.collidepoint(mouse_x, mouse_y):
                return False

    return True
