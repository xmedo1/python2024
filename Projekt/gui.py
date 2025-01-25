import pygame
from constants import *


def draw_board(screen, board, offset_x, offset_y, hide_ships=False, is_player=False):
    """
        Draws board and ships on the screen.

        Args:
            screen (pygame.Surface): Surface, where we draw all other elements.
            board (list[list[int]]): Two-dimensional list representing the state of the board.
                value -2: missed shot
                value -1: hit
                value 0: empty cell
                value > 0: represents presence of a ship (e.g. value 4 means that ship with a length of 4 has one of its parts on the cell)
            offset_x (int): The X coordinate of the start of the board on the screen.
            offset_y (int): The Y coordinate of the start of the board on the screen.
            hide_ships (bool): Whether to hide ships (e.g. on Enemy board: True). Can be used to test the program.
            is_player (bool): Whether it is a player board (if True, hits are marked differently).
        Returns:
            None
    """
    font = pygame.font.SysFont(None, 24)

    # Drawing letters (A-J) and numbers (1-10)
    for i in range(BOARD_SIZE):
        # Numbers
        number_text = font.render(str(i + 1), True, BLACK)
        screen.blit(number_text, (offset_x - 30, offset_y + i * CELL_SIZE + CELL_SIZE // 3))
        # Letters
        letter_text = font.render(chr(65 + i), True, BLACK)
        screen.blit(letter_text, (offset_x + i * CELL_SIZE + CELL_SIZE // 3, offset_y - 30))

    # Grid and ships
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
    """
        Draws an interactive button on the screen.

        Args:
            screen (pygame.Surface): Surface, where we draw all other elements.
            text (str): Text displayed on the button.
            x (int): The X coordinate of upper-left corner of the button.
            y (int): The Y coordinate of upper-left corner of the button.
            width (): Width of the button.
            height (): Height of the button.
            color (tuple): RGB values of a color to fill the button with.

        Returns:
            pygame.Rect: A rectangle object representing a button
    """
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)
    font = pygame.font.SysFont(None, 24)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect


def draw_ships_side(screen, ships_to_draw, ship_positions, offset_x=30, offset_y=60, fill_color=BLUE):
    """
        Draws ships next to a board.

        Args:
            screen (pygame.Surface): Surface, where we draw all other elements.
            ships_to_draw (list[int]): List containing ship sizes.
            ship_positions (list[pygame.Rect]): A list of rectangles representing ship positions.
            offset_x (int): The X coordinate of the beginning of the ship.
            offset_y (int): The Y coordinate of the beginning of the ship.
            fill_color (tuple): RGB values of a color to fill the ship with.

        Returns:
            None
    """
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
    """
        Highlights sunk ship on the board.

        Args:
            screen (pygame.Surface): Surface, where we draw all other elements.
            x (int): The X coordinate of the beginning of the ship.
            y (int): The Y coordinate of the beginning of the ship
            size (int): Ship size.
            orientation (str): Ship orientation ("H" - horizontal, "V" - vertical).
            offset_x (int): Offset X coordinate.
            offset_y (int): Offset Y coordinate.

        Returns:
            None
    """
    for i in range(size):
        nx, ny = (x, y + i) if orientation == "H" else (x + i, y)
        rect = pygame.Rect(offset_x + ny * CELL_SIZE, offset_y + nx * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 5)
        pygame.draw.line(screen, BLACK, rect.topleft, rect.bottomright, 5)
        pygame.draw.line(screen, BLACK, rect.topright, rect.bottomleft, 5)
