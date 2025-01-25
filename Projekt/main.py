from gui import *
from game_logic import *

player_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
computer_board = generate_random_board()
placed_ships = []
ship_drag_positions = []
placed_ships_computer = []
ships_to_drag = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
selected_ship = None
selected_offset = (0, 0)
ship_orientation = "H"
current_turn = "player"
game_state = "start"
winner = None


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battleships game")
    clock = pygame.time.Clock()

    global player_board, computer_board, placed_ships, placed_ships_computer, ships_to_drag, current_turn, selected_ship, selected_offset, ship_orientation, game_state, winner, mode, computer_shot_fn

    add_ships_from_random_board(player_board, placed_ships)
    add_ships_from_random_board(computer_board, placed_ships_computer)
    font = pygame.font.SysFont(None, 36)
    text_player_board = font.render("Your board", True, BLACK)
    text_computer_board = font.render("Computer's board", True, BLACK)

    running = True
    while running:
        if game_state == "start":
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
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if button_easy.collidepoint(mouse_x, mouse_y):
                        print("Easy Mode selected")
                        computer_shot_fn = computer_shot
                        game_state = "setup"
                    elif button_hard.collidepoint(mouse_x, mouse_y):
                        print("Hard Mode selected")
                        computer_shot_fn = computer_shot_hard
                        game_state = "setup"
                    elif button_rules.collidepoint(mouse_x, mouse_y):
                        print("Rules selected")
                        game_state = "rules"
        elif game_state == "rules":
            screen.fill(WHITE)
            font_title = pygame.font.SysFont(None, 48)
            text_title = font_title.render("Game rules", True, BLACK)
            text_title_rect = text_title.get_rect(center=(SCREEN_WIDTH // 2, 100))
            screen.blit(text_title, text_title_rect)

            font_text = pygame.font.SysFont(None, 32)

            for i, line in enumerate(RULES):
                text_rule = font_text.render(line, True, BLACK)
                screen.blit(text_rule, (50, 150 + i * 40))
            button_back = draw_button(screen, "Go back", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if button_back.collidepoint(mouse_x, mouse_y):
                        game_state = "start"
        elif game_state == "setup":
            screen.fill(WHITE)
            screen.blit(text_player_board, (300 + BOARD_SIZE * CELL_SIZE // 2 - text_player_board.get_width() // 2, 25))
            screen.blit(text_computer_board,
                        (SCREEN_WIDTH // 2 + 200 + BOARD_SIZE * CELL_SIZE // 2 - text_computer_board.get_width() // 2,
                         25))
            draw_board(screen, player_board, 300, 100)
            draw_board(screen, computer_board, SCREEN_WIDTH // 2 + 200, 100, hide_ships=True)
            button_randomize = draw_button(screen, "Randomize", 300, SCREEN_HEIGHT - 100, 150, 40)
            button_start_game = draw_button(screen, "Start game", 650, SCREEN_HEIGHT - 100, 150, 40)
            draw_ships_to_drag(screen, ships_to_drag, ship_drag_positions)

            for placed_ship in placed_ships:
                x, y, size, orientation = placed_ship
                for i in range(size):
                    rect = pygame.Rect(
                        300 + (y + i) * CELL_SIZE if orientation == "H" else 300 + y * CELL_SIZE,
                        100 + x * CELL_SIZE if orientation == "H" else 100 + (x + i) * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE
                    )
                    pygame.draw.rect(screen, BLUE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)

            # Draw dragged ship
            if selected_ship:
                ship_index, rect, is_from_board, size, orientation = selected_ship
                mouse_x, mouse_y = pygame.mouse.get_pos()
                rect = pygame.Rect(
                    mouse_x - selected_offset[0], mouse_y - selected_offset[1],
                    size * CELL_SIZE if orientation == "H" else CELL_SIZE,
                    CELL_SIZE if orientation == "H" else size * CELL_SIZE
                )
                pygame.draw.rect(screen, BLUE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos

                    if button_randomize.collidepoint(mouse_x, mouse_y):
                        player_board = generate_random_board()
                        add_ships_from_random_board(player_board, placed_ships)
                        ships_to_drag.clear()
                    elif button_start_game.collidepoint(mouse_x, mouse_y):
                        print("Game is trying to start...")

                    for idx, (x, y, size, orientation) in enumerate(placed_ships):
                        for i in range(size):
                            rect = pygame.Rect(
                                300 + (y + i) * CELL_SIZE if orientation == "H" else 300 + y * CELL_SIZE,
                                100 + x * CELL_SIZE if orientation == "H" else 100 + (x + i) * CELL_SIZE,
                                CELL_SIZE, CELL_SIZE
                            )
                            if rect.collidepoint(mouse_x, mouse_y):
                                selected_ship = (idx, rect, True, size, orientation)
                                selected_offset = (mouse_x - rect.x, mouse_y - rect.y)
                                clear_ship_from_board(player_board, x, y, size, orientation)
                                placed_ships.pop(idx)
                                break

                    for i, rect in enumerate(ship_drag_positions):
                        if rect.collidepoint(mouse_x, mouse_y):
                            selected_ship = (i, rect, False, ships_to_drag[i], ship_orientation)
                            selected_offset = (mouse_x - rect.x, mouse_y - rect.y)
                            break

                # Rotate ship
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and selected_ship:
                        ship_index, rect, is_from_board, size, orientation = selected_ship
                        new_orientation = "V" if orientation == "H" else "H"
                        selected_ship = (ship_index, rect, is_from_board, size, new_orientation)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if selected_ship:
                        mouse_x, mouse_y = event.pos
                        ship_index, rect, is_from_board, size, orientation = selected_ship
                        grid_x = (mouse_x - 300) // CELL_SIZE
                        grid_y = (mouse_y - 100) // CELL_SIZE

                        if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE and (
                                grid_x + size <= BOARD_SIZE if orientation == "H" else grid_y + size <= BOARD_SIZE):
                            if is_safe_to_place(player_board, grid_y, grid_x, size, orientation):
                                for j in range(size):
                                    nx, ny = (grid_y, grid_x + j) if orientation == "H" else (grid_y + j, grid_x)
                                    player_board[nx][ny] = size
                                placed_ships.append((grid_y, grid_x, size, orientation))
                                if not is_from_board:
                                    ships_to_drag.pop(ship_index)
                            else:
                                if is_from_board:
                                    ships_to_drag.append(size)
                        else:
                            if is_from_board:
                                ships_to_drag.append(size)
                        selected_ship = None

                    if button_start_game.collidepoint(mouse_x, mouse_y):
                        if len(ships_to_drag) != 0:
                            print("You have to place all of your ships!")
                        else:
                            print("Game has begun!")
                            game_state = "gameplay"
        elif game_state == "gameplay":
            screen.fill(WHITE)
            if winner is None:
                if check_victory(computer_board, placed_ships_computer):
                    winner = "player"
                    game_state = "end"
                elif check_victory(player_board, placed_ships):
                    winner = "computer"
                    game_state = "end"

            screen.blit(text_player_board, (50 + BOARD_SIZE * CELL_SIZE // 2 - text_player_board.get_width() // 2, 25))
            screen.blit(text_computer_board, (
                SCREEN_WIDTH // 2 + BOARD_SIZE * CELL_SIZE // 2 - text_computer_board.get_width() // 2, 25))
            draw_board(screen, player_board, 50, 100, is_player=True)
            draw_board(screen, computer_board, SCREEN_WIDTH // 2, 100, hide_ships=True)
            sorted_ships = sorted(placed_ships_computer, key=lambda ship: ship[2], reverse=True)

            fill_colors = []
            for x, y, size, orientation in sorted_ships:
                if is_ship_sunk(computer_board, x, y, size, orientation):
                    fill_colors.append(RED)
                else:
                    fill_colors.append(BLUE)

            font = pygame.font.SysFont(None, 24)
            text_remaining_ships = font.render("Remaining ships:", True, BLACK)
            text_rect = text_remaining_ships.get_rect(center=(SCREEN_WIDTH - 150 + CELL_SIZE // 2, 60))
            screen.blit(text_remaining_ships, text_rect)

            for i, ship_size in enumerate([ship[2] for ship in sorted_ships]):
                draw_ships_to_drag(screen, [ship_size], [], offset_x=SCREEN_WIDTH - 225,
                                   offset_y=100 + i * (CELL_SIZE + 10), fill_color=fill_colors[i])

            for x, y, size, orientation in placed_ships_computer:
                if is_ship_sunk(computer_board, x, y, size, orientation):
                    highlight_sunk_ship(screen, x, y, size, orientation, SCREEN_WIDTH // 2, 100)
                    mark_surrounding_as_missed(computer_board, x, y, size, orientation)

            for x, y, size, orientation in placed_ships:
                if is_ship_sunk(player_board, x, y, size, orientation):
                    highlight_sunk_ship(screen, x, y, size, orientation, 50, 100)
                    mark_surrounding_as_missed(player_board, x, y, size, orientation)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN and current_turn == "player":
                        mouse_x, mouse_y = event.pos
                        grid_x = (mouse_x - (SCREEN_WIDTH // 2)) // CELL_SIZE
                        grid_y = (mouse_y - 100) // CELL_SIZE
                        if 0 <= grid_x < BOARD_SIZE and 0 <= grid_y < BOARD_SIZE:
                            if computer_board[grid_y][grid_x] in (-1, -2):
                                print("You already shot here!")
                            else:
                                process_shot(computer_board, grid_y, grid_x)
                                current_turn = "computer"

                if current_turn == "computer":
                    computer_shot_fn(player_board)
                    current_turn = "player"
        elif game_state == "end":
            screen.fill(WHITE)
            font = pygame.font.SysFont(None, 72)
            if winner == "player":
                text = font.render("You Won!", True, GREEN)
            else:
                text = font.render("You Lost!", True, RED)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
            screen.blit(text, text_rect)

            button_retry = draw_button(screen, "Play again", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
            button_exit = draw_button(screen, "Exit", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if button_retry.collidepoint(mouse_x, mouse_y):
                        print("Restarting...")
                        player_board[:] = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
                        computer_board[:] = generate_random_board()
                        placed_ships.clear()
                        placed_ships_computer.clear()
                        add_ships_from_random_board(computer_board, placed_ships_computer)
                        ships_to_drag[:] = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
                        selected_ship = None
                        selected_offset = (0, 0)
                        ship_orientation = "H"
                        current_turn = "player"
                        game_state = "start"
                        winner = None

                    elif button_exit.collidepoint(mouse_x, mouse_y):
                        print("Game ended")
                        running = False

        pygame.display.flip()
        clock.tick(60)


pygame.quit()

if __name__ == "__main__":
    main()
