import pygame


pygame.init()
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("First Game")

rec_colour = (255, 155, 100)

x = 0
y = 0
move_x = 0.1
move_y = 0.0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((100, 100, 255))

    pygame.draw.rect(window, rec_colour, (x, y, 100, 100))

    if x >= 300 and y <= 0:
        move_x = 0.0
        move_y = 0.1
    elif x >= 300 and y >= 300:
        move_x = -0.1
        move_y = 0.0
    elif x <= 0 and y >= 300:
        move_x = 0.0
        move_y = -0.1
    elif x <= 0 and y <= 0:
        move_x = 0.1
        move_y = 0.0
    
    x += move_x
    y += move_y

    pygame.display.update()
    
pygame.quit()
