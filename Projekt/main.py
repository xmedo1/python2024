from running_states import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Battleships game")
    clock = pygame.time.Clock()
    state = GameState()
    add_ships_from_random_board(state.player_board, state.placed_ships)
    add_ships_from_random_board(state.computer_board, state.placed_ships_computer)

    running = True
    while running:
        if state.game_state == "start":
            running = handle_start_screen(screen, state)
        elif state.game_state == "rules":
            running = handle_rules_screen(screen, state)
        elif state.game_state == "setup":
            running = handle_setup_screen(screen, state)
        elif state.game_state == "gameplay":
            running = handle_gameplay_screen(screen, state)
        elif state.game_state == "end":
            running = handle_end_screen(screen, state)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
