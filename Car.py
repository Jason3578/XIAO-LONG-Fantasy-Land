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


hamburger = pygame.image.load("hamburger.png")
icecream = pygame.image.load("icecream.png")
pizza = pygame.image.load("pizza.png")


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


# Define the dimensions of the food objects
food_width, food_height = 50, 50
hamburger = pygame.transform.scale(hamburger, (food_width, food_height))
icecream = pygame.transform.scale(icecream, (food_width, food_height))
pizza = pygame.transform.scale(pizza, (food_width, food_height))

# Initialize food objects position and status
food_objects = []

# Initialize score
score = 0
# Constants for point values of food items
PIZZA_POINTS = 10
ICECREAM_POINTS = 20
HAMBURGER_POINTS = 30

# Define the speed of food objects
# TODO: you may change food speed here
food_speed = 2

# Function to create a random food object
def create_food():
    # TODO: you may change where food spawn here
    food_choices = [hamburger, icecream, pizza]
    food_image = random.choice(food_choices)
    food_x = random.randint(0, WIDTH - food_width)
    food_y = random.randint(0, HEIGHT - food_height)
    food_objects.append([food_image, food_x, food_y])

# Function to display and handle food objects
def update_food_objects():
    global food_objects
    for i in range(len(food_objects)):
        food_objects[i][2] += food_speed
        if food_objects[i][2] > HEIGHT:
            food_objects.pop(i)  # Remove food objects that are out of the screen
            break
        else:
            screen.blit(food_objects[i][0], (food_objects[i][1], food_objects[i][2]))

# Function to check for collisions between car and food objects
def check_collisions(car_rect):
    global score, food_objects

    for i in range(len(food_objects)):
        food_rect = pygame.Rect(food_objects[i][1], food_objects[i][2], food_width, food_height)
        if car_rect.colliderect(food_rect):
            # Increase the score based on the food type
            if food_objects[i][0] == hamburger:
                score += HAMBURGER_POINTS
            elif food_objects[i][0] == icecream:
                score += ICECREAM_POINTS
            elif food_objects[i][0] == pizza:
                score += PIZZA_POINTS
            # Remove the food object from the list
            food_objects.pop(i)
            break

# Function to display score
def display_score(score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (100, 100))

# Game loop
clock = pygame.time.Clock()
game_over_flag = False
running = True

# Play background music
pygame.mixer.music.play(-1)  # -1 loops the music indefinitely

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_over_flag:
        # Display game over screen
        title_font = pygame.font.Font(None, 69)
        font = pygame.font.Font(None, 36)
        game_over_text = title_font.render("Game Over", True, RED)
        play_again_text = font.render("1 - Play Again | 2 - Exit", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 20))

        # Update the display
        pygame.display.flip()

        #Handle user input after game over
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:  # Play again
            game_over_flag = False
            car_x = WIDTH // 2 - car_width // 2
            car_y = HEIGHT - car_height - 20
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_y = -enemy_height
            score = 0  # Reset score
            food_objects = []
        elif keys[pygame.K_2]:  # Exit
            running = False

    else:

        #Clear the screen
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, HEIGHT))  # Road color

        # Clear the screen and draw the road background
        screen.blit(background, (0, 0))

        #Display background
        display_score(score)


        # Draw car and enemy car on top of the road
        screen.blit(car_image, (car_x, car_y))


        #pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
        screen.blit(enemy, (enemy_x, enemy_y))

        # Spawn food objects with a certain probability
        if random.random() < 0.01:
            create_food()

        # Update food objects
        update_food_objects()

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
        car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        # Check for collisions with food objects
        check_collisions(car_rect)
        if car_rect.colliderect(enemy_rect):
            game_over_flag = True

        #Draw car and enemy car
        screen.blit(car_image, (car_x, car_y))

        #pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
        screen.blit(enemy, (enemy_x, enemy_y))

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)

# Quit the game
pygame.quit()
