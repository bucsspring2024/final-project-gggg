import pygame

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 60
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, dy):
        self.y += dy
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)