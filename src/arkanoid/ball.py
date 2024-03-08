import random

import pygame


# Class to represent the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, WHITE):
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.speed_x = random.choice([-2, 2])
        self.speed_y = -2

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1

        if self.rect.bottom > self.screen_height:
            # Reset the position of the ball if it falls off the screen.
            self.rect.x = self.screen_width // 2
            self.rect.y = self.screen_height // 2
            self.speed_x = random.choice([-2, 2])
            self.speed_y = -2


if __name__ == "__main__":
    pass
