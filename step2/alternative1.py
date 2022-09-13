import pygame
import math

PI = math.pi


# ініціалізація гри
pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("First Game")

bg_colour = (0, 0, 0) # чорний
rec_colour = (0, 255, 255)
cir_colour = (255, 255, 0)
line_colour = (255, 0, 255)

run = True
x = 100
y = 100
width = 100
height = 100

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill(bg_colour)
    
##    pygame.draw.rect(вікно, колір, (x, y, ширина, довжина))
    pygame.draw.rect(win, rec_colour, (x, y, 100, 100))
##    pygame.draw.circle(вікно, колір, (x_center, y_center), radius)
    pygame.draw.circle(win,  cir_colour, (250, 50), 50)
##    line(surface, color, start_pos, end_pos)
    pygame.draw.line(win, line_colour, (100, 300), (200, 350), 4)
    pygame.draw.arc(win, line_colour, (200, 200, 350, 300), PI/2, PI, 2)
    
    pygame.display.update()

pygame.quit()
