import pygame
from constants import *


def draw_board(screen, board, offset_x, offset_y):
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

            # Drawing computer's ships (WiP purposes only)
            if board[row][col] != 0:
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


def draw_ships_to_drag(screen, ships_to_draw, ship_positions, offset_x=30, offset_y=60, colors=None, fill_color=BLUE):
    ship_positions.clear()
    for i, size in enumerate(ships_to_draw):
        rect = pygame.Rect(offset_x, offset_y + i * (CELL_SIZE + 10), size * CELL_SIZE, CELL_SIZE)
        ship_positions.append(rect)
        color = colors[i] if colors else BLACK
        pygame.draw.rect(screen, fill_color, rect)
        pygame.draw.rect(screen, color, rect, 3)
        for j in range(size):
            cell_rect = pygame.Rect(rect.left + j * CELL_SIZE, rect.top, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, fill_color, cell_rect)
            pygame.draw.rect(screen, color, cell_rect, 1)
