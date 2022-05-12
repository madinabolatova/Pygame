import pygame

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

text_rotate_degrees = 1
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    display.fill(WHITE)
    fond = pygame.font.SysFont("Calibri", 25, True, False)
    text = fond.render("PP2", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    display.blit(text, (100, 100))
    text_rotate_degrees += 1
    clock.tick(60)
    pygame.display.flip()

pygame.quit()