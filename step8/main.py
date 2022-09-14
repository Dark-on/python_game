# 0. Зробити щоб гравець ходив із затиснутою клавішею
# 1. Оптимізувати рамки

import pygame


pygame.init()
win_width = 400
win_height = 400
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

bg_colour = (0, 0, 0) # чорний
rec_colour = (0, 255, 255)


run = True
x = 100
y = 100
width = 100
height = 100
speed = 0.05

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
##        elif event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_RIGHT:
##                x += 100
##            elif event.key == pygame.K_LEFT:
##                x -= 100
##            elif event.key == pygame.K_UP:
##                y -= 100
##            elif event.key == pygame.K_DOWN:
##                y += 100
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < win_width - 5 - width:
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < win_height - 5 - height:
        y += speed

        

    rec_colour = (0, 255, 255)

    win.fill(bg_colour)
    
    pygame.draw.rect(win, rec_colour, (x, y, width, height))
    
    pygame.display.update()

pygame.quit()
