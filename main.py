import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption("Snake and Ladder")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load board image
board_img = pygame.image.load("board.jpg")
board_img = pygame.transform.scale(board_img,  (600, 600))





# Load font
font = pygame.font.Font(None, 36)

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# move player
def move_player(player, steps, direction):
    if direction == 1:  # 1 for positive direction
        player += steps
    elif direction == -1: # -1 for negative direction
        player -= steps
    return player

# ladder position
def check_ladder(player, name):
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    if player in ladders:
        print(f"****** {name} Climb Ladder at {player} ******")
        return ladders[player]

    return player

# Function to check if player landed on a snake
def check_snake(player, name):
    snakes = {17: 7, 54: 34, 64: 60, 62: 19, 87: 24, 93: 73, 95: 75, 98: 79}
    if player in snakes:
        print(f"-------- {name} Eaten by Snake at {player} --------")

        return snakes[player]

    return player

# Main game loop
def play_game():
    players = {"Player 1": {"position": 0, "direction": 1}, "Player 2": {"position": 0, "direction": 1}}
    current_player = "Player 1"
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice_roll = roll_dice()
                    current_player_data = players[current_player]
                    if current_player_data["position"] + dice_roll > 100:
                        if dice_roll != 6:
                            current_player = "Player 2" if current_player == "Player 1" else "Player 1"

                        break
                    else:
                        current_player_data["position"] = move_player(current_player_data["position"], dice_roll, current_player_data["direction"])
                        current_player_data["position"] = check_ladder(current_player_data["position"], current_player)
                        current_player_data["position"] = check_snake(current_player_data["position"], current_player)
                    print(f"{current_player} rolled a {dice_roll}")
                    print(f"{current_player} is now at position {current_player_data['position']}")

                    if current_player_data["position"] == 100:
                        print(f"Congratulations! {current_player} reached the finish line!")
                        running = False

                    # current player
                    if dice_roll != 6:
                        current_player = "Player 2" if current_player == "Player 1" else "Player 1"

        screen.fill(WHITE)
        screen.blit(board_img, (0, 50))

        # Display player positions on the board
        for player, data in players.items():
            position = data["position"]
            row = (position - 1) // 10
            col = (position - 1) % 10
            direction = data["direction"]
            if row % 2 == 0:
                x = 45 + col * 56 + 30 * (row % 2) + direction * 56 * (row % 2)  # Adjust x position
            else:
                x = 45 + (9 - col) * 56 + direction * 56 * ((row + 1) % 2)
            y = 605 - row * 58   # y position
            if player == "Player 1":
                pygame.draw.circle(screen, RED, (x, y), 15)
            elif player == "Player 2":
                pygame.draw.circle(screen, BLUE, (x, y), 15)

        # Display current player and position
        text_surface = font.render(f"{current_player}: Position {players[current_player]['position']}", True, BLACK)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    print("Welcome to Snake and Ladder!")
    play_game()
