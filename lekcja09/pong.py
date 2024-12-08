"""
PLAYER 1 CONTROLS: W/S
PLAYER 2 CONTROLS: UP/DOWN
"""
import pygame
import random

# Consts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 600
WIN_SCORE = 11
PADDLE_SPEED = 10

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping pong game')

# Clock
FPS = 60
clock = pygame.time.Clock()


def reset_ball(ball, ball_speed):
    ball.x = WIDTH // 2
    ball.y = HEIGHT // 2
    ball_speed[0] *= random.choice([-1, 1])
    ball_speed[1] *= random.choice([-1, 1])


# Main game loop
def main():
    # Position, Paddle Width, Paddle Height
    p1 = pygame.Rect(20, 250, 10, 75)
    p2 = pygame.Rect(770, 250, 10, 75)
    # Position, ball size
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, 20, 20)
    ball_speed = [5, 5]

    score_p1, score_p2 = 0, 0

    game_on = True

    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        # Player 1 controls (W/S)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and p1.top > 0:
            p1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and p1.bottom < HEIGHT:
            p1.y += PADDLE_SPEED

        # Player 2 controls (UP/DOWN)
        if keys[pygame.K_UP] and p2.top > 0:
            p2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and p2.bottom < HEIGHT:
            p2.y += PADDLE_SPEED

        # Ball physics
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        if ball.colliderect(p1) or ball.colliderect(p2):
            ball_speed[0] = -ball_speed[0]

        # Scoring points
        if ball.left <= 0:
            score_p2 += 1
            reset_ball(ball, ball_speed)
        if ball.right >= WIDTH:
            score_p1 += 1
            reset_ball(ball, ball_speed)

        if score_p1 == WIN_SCORE or score_p2 == WIN_SCORE:
            game_on = False

        # Drawing Game
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, p1)
        pygame.draw.rect(screen, WHITE, p2)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 1)

        # Score
        font = pygame.font.Font(None, 74)
        text1 = font.render(str(score_p1), True, WHITE)
        text2 = font.render(str(score_p2), True, WHITE)
        screen.blit(text1, (WIDTH // 4 - text1.get_width() // 2, 20))
        screen.blit(text2, (3 * WIDTH // 4 - text2.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(FPS)

    screen.fill(BLACK)
    font = pygame.font.Font(None, 50)
    if score_p1 == WIN_SCORE:
        text = font.render("Player 1 won!", True, WHITE)
    else:
        text = font.render("Player 2 won!", True, WHITE)

    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()


if __name__ == "__main__":
    main()
