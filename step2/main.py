import pygame

# створює гру
pygame.init()
# створюємо вікно
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("First Game")

# перевірка чи натиснули хрестик
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((200, 250, 200))
    
    pygame.draw.rect(win, (50, 50, 50), (50, 100, 60, 70))
    pygame.draw.rect(win, (150, 150, 150), (100, 50, 30, 30))

    pygame.draw.circle(win, (150, 50, 50), (200, 220), 45)
    pygame.draw.line(win, (50, 50, 150), (50, 250), (300, 20), 6)
    pygame.draw.line(win, (50, 150, 50), (50, 300), (120, 350), 60)

    pygame.draw.arc(win, (50, 150, 150), (320, 320, 30, 60), 1, 4, 3)

    pygame.draw.polygon(win, (150, 150, 50), [(320, 50), (370, 70), (340, 100)])
    pygame.draw.polygon(win, (150, 50, 150),
                        [(320, 150), (390, 170), (380, 200), (340, 220), (327, 200)])
    
    pygame.display.update()
    
# закриває гру
pygame.quit()
