import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario Maker 4-like Level Editor")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Tile settings
TILE_SIZE = 32
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Player settings
player_x = 100
player_y = 100
player_speed = 5
player_width = 32
player_height = 32

# Create a basic grid to represent the level (0 = empty, 1 = block)
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Load player image (placeholder)
player_img = pygame.Surface((player_width, player_height))
player_img.fill(BLUE)


# Function to draw the grid
def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, GREEN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))


# Function to move the player
def move_player(keys):
    global player_x, player_y

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed


# Function to handle tile placement (for grid editing)
def place_tile(mx, my):
    grid_row = my // TILE_SIZE
    grid_col = mx // TILE_SIZE

    # Toggle tile placement (empty <-> block)
    if grid_row < GRID_HEIGHT and grid_col < GRID_WIDTH:
        grid[grid_row][grid_col] = 1 if grid[grid_row][grid_col] == 0 else 0


# Main loop
def game_loop():
    global player_x, player_y
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Get events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mx, my = pygame.mouse.get_pos()
                    place_tile(mx, my)

        # Get keyboard input
        keys = pygame.key.get_pressed()
        move_player(keys)

        # Draw grid
        draw_grid()

        # Draw the player
        screen.blit(player_img, (player_x, player_y))

        # Update the screen
        pygame.display.flip()

        # Frame rate
        clock.tick(60)


# Run the game loop
game_loop()
