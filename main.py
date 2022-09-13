import pygame

"""Створення вікна"""

# ініціалізація гри
pygame.init()
win = pygame.display.set_mode((400,400))
pygame.display.set_caption("First Game")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))
    pygame.display.update()

pygame.quit()
