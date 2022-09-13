import pygame


pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("First Game")

bg_colour = (80, 80, 190) 
cir_colour = (255, 255, 0)


run = True
x = 250
y = -100
radius = 50

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

                    
    win.fill(bg_colour)
    
    pygame.draw.circle(win, cir_colour, (x, y), radius)

    y += 0.01
    
    pygame.display.update() 

pygame.quit()
