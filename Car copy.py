import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000,700
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")


# Initialize Pygame mixer
pygame.mixer.init()

# Load background music
pygame.mixer.music.load("background_music.mp3")  # Replace with your music file


#Load background image
background = pygame.image.load("road.png")  # Replace with your road image


#Load docter image
enemy = pygame.image.load("docter.png")

#Load Car image
car_image = pygame.image.load("littledragon.png") 


# Get car image dimensions
car_width, car_height = 230, 360
car_image = pygame.transform.scale(car_image, (car_width, car_height))

# Change the dimensions of the enemy car
enemy_width, enemy_height = 160, 250
enemy = pygame.transform.scale(enemy, (enemy_width, enemy_height))


#background size
background_width, background_height = 1000, 700
background = pygame.transform.scale(background, (background_width, background_height))


# Initialize car position
car_x = WIDTH // 2 - car_width // 2
car_y = HEIGHT - car_height - 70


# Initialize enemy car position
enemy_width, enemy_height = 130, 220
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3

# Initialize score
score = 0

# Function to display score
def display_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

# Game loop
clock = pygame.time.Clock()
game_over_flag = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, HEIGHT))  # Road color
    display_score(score)

        # Clear the screen and draw the road background
    screen.blit(background, (0, 0))


    # Draw car and enemy car on top of the road
    screen.blit(car_image, (car_x, car_y))


    #pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    screen.blit(enemy, (enemy_x, enemy_y))



    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= 5
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += 5

    # Update enemy car position
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = -enemy_height


    # Check for collision
    pygame.display.flip()
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    if car_rect.colliderect(enemy_rect):
        running = True

        # Display game over screen
    #font = pygame.font.Font(None, 36)
    #game_over_text = font.render("Game Over", True, RED)
    #play_again_text = font.render("1 - Play Again | 2 - Exit", True, BLACK)
    #screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 20))
    #screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 20))


        
     #Draw car and enemy car
    screen.blit(car_image, (car_x, car_y))


    #pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    screen.blit(enemy, (enemy_x, enemy_y))

 
    # Update the display
    pygame.display.flip()


# Handle user input after game over
while game_over_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:  # Play again
        game_over_flag = False
        car_x = WIDTH // 2 - car_width // 2
        car_y = HEIGHT - car_height - 20
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = -enemy_height
        score = 0  # Reset score
    elif keys[pygame.K_2]:  # Exit
        running = False




    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()


