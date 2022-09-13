import pygame


pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My game")

# -------colours---------------
PINK = (255, 100, 100)
BLUE = (80, 80, 190)
GREEN = (10, 90, 10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 10)
AQUA = (100, 255, 255)
VIOLET = (255, 100, 255)

x = 50
y = 350

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(GREEN)
    pygame.draw.circle(win, PINK, (x, y), 50)
    x = x + 0.1
    y = y - 0.1
    pygame.display.update() 


# закриття вікна
pygame.quit()

# colour picker
