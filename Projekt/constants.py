BOARD_SIZE = 10
CELL_SIZE = 50
SCREEN_WIDTH = BOARD_SIZE * CELL_SIZE * 2 + 500
SCREEN_HEIGHT = BOARD_SIZE * CELL_SIZE + 225
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RULES = [
                "0. Easy mode - Computer takes shots randomly, Hard mode - when computer hits, it tries to sink your ship before proceeding.",
                "1. Place your ships on the board. You can rotate your ships by holding it and pressing `R`. You can also randomize their positions.",
                "2. Attack your enemy ships, by clicking it's board.",
                "3. Field with red cross means, that you've hit a ship, but it has not sunk yet.",
                "4. Red ship means, that ship sank.",
                "5. The player who first sinks all the enemy's ships wins.",
                "Good Luck!"
]