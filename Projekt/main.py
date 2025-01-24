from gui import *
from board import *
from game_logic import *

ships_to_drag = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
ship_drag_positions = []
placed_ships = []
selected_ship = None
selected_offset = (0, 0)
ship_orientation = "H"


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battleships game")
    clock = pygame.time.Clock()

    player_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    computer_board = generate_random_board()

    global selected_ship
    global selected_offset
    global ship_orientation

    add_ships_from_random_board(player_board, placed_ships)
    font = pygame.font.SysFont(None, 36)
    text_player_board = font.render("Your board", True, BLACK)
    text_computer_board = font.render("Computer's board", True, BLACK)

    running = True
    while running:
        screen.fill(WHITE)

        screen.blit(text_player_board, (300 + BOARD_SIZE * CELL_SIZE // 2 - text_player_board.get_width() // 2, 25))
        screen.blit(text_computer_board,
                    (SCREEN_WIDTH // 2 + 200 + BOARD_SIZE * CELL_SIZE // 2 - text_computer_board.get_width() // 2, 25))

        draw_board(screen, player_board, 300, 100)
        draw_board(screen, computer_board, SCREEN_WIDTH // 2 + 200, 100)

        button_randomize = draw_button(screen, "Randomize", 300, SCREEN_HEIGHT - 100, 150, 40)
        button_start_game = draw_button(screen, "Start game", 500, SCREEN_HEIGHT - 100, 150, 40)
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
                    print("Game is starting...")

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
                        running = False
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
