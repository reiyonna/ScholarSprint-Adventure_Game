import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Finger-Head Game")

# Load images
face_images = [
    pygame.image.load("assets/up.jpg"),
    pygame.image.load("assets/right.jpg"),
    pygame.image.load("assets/down.jpg"),
    pygame.image.load("assets/left.jpg"),
]

finger_images = [
    pygame.image.load("assets/finger point up.jpeg"),
    pygame.image.load("assets/download.png"),
    pygame.image.load("assets/finger point down.png"),
    pygame.image.load("assets/left point.jpeg"),
]

# Load GIFs
karl_losing_gif = pygame.image.load("assets/Karl_losing.gif")
karl_wins_gif = pygame.image.load("assets/Karl_wins.gif")
header_image = pygame.image.load("img/CIA_Text.png")
# Load font
font = pygame.font.Font(None, 36)

# Game variables
player_input = 0
comp_input = 0
rounds = 0
player_wins = 0
comp_wins = 0

# Function to change face direction randomly
def change_face_direction():
    return random.randint(0, 3)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_input = 0
                comp_input = change_face_direction()
            elif event.key == pygame.K_RIGHT:
                player_input = 1
                comp_input = change_face_direction()
            elif event.key == pygame.K_DOWN:
                player_input = 2
                comp_input = change_face_direction()
            elif event.key == pygame.K_LEFT:
                player_input = 3
                comp_input = change_face_direction()

    # Fill the screen with a background color to clear the face
    screen.fill((255, 255, 255))
    screen.blit(header_image, (width // 2 - header_image.get_width() // 2, 10))

    # Display player and computer choices
    screen.blit(finger_images[player_input], (50, 50))
    screen.blit(face_images[comp_input], (width - 250, 50))

    # Compare choices and render the result text and GIF
    if player_input == comp_input:
        if rounds % 2 == 1:
            comp_wins += 1
            screen.blit(karl_losing_gif, (width // 2 - karl_losing_gif.get_width() // 2, height - 200))
        else:
            player_wins += 1
            screen.blit(karl_wins_gif, (width // 2 - karl_wins_gif.get_width() // 2, height - 200))

    # Update display
    pygame.display.flip()

    # Add a delay to make it playable
    pygame.time.delay(1000)
