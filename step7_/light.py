import pygame


pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My game")

# -------кольори---------------
PINK = (255, 100, 100)
BLUE = (10, 10, 200)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 10)
AQUA = (100, 255, 255)
VIOLET = (255, 100, 255)
RED = (255, 0, 0)

x = 0
y = 0
width = 100
height = 100
colour_rect = GREEN

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < 300:
                x += 100
            if event.key == pygame.K_LEFT and x > 0:
                x -= 100
            if event.key == pygame.K_UP and y > 0:
                y -= 100
            if event.key == pygame.K_DOWN and y < 300:
                y += 100


    win.fill(BLACK)
    if 0 <= y <= 100:
        colour_rect = GREEN
    else:
        colour_rect = RED
    pygame.draw.rect(win, colour_rect, (x, y, width, height))
    
    pygame.display.update() 


# закриття вікна
pygame.quit()

# colour picker
