import pygame

pygame.init()

size = width, height = (400, 300)
display = pygame.display.set_mode(size)


def run_game():
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((255, 255, 255))
        pygame.display.update()


run_game()