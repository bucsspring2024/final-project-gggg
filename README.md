[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588114&assignment_repo_type=AssignmentRepo)



# Pong with Pygame
## CS110 Final Project Spring, 2024

## Team Members

Albi Dobrova

***

## Project Description

Classic Pong Game. 2 players that can move their paddles up and down with either W and S key, or UP and DOWN arrow keys. Goals are scored if the ball collides with a players respective side. The ball can bounce off the top and bottom walls and paddles through collision handling in pygame. There is a popup start menu screen that prompts the user to hit space bar to begin the game. After any player scores 1 goal, a game over screen is shown and the game window closes. The Final Score displayed at the end is taken from a json file that is both opened and read within the controller.
***    

## GUI Design

### Initial Design

![initial gui](assets/initialgui.png)

### Final Design

![final gui](assets/finalgui.png)

## Program Design

### Features

1. Player-controlled paddles: Players can move their paddles up and down to hit the ball.
2. Ball movement and collision: The ball moves continuously and bounces off the paddles and walls.
3. Score tracking: The game keeps track of each player's score as they successfully hit the ball past their opponent's paddle.
4. Game over condition: The game ends when one player reaches a predefined winning score limit.
5. Responsive user interface: The game provides clear feedback to players through visual elements such as paddle movement, ball trajectory, and score display.

## Classes

### Ball:
 This class defines a basic implementation for a ball object in Pygame. It initializes with an x and y coordinate, assigns a radius of 5, and sets initial speeds in both x and y directions. The move method updates the ball's position based on its speed, and the draw method renders the ball on a Pygame surface.

### Paddle:
 This class represents a paddle object in a Pygame environment. Upon initialization, it requires x and y coordinates, and sets default width and height values. The move method allows the paddle to move vertically by a specified amount (dy), adjusting both the paddle's position and its associated rectangle. Finally, the draw method renders the paddle on a Pygame surface.

## ATP

### Test 1 : Game Initialization

- Step 1: Launch the Pong game.
- Step 2: Verify that the game window opens with the correct dimensions.
- Step 3: Ensure that the paddles, ball, and score display are visible.
- Expected Outcome: The game initializes successfully with all game elements displayed correctly.

### Test 2: Paddle Movement

- Step 1: Start the game.
- Step 2: Use the arrow keys or designated keys to move the paddles up and down.
- Step 3: Verify that both paddles respond to input and move accordingly.
- Expected Outcome: Paddle movement controls are responsive and functional.

### Test 3: Ball Movement

- Step 1: Start the game.
- Step 2: Observe the movement of the ball.
- Step 3: Ensure that the ball moves continuously and bounces off the paddles and walls.
- Expected Outcome: The ball moves smoothly and interacts correctly with game elements.

### Test 4: Menu Pop-Up

- Step 1: Launch the Pong game.
- Step 2: Observe the initial game screen.
- Step 3: Verify that a menu pops up with the message "Press Space to Start Playing Pong!".
- Expected Outcome: A menu should appear at the beginning of the game, prompting the player to press the spacebar to start playing.

### Test 5: Collision Detection

- Step 1: Start the game.
- Step 2: Allow the ball to collide with one of the paddles.
- Step 3: Observe the behavior of the ball upon collision.
- Expected Outcome: When the ball collides with a paddle, it should change direction accordingly, bouncing off the paddle's surface without passing through it. This also goes for the top and bottom walls of the window.