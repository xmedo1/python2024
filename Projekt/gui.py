import pygame
from constants import *


def draw_board(screen, board, offset_x, offset_y, hide_ships=False, is_player=False):
    font = pygame.font.SysFont(None, 24)

    # Drawing letters and numbers
    for i in range(BOARD_SIZE):
        # Numbers
        number_text = font.render(str(i + 1), True, BLACK)
        screen.blit(number_text, (offset_x - 30, offset_y + i * CELL_SIZE + CELL_SIZE // 3))
        # Letters
        letter_text = font.render(chr(65 + i), True, BLACK)
        screen.blit(letter_text, (offset_x + i * CELL_SIZE + CELL_SIZE // 3, offset_y - 30))

    # Grid
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(offset_x + col * CELL_SIZE, offset_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[row][col] == -1 and is_player:  # Hit player
                pygame.draw.rect(screen, BLUE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
                pygame.draw.line(screen, RED, rect.topleft, rect.bottomright, 5)
                pygame.draw.line(screen, RED, rect.topright, rect.bottomleft, 5)
            elif board[row][col] == -1:  # Hit computer
                pygame.draw.line(screen, RED, rect.topleft, rect.bottomright, 5)
                pygame.draw.line(screen, RED, rect.topright, rect.bottomleft, 5)
            elif board[row][col] == -2:  # Miss
                pygame.draw.circle(screen, (170, 210, 230), rect.center, 5)
            elif board[row][col] > 0 and not hide_ships:
                pygame.draw.rect(screen, BLUE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)


def draw_button(screen, text, x, y, width, height, color=GREEN):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    font = pygame.font.SysFont(None, 24)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect


def draw_ships_to_drag(screen, ships_to_draw, ship_positions, offset_x=30, offset_y=60, fill_color=BLUE):
    ship_positions.clear()
    for i, size in enumerate(ships_to_draw):
        rect = pygame.Rect(offset_x, offset_y + i * (CELL_SIZE + 10), size * CELL_SIZE, CELL_SIZE)
        ship_positions.append(rect)
        pygame.draw.rect(screen, fill_color, rect)
        pygame.draw.rect(screen, BLACK, rect, 3)
        for j in range(size):
            cell_rect = pygame.Rect(rect.left + j * CELL_SIZE, rect.top, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, fill_color, cell_rect)
            pygame.draw.rect(screen, BLACK, cell_rect, 1)


def highlight_sunk_ship(screen, x, y, size, orientation, offset_x, offset_y):
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        rect = pygame.Rect(offset_x + ny * CELL_SIZE, offset_y + nx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 5)
        pygame.draw.line(screen, BLACK, rect.topleft, rect.bottomright, 5)
        pygame.draw.line(screen, BLACK, rect.topright, rect.bottomleft, 5)
