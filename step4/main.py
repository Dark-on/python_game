import pygame


pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("First Game")

bg_colour = (0, 0, 0) # чорний
rec_colour = (0, 255, 255)


run = True
x = 100
y = 100
width = 100
height = 100

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 100
            elif event.key == pygame.K_LEFT:
                x -= 100
                    
    win.fill(bg_colour)
    
    pygame.draw.rect(win, rec_colour, (x, y, width, height))
    
    pygame.display.update() 

pygame.quit()
