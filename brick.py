
import pygame,sys,random,math,shelve
from pygame.locals import *



def level_1(level,lives):
    DISPLAYSURF.fill(blue)
    pad = pygame.Rect(600,900,100,20)
    left = False
    right = False
    start = False
    mag = False
    angle = 60
    pad_sp = 50
    ball_sp = 9
    x_sp = ball_sp*math.cos(math.radians(angle))
    y_sp = -ball_sp*math.sin(math.radians(angle))
    x_dir,y_dir = 1,-1
    bricks = []
    outlines = []
    col = []
    pow = []
    type = []
    if level == 1:
        for i in range(8):
            for j in range(10):
                if j == 3 or j == 6:
                    continue
                b = pygame.Rect(2+130*j,2+50*i,126,46)
                bricks.append(b)
                b = pygame.Rect(130*j,50*i,130,50)
                outlines.append(b)
                if i == 7:
                    col.append(red)
                else:
                    col.append(yellow)
    elif level == 2:
        for i in range(8):
            for j in range(10):
                if i <=3:
                    p = i
                else:
                    p = 7-i
                if j >= 4-p and j <= 5+p:
                    b = pygame.Rect(2+130*j,2+50*i,126,46)
                    bricks.append(b)
                    b = pygame.Rect(130*j,50*i,130,50)
                    outlines.append(b)
                    if j == 4-p or j == 5+p:
                        col.append(red)
                    else:
                        col.append(yellow)
    for i in range(len(outlines)):
        pygame.draw.rect(DISPLAYSURF,black,outlines[i])
    for i in range(len(bricks)):
        pygame.draw.rect(DISPLAYSURF,col[i],bricks[i])
    pygame.draw.rect(DISPLAYSURF,black,pad)
    ball = pygame.Rect(640,880,20,20)
    pygame.display.update()
    sw = []
    inc = []
    shield = pygame.Rect(0,1100,1300,20)
    while True:
        for i in range(len(sw)):
            if inc[i] == True:
                sw[i] = sw[i] + 1
        for i in range(len(sw)):
            if sw[i] == 1850:   #1000 = 10 sec, adjust accordingly
                if type[i] == 1:
                    pad[2] = 100
                if type[i] == 2:
                    shield = pygame.Rect(0,1100,1300,20)
                if type[i] == 4:
                    mag = False
                sw.pop(i)
                pow.pop(i)
                type.pop(i)
                inc.pop(i)
                break
        if lives == 0:
            DISPLAYSURF.fill(blue)
            pygame.draw.rect(DISPLAYSURF,blue,(600,480,200,40))
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('Game over', True, green, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (700, 500)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            return 0
        if len(bricks) == 0:
            DISPLAYSURF.fill(blue)
            pygame.draw.rect(DISPLAYSURF,red,(600,480,200,40))
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('Level passed', True, green, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (700, 500)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            pygame.time.delay(3000)
            return lives
        DISPLAYSURF.fill(blue)
        if start == False and mag == True:
            DISPLAYSURF.fill(blue)
            diff = (ball[0]+10) - (pad[0]+(pad[2]/2))
            angle = 7*diff
            angle = angle/5
            pad_sp = 5
            x_sp = ball_sp*math.sin(math.radians(angle))
            y_sp = -ball_sp*math.cos(math.radians(angle))
            for i in range(len(outlines)):
                pygame.draw.rect(DISPLAYSURF,blue,outlines[i])
            for i in range(len(bricks)):
                pygame.draw.rect(DISPLAYSURF,col[i],bricks[i])
            pygame.draw.rect(DISPLAYSURF,black,pad)
            pygame.draw.circle(DISPLAYSURF,white,(ball[0]+10,ball[1]+10),10)
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('Lives: '+str(lives), True, green, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (950, 950)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.draw.rect(DISPLAYSURF,green,shield)
            for i in range(len(pow)):
                if type[i] == 1:
                    pygame.draw.rect(DISPLAYSURF,green,pow[i])
                elif type[i] == 2:
                    pygame.draw.rect(DISPLAYSURF,black,pow[i])
                elif type[i] == 3:
                    pygame.draw.rect(DISPLAYSURF,red,pow[i])
                elif type[i] == 4:
                    pygame.draw.rect(DISPLAYSURF,white,pow[i])
            pygame.display.update()
        if start == False and mag == False:
            DISPLAYSURF.fill(blue)
            pow = []
            sw = []
            inc = []
            type = []
            pad_sp = 4
            ball_sp = 5
            x_sp = ball_sp*math.sin(math.radians(angle))
            y_sp = -ball_sp*math.cos(math.radians(angle))
            for i in range(len(outlines)):
                pygame.draw.rect(DISPLAYSURF,blue,outlines[i])
            for i in range(len(bricks)):
                pygame.draw.rect(DISPLAYSURF,col[i],bricks[i])
            pygame.draw.rect(DISPLAYSURF,black,pad)
            ball = pygame.Rect(pad[0]+40,880,20,20)
            pygame.draw.circle(DISPLAYSURF,white,(ball[0]+10,ball[1]+10),10)
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('Lives: '+str(lives), True, green, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (950, 950)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    start = True
                if event.key == K_LEFT:
                    left = True
                elif event.key == K_RIGHT:
                    right = True
            if event.type == KEYUP:
                left = False
                right = False
        if left == True and pad.left > 0:
            pad = pad.move(-pad_sp,0)
            if mag == True and (ball[1] >=875 and ball[1] <=885):
                ball = ball.move(-pad_sp,0)
        if right == True and pad.right < 1300:
            pad = pad.move(pad_sp,0)
            if mag == True and (ball[1] >=875 and ball[1] <=885):
                ball = ball.move(pad_sp,0)
        pygame.draw.rect(DISPLAYSURF,black,pad)
        if start == True:
            if ball[0] >= 1280 or ball[0] <= 0:
                x_dir = -x_dir
            if ball[1] <= 0:
                y_dir = 1
            if ball[1] >= 1000:
                start = False
                lives = lives - 1
                continue
            if ball.colliderect(shield):
                y_dir = -y_dir
            if ball.colliderect(pad):
                if y_dir == 1:
                    diff = (ball[0]+10) - (pad[0]+(pad[2]/2))
                    if diff > 50:
                        diff = 47
                    elif diff < -50:
                        diff = -47
                    ang = angle
                    angle = (180 - angle)%360
                    angle = angle - diff
                    if angle < 0:
                        angle = -angle
                    y_dir = -1
                    if diff > 0 and x_dir == -1:
                        x_dir = 1
                    if diff < 0 and x_dir == 1:
                        x_dir = -1
                    for j in range(len(type)):
                        if type[j] == 4 and inc[j] == True:
                            start = False
                            mag = True
            if ball.collidelist(bricks) != -1:
                i = ball.collidelist(bricks)
                temp = random.randrange(1,9)
                if col[i] == yellow:
                    #print(temp)
                    if temp == 1:
                        y = random.randrange(1,5)
                        qt = 0
                        for j in range(len(pow)):
                            if type[j] == y:
                                qt = 1
                        if qt == 0:
                            pow.append(pygame.Rect(bricks[i][0]+65,bricks[i][1]+25,20,20))
                            inc.append(False)
                            type.append(y)
                            sw.append(0)
                if abs(bricks[i][1]+46-ball[1]) < ball_sp or abs(ball[1]+20-bricks[i][1]) < ball_sp:
                    temp_int = 0
                    for j in range(len(type)):
                        if type[j] == 3 and inc[j] == True:
                            temp_int = 1
                    if temp_int == 0:
                        y_dir = -y_dir
                if abs(ball[0]+20-bricks[i][0]) < ball_sp or abs(bricks[i][0]+126-ball[0]) < ball_sp:
                    temp_int = 0
                    for j in range(len(type)):
                        if type[j] == 3 and inc[j] == True:
                            temp_int = 1
                    if temp_int == 0:
                        x_dir = -x_dir
                if col[i] == yellow:
                    outlines.pop(i)
                    col.pop(i)
                    bricks.pop(i)
                elif col[i] == red:
                    col[i] = yellow
            x_sp = ball_sp*x_dir*abs(math.sin(math.radians(angle)))
            y_sp = ball_sp*y_dir*abs(math.cos(math.radians(angle)))
            if abs(y_sp) < 1:
                y_sp = -1
                angle = math.acos(y_sp/math.sqrt(x_sp*x_sp+y_sp*y_sp))
                angle = 180*angle/math.pi
                x_sp = ball_sp*x_dir*abs(math.sin(math.radians(angle)))
            ball = ball.move(x_sp,y_sp)
            for i in range(len(pow)):
                if pad.colliderect(pow[i]):
                    if type[i] == 1:
                        pow[i].top = 1000
                        pad[2] = 175
                    elif type[i] == 2:
                        pow[i].top = 1000
                        shield[1] = 920
                    pow[i].top = 1000
                    inc[i] = True
                    break
            for i in range(len(pow)):
                if i > len(pow):
                    break
                if len(pow) == 0:
                    break
                if type[i] == 1:
                    pygame.draw.rect(DISPLAYSURF,green,pow[i])
                elif type[i] == 2:
                    pygame.draw.rect(DISPLAYSURF,black,pow[i])
                elif type[i] == 3:
                    pygame.draw.rect(DISPLAYSURF,red,pow[i])
                elif type[i] == 4:
                    pygame.draw.rect(DISPLAYSURF,white,pow[i])
                pow[i].top = pow[i].top + 2
                if pow[i].top >= 1000 and inc[i] == False:
                    pow.pop(i)
                    inc.pop(i)
                    type.pop(i)
                    sw.pop(i)
                    break
            pygame.draw.circle(DISPLAYSURF,white,(ball[0]+10,ball[1]+10),10)
            for i in range(len(outlines)):
                pygame.draw.rect(DISPLAYSURF,blue,outlines[i])
            for i in range(len(bricks)):
                pygame.draw.rect(DISPLAYSURF,col[i],bricks[i])
            pygame.draw.rect(DISPLAYSURF,green,shield)
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            textSurfaceObj = fontObj.render('Lives: '+ str(lives), True, green, blue)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (950, 950)
            DISPLAYSURF.blit(textSurfaceObj,textRectObj)
            pygame.display.update()
            mainClock.tick(140)


pygame.init()
mainClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1300,1000))
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
level = 1
lives = 3
a = 0

while True:
    if a == 0:
        DISPLAYSURF.fill(black)
        button = pygame.draw.rect(DISPLAYSURF,red,(550,480,200,40))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Start', True, green, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (650, 500)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    else:
        DISPLAYSURF.fill(black)
        button = pygame.draw.rect(DISPLAYSURF,red,(550,480,200,40))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Next level', True, green, red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (650, 500)
        DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if button.collidepoint(mouse):
                lives = level_1(level,lives)
                if lives > 0:
                    level = level + 1
