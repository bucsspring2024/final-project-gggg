import pygame
from ball import Ball
from paddle import Paddle
class Controller:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.paddle_speed = 5

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.paddle1 = Paddle(30, self.screen_height // 2 - 30)
        self.paddle2 = Paddle(self.screen_width - 40, self.screen_height // 2 - 30)
        self.ball = Ball(self.screen_width // 2, self.screen_height // 2)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    self.paddle1.move(-self.paddle_speed)
                elif event.key == K_s:
                    self.paddle1.move(self.paddle_speed)
                elif event.key == K_UP:
                    self.paddle2.move(-self.paddle_speed)
                elif event.key == K_DOWN:
                    self.paddle2.move(self.paddle_speed)

    def update(self):
        self.ball.move()

        # Check collision with paddles
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.speed_x *= -1

        # Check collision with walls
        if self.ball.y <= 0 or self.ball.y + self.ball.radius * 2 >= self.screen_height:
            self.ball.speed_y *= -1

        # Check if ball goes out of bounds
        if self.ball.x <= 0 or self.ball.x >= self.screen_width:
            self.ball = Ball(self.screen_width // 2, self.screen_height // 2)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)