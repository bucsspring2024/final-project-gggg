import pygame
from src.ball import Ball
from src.paddle import Paddle

class Controller:
    def __init__(self):
        """
        Initializes the Controller class
        Sets up pygame, initializes game variables, and creates game objects
        """
        # setup pygame data
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
        
        self.score1 = 0
        self.score2 = 0
        
        self.is_menu = True

    def mainloop(self):
        """
        Main Game loop
        Handles events, updates game state, and draws game objects
        """
        self.menu_loop()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Get the state of the keys
            keys = pygame.key.get_pressed()

            # Move paddle 1
            if keys[pygame.K_w]:
                self.paddle1.move(-self.paddle_speed)
            if keys[pygame.K_s]:
                self.paddle1.move(self.paddle_speed)

            # Move paddle 2
            if keys[pygame.K_UP]:
                self.paddle2.move(-self.paddle_speed)
            if keys[pygame.K_DOWN]:
                self.paddle2.move(self.paddle_speed)

            # Update game state and draw objects
            self.update()
            self.draw()

            # Check game over condition
            if self.score1 >= 3 or self.score2 >= 3:
                self.gameoverloop()

            self.clock.tick(60)

    
    def menu_loop(self):
        """
        Displays the main menu and waits for the player to start the game by pressing the spacebar.
        """
        self.screen.fill((0, 0, 0))
        menu_font = pygame.font.Font(None, 50)
        menu_text = menu_font.render("Press Space to Start Playing Pong!", True, (255, 255, 255))
        menu_rect = menu_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(menu_text, menu_rect)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                        self.is_menu = False

    def update(self):
        """
        Updates the game state
        Moves the ball, checks for collisions, and updates scores
        """
        self.ball.move()

        # Check collision with paddles
        if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
            self.ball.speed_x *= -1

        # Check collision with walls
        if self.ball.y <= 0 or self.ball.y + self.ball.radius * 2 >= self.screen_height:
            self.ball.speed_y *= -1

        # Check if ball goes out of bounds and update scores
        if self.ball.x <= 0:
            self.score2 += 1
            self.ball.reset()
        elif self.ball.x >= self.screen_width:
            self.score1 += 1
            self.ball.reset()
            
        if self.score1 >= 2:
                self.gameoverloop()

    def draw(self):
        """
        Draws game objects onto the screen
        """
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        score_text = self.font.render(f"{self.score1} - {self.score2}", True, (255, 255, 255))
        self.screen.blit(score_text, (self.screen_width // 2 - score_text.get_width() // 2, 10))
        pygame.display.flip()

    def gameoverloop(self):
        """
        Displays the game over message and final scores
        Waits for a moment before restarting the game
        """
        # Display game over message and final scores
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 2 - game_over_text.get_height() // 2))

        final_score_text = self.font.render(f"Final Score: {self.score1} - {self.score2}", True, (255, 255, 255))
        self.screen.blit(final_score_text, (self.screen_width // 2 - final_score_text.get_width() // 2, self.screen_height // 2 + game_over_text.get_height()))

        pygame.display.flip()

        # Wait for a moment before restarting the game
        pygame.time.wait(4000)

        # Reset scores and ball position
        self.score1 = 0
        self.score2 = 0
        self.ball.reset()
