import pygame
import math


PI = math.pi

pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("First Game")
rec_colour = (255, 100, 100)
cir_colour = (100, 255, 100)
line_colour = (255, 255, 255)
arc_colour = (255, 255, 0)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((155, 34, 200))
    pygame.draw.rect(window, rec_colour, (50, 150, 50, 50))
    pygame.draw.circle(window, cir_colour, (200, 50), 50)
    pygame.draw.line(window, line_colour, (300, 350), (400, 390), 5)
    pygame.draw.line(window, (255, 100, 200), (100, 250), (150, 350), 100)
    pygame.draw.arc(window, arc_colour, (300, 50, 100, 150), 0, PI, 5)
    pygame.draw.polygon(window, (100, 100, 250),
                        [(10, 10), (100, 10), (100, 100)])
    pygame.draw.polygon(
        window, (200, 255, 250),
        [(210, 150), (300, 210), (300, 300), (200, 300), (150, 200)])
    
    pygame.display.update()
    

pygame.quit()
