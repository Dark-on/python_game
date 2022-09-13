import pygame


pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("My game")

BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
PINK = (255, 100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255, 255, 255))
    

    pygame.draw.rect(win, BLUE, (50, 100, 150, 120))
    pygame.draw.circle(win, BLACK, (300, 200), 60)

    pygame.draw.rect(win, BLACK, (100, 300, 50, 50))
    pygame.draw.line(win, PINK, (350, 50), (300, 100), 8)

    pygame.draw.polygon(win, PINK, [(50, 360), (70, 340), (60, 300)])
    pygame.draw.polygon(win, PINK, [(500, 10), (590, 30), (520, 200), (450, 200), (410, 30)])

    
    pygame.display.update()



# закриття вікна
pygame.quit()





