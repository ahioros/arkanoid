#!/usr/bin/env python3

import random

import pygame

from arkanoid.ball import Ball
from arkanoid.brick import Brick
from arkanoid.paddle import Paddle


def main():
    # Init Pygame
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600

    # Ball color
    WHITE = (255, 255, 255)
    # Brick color
    BLUE = (0, 0, 255)
    # Paddle color
    YELLOW = (255, 255, 0)

    # Screen configuration
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Arkanoid")

    # Clock to control screen update speed
    clock = pygame.time.Clock()

    # Create the paddle
    paddle = Paddle(screen_width, screen_height, YELLOW)

    # Create the ball
    ball = Ball(screen_width, screen_height, WHITE)

    # Create the bricks
    bricks = pygame.sprite.Group()
    colors = [BLUE, BLUE, BLUE, BLUE, BLUE]
    for row in range(5):
        for col in range(8):
            brick = Brick(colors[row], col * 100, 50 + row * 30)
            bricks.add(brick)

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle)
    all_sprites.add(ball)
    all_sprites.add(bricks)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update paddle, ball, and bricks
        all_sprites.update()

        # Check collisions between ball and paddle
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y *= -1

        # Check collisions between ball and bricks
        brick_collision = pygame.sprite.spritecollide(ball, bricks, True)
        if brick_collision:
            ball.speed_y *= -1

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all sprites on the screen
        all_sprites.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Control the update speed
        clock.tick(60)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
            running = False
            pygame.quit()

    # Quit the game
    pygame.quit()


if __name__ == "__main__":
    main()
