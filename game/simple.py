import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (600, 600)
window_title = "Simple Game"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Set the background color
bg_color = (255, 255, 255)

# Create a player sprite
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# Set the player's starting position
player_rect.x = 300
player_rect.y = 300

# Set the player's speed
player_speed = 5

# Set the game's running flag to True
running = True

# Run the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check for keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    
    # Clear the screen
    screen.fill(bg_color)
    
    # Draw the player sprite
    screen.blit(player_image, player_rect)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
