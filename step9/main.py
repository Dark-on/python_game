# 0. Стрибки
# 1. Також видалити переміщення вгору-вниз,
#     змінити початкову координату

import pygame


pygame.init()
win_width = 400
win_height = 400
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

bg_colour = (0, 0, 0) # чорний
rec_colour = (0, 255, 255)


run = True
width = 100
height = 100
x = 100
y = win_height - height - 5
speed = 5

isJump = False
jump_count = 10

while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < win_width - 5 - width:
        x += speed
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -10:
            y -= jump_count
            jump_count -= 1
        else:
            isJump = False
            jump_count = 10

    rec_colour = (0, 255, 255)

    win.fill(bg_colour)
    
    pygame.draw.rect(win, rec_colour, (x, y, width, height))
    
    pygame.display.update()

pygame.quit()
