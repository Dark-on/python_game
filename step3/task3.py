import pygame
import math


PI = math.pi

pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("First Game")

cir_colour = (255, 155, 100)

x = 350
y = -50
move_x = -0.1

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((100, 100, 255))

    pygame.draw.circle(window, cir_colour, (x, y), 50)
    y += 0.03
    x += move_x
    
    if x <= 50 or x >= 350:
        move_x = -move_x
        

    pygame.display.update()
    

pygame.quit()
