import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Matching Game")

# Load images
folder_path = 'path/to/your/images'  # Change this to your folder path
images = [pygame.image.load(os.path.join(r"C:\Users\DELL\Documents\Python\Function\Internship Projects", f)) for f in os.listdir(r"C:\Users\DELL\Documents\Python\Function\Internship Projects") if f.endswith(('png', 'jpg', 'jpeg'))]
images = images[:8]  # Use only the first 8 images

# Duplicate and shuffle images
cards = images * 2
random.shuffle(cards)

# Constants
CARD_WIDTH, CARD_HEIGHT = 100, 100
GRID_SIZE = 4  # 4x4 grid
GRID_POS = [(x * (CARD_WIDTH + 10), y * (CARD_HEIGHT + 10)) for y in range(GRID_SIZE) for x in range(GRID_SIZE)]
revealed = [False] * len(cards)
selected = []

# Timer settings
TIME_LIMIT = 60  # 60 seconds
start_time = pygame.time.get_ticks()

def draw_card(image, pos):
    """Draws the card at the specified position, fitting the image inside."""
    rect = pygame.Rect(pos[0], pos[1], CARD_WIDTH, CARD_HEIGHT)
    pygame.draw.rect(screen, (0, 0, 0), rect)

    if image:
        image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
        img_rect = image.get_rect(center=rect.center)
        screen.blit(image, img_rect.topleft)

# Main game loop
running = True
game_over = False
win = False
remaining_time = TIME_LIMIT  # Initialize remaining time

while running:
    screen.fill((255, 255, 255))

    # Update remaining time only if the game is not over
    if not game_over and not win:
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        remaining_time = TIME_LIMIT - elapsed_time
        if remaining_time <= 0:
            game_over = True
            remaining_time = 0  # Ensure it doesn't go negative

    # Draw the cards
    for idx, (pos, revealed_state) in enumerate(zip(GRID_POS, revealed)):
        if revealed_state:
            draw_card(cards[idx], pos)
        else:
            draw_card(None, pos)

    # Check for win condition
    if all(revealed):
        win = True

    # Display timer
    font = pygame.font.Font(None, 36)
    timer_text = font.render(f"Time: {int(remaining_time)}", True, (0, 0, 0))
    screen.blit(timer_text, (WIDTH - 150, 10))

    # Display messages below the grid
    message_text = ""
    if game_over:
        message_text = "You lose! Try again!"
    elif win:
        message_text = "Great! You win!"

    if message_text:
        message_surface = font.render(message_text, True, (255, 0, 0) if game_over else (0, 255, 0))
        screen.blit(message_surface, (WIDTH // 2 - message_surface.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and not win:
            mouse_pos = event.pos
            for idx, pos in enumerate(GRID_POS):
                rect = pygame.Rect(pos[0], pos[1], CARD_WIDTH, CARD_HEIGHT)
                if rect.collidepoint(mouse_pos) and not revealed[idx]:
                    revealed[idx] = True
                    selected.append(idx)

                    if len(selected) == 2:
                        pygame.time.delay(1000)  # Pause for a moment
                        if cards[selected[0]] != cards[selected[1]]:
                            revealed[selected[0]] = revealed[selected[1]] = False
                        selected = []

pygame.quit()
