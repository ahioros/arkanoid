import pytest

from arkanoid.ball import Ball
from arkanoid.paddle import Paddle

screen_width = 800
screen_height = 600

# Ball color
WHITE = (255, 255, 255)
# Paddle color
YELLOW = (255, 255, 0)


def test_ball_update():
    ball = Ball(screen_width, screen_height, WHITE)
    paddle = Paddle(screen_width, screen_height, YELLOW)
    ball.speed_x = 2
    ball.speed_y = 2
    ball.rect.x = 400
    ball.rect.y = 300
    ball.update()
    assert ball.rect.x == 402
    assert ball.rect.y == 302
