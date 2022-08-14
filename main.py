import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 50
snake_y = 50
velocity_x = 0
velocity_y = 0
init_velocity = 10
snake_size = 10
food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)
food_size = 10
score = 0
fps = 30

font = pygame.font.SysFont(None, 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(window, color, snk_list1, snake_size1):
    for x, y in snk_list1:
        pygame.draw.rect(window, color, [x, y, snake_size1, snake_size1])


snk_list = []
snk_length = 1

clock = pygame.time.Clock()
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -init_velocity

            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = init_velocity

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    # if snake_x > screen_width or snake_x < 0 or snake_y > screen_height or snake_y < 0:
    #     exit_game = True

    if snake_x > screen_width:
        snake_x = 0

    if snake_y > screen_height:
        snake_y = 0

    if snake_x < 0:
        snake_x = screen_width

    if snake_y < 0:
        snake_y = screen_height

    # if food_x <= snake_x <= food_x + food_size and food_y <= snake_y <= food_y + food_size:
    #     score = score + 1
    #     food_x = random.randrange(0, 900, 1)
    #     food_y = random.randrange(0, 600, 1)

    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score = score + 1
        food_x = random.randrange(0, 900, 1)
        food_y = random.randrange(0, 600, 1)
        snk_length = snk_length + 5

    gameWindow.fill(white)
    text_screen("score: " + str(score * 10), red, 5, 5)
    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)
print("score is : ", score)

pygame.quit()
quit()
