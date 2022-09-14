# найпростіший рахунок балів (вивід балів у термінал) і вікно gameover

import pygame
from random import randint


pygame.init()
win_width = 800
win_height = 700
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("First Game")

walk_right = [pygame.image.load('../img/right1.png'),
              pygame.image.load('../img/right2.png'),
              pygame.image.load('../img/right3.png'),
              pygame.image.load('../img/right4.png'),
              pygame.image.load('../img/right5.png'),
              pygame.image.load('../img/right6.png')]

walk_left = [pygame.image.load('../img/left1.png'),
             pygame.image.load('../img/left2.png'),
             pygame.image.load('../img/left3.png'),
             pygame.image.load('../img/left4.png'),
             pygame.image.load('../img/left5.png'),
             pygame.image.load('../img/left6.png')]
front_img = pygame.image.load('../img/front.png')             
bg_img = pygame.image.load('../img/background.jpg')

BLACK = (0, 0, 0) 

run = True
width = 80
height = 100
x = 100
y = win_height - height - 75
speed = 5

clock = pygame.time.Clock()

isJump = False
jump_height = 30
jump_count = jump_height

left = False
right = False
anim_count = 0
points = 0

ball_pos_list = []

def draw_ball(ball_y, ball_count):
    global ball_pos_list
    if ball_count > len(ball_pos_list) - 1:
        ball_pos_list += [randint(win_width, win_width * 2)]
        
    ball_x = ball_pos_list[ball_count]
    if 0 <= ball_x: 
        pygame.draw.circle(win, BLACK, (ball_x, ball_y), 10)
        ball_pos_list[ball_count] -= 5
    else:
        ball_pos_list[ball_count] = randint(win_width, win_width * 2)

    return ball_x, ball_y

def draw_char():
    win.blit(bg_img, (0, 0))
    global anim_count, points
    if anim_count + 1 >= 30:
        anim_count = 0
        points += 1
    if left:
        win.blit(walk_left[anim_count // 5], (x, y))
        anim_count += 1
    elif right:
        win.blit(walk_right[anim_count // 5], (x, y))
        anim_count += 1
    else:
        win.blit(front_img, (x, y))
    

while run:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < win_width - 5 - width:
        x += speed
        right = True
        left = False
    else:
        right = False
        left = False
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jump_count >= -jump_height:
            y -= jump_count
            jump_count -= 1
        else:
            isJump = False
            jump_count = jump_height

    draw_char()
    for i in range(6):
        ball_x, ball_y = draw_ball(100 * (i + 1), i)
        if ball_x <= x + width and ball_x >= x and \
                ball_y <= y + height and ball_y >= y:
            win.blit(pygame.image.load('../img/bg_game_over.jpg'), (0, 0))
            pygame.display.update()
            run = False
            pygame.time.delay(300)
            break
            
    pygame.display.update()

pygame.quit()
print("==============Гра закінчена=============\n"
      "Ваші бали:", points * 30 + anim_count)
