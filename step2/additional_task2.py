import pygame


pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My game")

PINK = (255, 100, 100)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
AQUA = (100, 255, 255)
VIOLET = (255, 100, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((52, 102, 45))

    pygame.draw.circle(win, WHITE, (200, 200), 100)
    pygame.draw.circle(win, YELLOW, (220, 200), 40)

    pygame.display.update() 


# закриття вікна
pygame.quit()

# colour picker






