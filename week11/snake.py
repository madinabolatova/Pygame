import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
font_style = pygame.font.SysFont("times-new-roman", 50)
score_font = pygame.font.SysFont("times-new-roman", 35)


class Food:
    def __init__(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

    def gen(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

    def draw(self):
        #pygame.draw.rect(screen, (139, 0, 0), (self.x, self.y, 15, 15))
        self.image = pygame.image.load("apple.png")
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center=(random.randint(40, 560), 0))
        screen.blit(self.image, (self.x, self.y))


class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.is_add = False
        self.speed = 10

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def eat(self, food_x, food_y):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if food_x <= x <= food_x + 35 and food_y <= y <= food_y + 35:
            return True
        return False


def message(words, color):
    words = font_style.render(words, True, color)
    screen.blit(words, [250, 250])


def display_score(score):
    value = score_font.render("Your score: " + str(score), True, (255, 215, 0))
    screen.blit(value, [0, 0])


snake1 = Snake(100, 100)
snake2 = Snake(150, 100)
food = Food()

running = True
game_over = False

d = 5
FPS = 30

clock = pygame.time.Clock()


def menu():
    menu_background = pygame.image.load("menu.jpg")

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(menu_background, (0, 0))


while running:
    clock.tick(30)
    while game_over == True:
        screen.fill((64, 224, 208))
        message("game over!", (255, 225, 255))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d

    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        pygame.mixer.Sound('Sound_crunch.wav').play()
        time.sleep(1)
        food.gen()

    if snake2.eat(food.x, food.y):
        snake2.is_add = True
        pygame.mixer.Sound('Sound_crunch.wav').play()
        time.sleep(1)
        food.gen()

    if snake1.elements[0][0] >= 800 or snake1.elements[0][0] < 0 or snake1.elements[0][1] >= 600 or snake1.elements[0][1] < 0:
        game_over = True

    if snake2.elements[0][0] >= 800 or snake2.elements[0][0] < 0 or snake2.elements[0][1] >= 600 or snake2.elements[0][1] < 0:
        game_over = True

    display_score(snake1.size - 1)
    display_score(snake2.size - 1)
    snake1.move()
    snake2.move()
    screen.fill((175, 215, 70))
    snake1.draw()
    snake2.draw()
    food.draw()
    pygame.display.flip()

pygame.quit()