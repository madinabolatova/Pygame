import pygame
import math

pygame.init()

#RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (500, 500)

display = pygame.display.set_mode(size)

pygame.display.set_caption("Pygame example")


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(WHITE)

        pygame.draw.line(display, GREEN, [0, 0], [100, 100], 5)
        for y in range(0, 100, 10):
            pygame.draw.line(display, RED, [0, 10 + y], [100, 110 + y], 2)

        pygame.draw.rect(display, BLACK, [20, 20, 250, 100], 2)

        pygame.draw.ellipse(display, GREEN, [20, 100, 250, 100], 2)

        pygame.draw.arc(display, (100, 100, 100), [20, 200, 250, 100], 0, math.pi/2, 2)
        pygame.draw.arc(display, GREEN, [20, 200, 250, 100], math.pi/2, math.pi, 2)
        pygame.draw.arc(display, RED, [20, 200, 250, 100], math.pi, 3 * math.pi/2, 2)
        pygame.draw.arc(display, BLUE, [20, 200, 250, 100], 3 * math.pi/2, 2 * math.pi, 2)

        fond = pygame.font.Font(None, 50)
        text1 = fond.render("My text", True, RED)
        text2 = fond.render("My text", False, RED)
        display.blit(text1, (250, 250))
        display.blit(text2, (250, 300))

        fond = pygame.font.SysFont("Calibri", 25, True, False)
        text = fond.render("PP2", True, BLACK)
        text = pygame.transform.rotate(text, 90)
        display.blit(text, (0, 0))

        pygame.display.update()


run_game()