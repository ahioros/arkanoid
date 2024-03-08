import pygame


# Class to represent the paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, YELLOW):
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__()
        self.image = pygame.Surface([100, 10])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = (screen_width - self.rect.width) // 2
        self.rect.y = screen_height - 20
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width


if __name__ == "__main__":
    pass
