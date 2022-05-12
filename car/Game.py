import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0


font = pygame.font.SysFont("times-new-roman", 60)
font_small = pygame.font.SysFont("times-new-roman", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("GAME")

coinIcon = pygame.image.load('coin.png')
dX = random.randint(50, 350)
dY = random.randint(10, 300)
dX_change = 0
dY_change = 5
score_coins = 0

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)


def coin(x, y):
    SCREEN.blit(coinIcon, (x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.randint(1, 5)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH-40), 0))

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if(self.rect.bottom > 600):
            SCORE += 1
            self.speed = random.randint(1, 5)
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 40:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH - 40:
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN.blit(scores, (10, 10))
    coins_scores = font_small.render(str(score_coins), True, BLACK)
    SCREEN.blit(coins_scores, (370, 10))

    for entity in all_sprites:
        SCREEN.blit(entity.image, entity.rect)
        entity.move()

    dY += dY_change

    if dY > 600:
        dX = random.randint(40, 350)
        dY = random.randint(10, 300)

    coin(dX, dY)

    if P1.rect.collidepoint(dX+10, dY+10):
        score_coins += 1
        dX = random.randint(40, 350)
        dY = random.randint(10, 300)

    coins_scores = font_small.render(str(score_coins), True, BLACK)
    SCREEN.blit(coins_scores, (590, 10))

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        SCREEN.fill((0, 126, 78))
        SCREEN.blit(game_over, (60, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(60)