import pygame


pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("My game")

PINK = (255, 100, 100)
BLUE = (100, 100, 255)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 170)
AQUA = (100, 255, 255)
VIOLET = (255, 100, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((30, 20, 150))

    pygame.draw.rect(win, BLACK, (50, 200, 100, 200))
    pygame.draw.rect(win, BLACK, (200, 300, 70, 100))
    pygame.draw.rect(win, BLACK, (300, 230, 80, 170))
    pygame.draw.circle(win, YELLOW, (250, 100), 40)
    pygame.draw.line(win, BLACK, (130, 150), (130, 200), 5)
    pygame.draw.line(win, BLACK, (110, 180), (150, 180), 5)
    pygame.draw.line(win, BLACK, (120, 170), (140, 170), 5)
    pygame.draw.line(win, BLACK, (110, 160), (150, 160), 5)


##    pygame.draw.polygon(win, BLACK, [(), (), (), (), ()])
    
    
    
##    pygame.draw.circle(win, WHITE, (200, 200), 100)
##    pygame.draw.circle(win, YELLOW, (220, 200), 40)

##    pygame.draw.line(win, VIOLET, (350, 50), (300, 200), 6)
##    pygame.draw.polygon(win, GREEN, [(50, 200), (100, 210), (70, 300)])
##    
    pygame.display.update() 


# закриття вікна
pygame.quit()

# colour picker






