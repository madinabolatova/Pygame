import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")
font_style = pygame.font.SysFont("times-new-roman", 50)
score_font = pygame.font.SysFont("times-new-roman", 35)

RED = (255, 0, 0)
BLUE = (0, 255, 255)


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (139, 0, 0), (self.x, self.y, 15, 15))

    def collide(self, snakes):
        for snake in snakes:
            x, y = snake.elements[-1]
            x -= snake.radius
            y -= snake.radius
            w = snake.radius * 2
            h = snake.radius * 2
            if x < self.x + 15 and x + w > self.x and y < self.y + 15 and y + h > self.y:
                return True
        return False


class Food:
    def __init__(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)

    def gen(self):
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)

    def draw(self):
        # pygame.draw.rect(screen, (139, 0, 0), (self.x, self.y, 15, 15))
        self.image = pygame.image.load("apple.png")
        self.surf = self.image.get_rect()
        print(self.surf)
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
            pygame.draw.circle(screen, RED, element, self.radius)

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

    def eat(self, food):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if food.x <= x <= food.x + 40 and food.y <= y <= food.y + 40:
            return True
        return False


def message(words, color):
    words = font_style.render(words, True, color)
    screen.blit(words, [100, 200])


def display_score(score):
    value = score_font.render("Your score: " + str(score), True, (255, 215, 0))
    screen.blit(value, [0, 0])


walls = []
for i in range(0, 800, 15):
    walls.append(Wall(i, 0))
snake1 = Snake(100, 100)
snake2 = Snake(150, 100)
food = Food()

running = True
game_over = True

d = 5
FPS = 30

clock = pygame.time.Clock()


def new_game_easy():
    global walls, snake2, snake1, food
    walls = []
    for i in range(0, 800, 15):
        walls.append(Wall(i, 0))
        walls.append(Wall(i, 585))
    for i in range(0, 600, 15):
        walls.append(Wall(785, i))
        walls.append(Wall(0, i))
    snake1 = Snake(100, 100)
    snake2 = Snake(150, 100)
    food = Food()


def new_game_meddium():
    global walls, snake2, snake1, food
    walls = []
    for i in range(0, 800, 15):
        walls.append(Wall(i, 0))
        walls.append(Wall(i, 585))
    for i in range(0, 600, 15):
        walls.append(Wall(785, i))
        walls.append(Wall(0, i))
    for i in range(200, 300, 15):
        for j in range(200, 300, 15):
            walls.append(Wall(i, j))
    snake1 = Snake(100, 100)
    snake2 = Snake(150, 100)
    food = Food()


def new_game_hard():
    global walls, snake2, snake1, food
    walls = []
    for i in range(0, 800, 15):
        walls.append(Wall(i, 0))
        walls.append(Wall(i, 585))
    for i in range(0, 600, 15):
        walls.append(Wall(785, i))
        walls.append(Wall(0, i))
    for i in range(200, 300, 15):
        for j in range(200, 300, 15):
            walls.append(Wall(i, j))
    for i in range(400, 800, 15):
        for j in range(300, 400, 15):
            walls.append(Wall(i, j))
    snake1 = Snake(100, 100)
    snake2 = Snake(150, 100)
    food = Food()


difficult = "easy"
while running:
    if not game_over:
        if difficult == "easy":
            new_game_easy()
        elif difficult == "medium":
            new_game_meddium()
        else:
            new_game_hard()
        pygame.display.flip()
    while not game_over:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
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
        for wall in walls:
            if wall.collide([snake1, snake2]):
                game_over = True

        if snake1.eat(food):
            snake1.is_add = True
            pygame.mixer.Sound('Sound_crunch.wav').play()
            time.sleep(1)
            food.gen()

        if snake2.eat(food):
            snake2.is_add = True
            pygame.mixer.Sound('Sound_crunch.wav').play()
            time.sleep(1)
            food.gen()

        if snake1.elements[0][0] >= 800 or snake1.elements[0][0] < 0 or snake1.elements[0][1] >= 600 or \
                snake1.elements[0][1] < 0:
            game_over = True

        if snake2.elements[0][0] >= 800 or snake2.elements[0][0] < 0 or snake2.elements[0][1] >= 600 or \
                snake2.elements[0][1] < 0:
            game_over = True

        display_score(snake1.size - 1)
        display_score(snake2.size - 1)
        snake1.move()
        snake2.move()
        screen.fill((175, 215, 70))
        snake1.draw()
        snake2.draw()
        food.draw()
        for wall in walls:
            wall.draw()
        pygame.display.flip()
    screen.fill((64, 224, 208))
    message("To start game press button!", (255, 225, 255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                difficult = "easy"
                game_over = False
            elif event.key == pygame.K_2:
                difficult = "medium"
                game_over = False
            elif event.key == pygame.K_3:
                difficult = "hard"
                game_over = False

pygame.quit()