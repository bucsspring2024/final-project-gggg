import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.speed_x = 4
        self.speed_y = 4

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x + self.radius, self.y + self.radius), self.radius)
    
    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y