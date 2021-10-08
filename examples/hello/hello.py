import pygame
import random
def font():
    pygame.draw.rect(setup, (255,255,255), (0,0,(600//8)*8,(600//8)*8))
def rayV(x,y,rgb):
    pygame.draw.rect(setup, rgb, (x-5,-100,10,1200))
def rayH(x,y,rgb):
    pygame.draw.rect(setup, rgb, (-100,y-5,1200,10))
def bulletV(x,y,rgb):
    pygame.draw.rect(setup, rgb, (x-5,y-15,10,30))
def bulletH(x,y,rgb):
    pygame.draw.rect(setup, rgb, (x-15,y-5,30,10))
def player(x,y,rgb):
    pygame.draw.rect(setup, rgb,(x-2,y-2,4,4))
def phost(x,y):
    player(x,y,(0,0,248))
def pclient1(x,y):
    player(x,y,(248,0,0))
def typeShoot(n,x,y):
    rand = random.randrange(0,4)
    Type = random.randrange(0,4)
    if rand != 3:
        if Type == 0:
            Bcoord[n][0] = x+random.randrange(-10,11)
        if Type == 1:
            Bcoord[n][1] = y+random.randrange(-10,11)
        if Type == 2:
            Bcoord[n][0] = x+random.randrange(-10,11)
            Bcoord[n][1] = random.randrange(-20,621,640)
        if Type == 3:
            Bcoord[n][0] = random.randrange(-20,621,640)
            Bcoord[n][1] = y+random.randrange(-10,11)
    else:
        if Type == 0:
            Bcoord[n][0] = random.randrange(8,592)
        if Type == 1:
            Bcoord[n][1] = random.randrange(8,592)
        if Type == 2:
            Bcoord[n][0] = random.randrange(8,592)
            Bcoord[n][1] = random.randrange(-20,621,640)
        if Type == 3:
            Bcoord[n][0] = random.randrange(-20,621,640)
            Bcoord[n][1] = random.randrange(8,592)
    return Type
shoot = [rayV, rayH, bulletV, bulletH]

pygame.init()

setup = pygame.display.set_mode(((600//8)*8, (600//8)*8)) 
pygame.display.set_caption("game")
font()
xhost=(600//8)*3
yhost=(600//8)*3
phost(xhost, yhost)
run = True
moveHost = [-4,-3,-2,-1]
time=0
B=[-1,-1,-1,-1,-1,-1,-1]
xb1 = xb2 = xb3 = xb4 = xb5 = xb6 = xb7 = -1000
yb1 = yb2 = yb3 = yb4 = yb5 = yb6 = yb7 = -1000
gb1 = gb2 = gb3 = gb4 = gb5 = gb6 = gb7 = 120
test1 = test2 = test3 = test4 = test5 = test6 = test7 = 0
loop1 = loop2 = loop3 = loop4 = loop5 = loop6 = loop7 = 0
depl1 = depl2 = depl3 = depl4 = depl5 = depl6 = depl7 = 0
Bcoord = [[xb1,yb1],[xb2,yb2],[xb3,yb3],[xb4,yb4],[xb5,yb5],[xb6,yb6],[xb7,yb7]]
while run:
    for echec1 in range(xhost-2,xhost+3):
        for echec2 in range(yhost-2,yhost+3):
            if pygame.Surface.get_at(setup,(echec1,echec2)) == ((248,8,8,255)or(248,9,9,255)or(248,10,10,255)or(248,11,11,255)or(248,12,12,255)or(248,13,13,255)or(248,14,14,255)or(248,7,7,255)or(248,6,6,255)or(248,5,5,255)or(248,4,4,255)or(248,3,3,255)or(248,2,2,255)or(248,1,1,255)or(248,0,0,255)):
                run=False
    print(moveHost)
    print(Bcoord[0])
    time+=1
    print(time,B[2], test3, Bcoord[2])
    if time>= 2000 and B[0] == -1:
        B[0] = typeShoot(0,xhost,yhost)
        loop1 = 0
        gb1 = 120
    if B[0] > -1:
        if B[0] < 2:
            shoot[B[0]](Bcoord[0][0],Bcoord[0][1],(248,gb1,gb1,255))
            gb1 += 1
            if gb1 > 248:
                gb1 = 0 
                loop1 += 1
            if loop1 == 2:
                B[0] = -1
        else:
            if B[0] == 2:
                if test1 == 0:
                    if Bcoord[0][1] == -20:
                        depl1 = 2
                        test1 = 1
                    if Bcoord[0][1] == 720:
                        depl1 = -2
                        test1 = -1
                shoot[B[0]](Bcoord[0][0],Bcoord[0][1],(248,252,248,255))
                Bcoord[0][1] += depl1
                shoot[B[0]](Bcoord[0][0],Bcoord[0][1],(248,0,0,255))
                if test1 == -1:
                    if Bcoord[0][1] <= -20:
                        B[0] = -1
                        test1 = 0
                if test1 == 1:
                    if Bcoord[0][1] >= 720:
                        B[0] = -1
                        test1 = 0
            if B[0] == 3:
                if test1 == 0:
                    if Bcoord[0][0] == -20:
                        depl1 = 2
                        test1 = 1
                    if Bcoord[0][0] == 720:
                        depl1 = -2
                        test1 = -1
                shoot[B[0]](Bcoord[0][0],Bcoord[0][1],(248,252,248,255))
                Bcoord[0][0] += depl1
                shoot[B[0]](Bcoord[0][0],Bcoord[0][1],(248,0,0,255))
                if test1 == -1:
                    if Bcoord[0][0] <= -20:
                        B[0] = -1
                        test1 = 0
                if test1 == 1:
                    if Bcoord[0][0] >= 720:
                        B[0] = -1
                        test1 = 0
    if time>= 4000 and B[1] == -1:
        B[1] = typeShoot(1,xhost,yhost)
        loop2 = 0
        gb2 = 120
    if B[1] > -1:
        if B[1] < 2:
            shoot[B[1]](Bcoord[1][0],Bcoord[1][1],(248,gb2,gb2,255))
            gb2 += 1
            if gb2 > 248:
                gb2 = 0 
                loop2 += 1
            if loop2 == 2:
                B[1] = -1
        else:
            if B[1] == 2:
                if test2 == 0:
                    if Bcoord[1][1] == -20:
                        depl2 = 2
                        test2 = 1
                    if Bcoord[1][1] == 720:
                        depl2 = -2
                        test2 = -1
                shoot[B[1]](Bcoord[1][0],Bcoord[1][1],(248,252,248,255))
                Bcoord[1][1] += depl2
                shoot[B[1]](Bcoord[1][0],Bcoord[1][1],(248,0,0,255))
                if test2 == -1:
                    if Bcoord[1][1] <= -20:
                        B[1] = -1
                        test2 = 0
                if test2 == 1:
                    if Bcoord[1][1] >= 720:
                        B[1] = -1
                        test2 = 0
            if B[1] == 3:
                if test2 == 0:
                    if Bcoord[1][0] == -20:
                        depl2 = 2
                        test2 = 1
                    if Bcoord[1][0] == 720:
                        depl2 = -2
                        test2 = -1
                shoot[B[1]](Bcoord[1][0],Bcoord[1][1],(248,252,248))
                Bcoord[1][0] += depl2
                shoot[B[1]](Bcoord[1][0],Bcoord[1][1],(248,0,0))
                if test2 == -1:
                    if Bcoord[1][0] <= -20:
                        B[1] = -1
                        test2 = 0
                if test2 == 1:
                    if Bcoord[1][0] >= 720:
                        B[1] = -1
                        test2 = 0
    if time >= 6000 and B[2] == -1:
        B[2] = typeShoot(2,xhost,yhost)
        loop3 = 0
        gb3 = 120
    if B[2] > -1:
        if B[2] < 2:
            shoot[B[2]](Bcoord[2][0],Bcoord[2][1],(248,gb3,gb3,255))
            gb3 += 1
            if gb3 > 248:
                gb3 = 0 
                loop3 += 1
            if loop3 == 2:
                B[2] = -1
        else:
            if B[2] == 2:
                if test3 == 0:
                    if Bcoord[2][1] == -20:
                        depl3 = 2
                        test3 = 1
                    if Bcoord[2][1] == 720:
                        depl3 = -2
                        test3 = -1
                shoot[B[2]](Bcoord[2][0],Bcoord[2][1],(248,252,248,255))
                Bcoord[2][1] += depl3
                shoot[B[2]](Bcoord[2][0],Bcoord[2][1],(248,0,0,255))
                if test3 == -1:
                    if Bcoord[2][1] <= -20:
                        B[2] = -1
                        test3 = 0
                if test3 == 1:
                    if Bcoord[2][1] >= 720:
                        B[2] = -1
                        test3 = 0
            if B[2] == 3:
                if test3 == 0:
                    if Bcoord[2][0] == -20:
                        depl3 = 2
                        test3 = 1
                    if Bcoord[2][0] == 720:
                        depl3 = -2
                        test3 = -1
                shoot[B[2]](Bcoord[2][0],Bcoord[2][1],(248,252,248,255))
                Bcoord[2][0] += depl3
                shoot[B[2]](Bcoord[2][0],Bcoord[2][1],(248,0,0,255))
                if test3 == -1:
                    if Bcoord[2][0] <= -20:
                        B[2] = -1
                        test3 = 0
                if test3 == 1:
                    if Bcoord[2][0] >= 720:
                        B[2] = -1
                        test3 = 0
    if time>= 8000 and B[3] == -1:
        B[3] = typeShoot(3,xhost,yhost)
        loop4 = 0
        gb4 = 120
    if B[3] > -1:
        if B[3] < 2:
            shoot[B[3]](Bcoord[3][0],Bcoord[3][1],(248,gb4,gb4,255))
            gb4 += 1
            if gb4 > 248:
                gb4 = 0 
                loop4 += 1
            if loop4 == 2:
                B[3] = -1
        else:
            if B[3] == 2:
                if test4 == 0:
                    if Bcoord[3][1] == -20:
                        depl4 = 2
                        test4 = 1
                    if Bcoord[3][1] == 720:
                        depl4 = -2
                        test4 = -1
                shoot[B[3]](Bcoord[3][0],Bcoord[3][1],(248,252,248,255))
                Bcoord[3][1] += depl4
                shoot[B[3]](Bcoord[3][0],Bcoord[3][1],(248,0,0,255))
                if test4 == -1:
                    if Bcoord[3][1] <= -20:
                        B[3] = -1
                        test4 = 0
                if test4 == 1:
                    if Bcoord[3][1] >= 720:
                        B[3] = -1
                        test4 = 0
            if B[3] == 3:
                if test4 == 0:
                    if Bcoord[3][0] == -20:
                        depl4 = 2
                        test4 = 1
                    if Bcoord[3][0] == 720:
                        depl4 = -2
                        test4 = -1
                shoot[B[3]](Bcoord[3][0],Bcoord[3][1],(248,252,248,255))
                Bcoord[3][0] += depl4
                shoot[B[3]](Bcoord[3][0],Bcoord[3][1],(248,0,0,255))
                if test4 == -1:
                    if Bcoord[3][0] <= -20:
                        B[3] = -1
                        test4 = 0
                if test4 == 1:
                    if Bcoord[3][0] >= 720:
                        B[3] = -1
                        test4 = 0
                
    if moveHost[0] == 0 :
        player(xhost,yhost,(248,252,248,255))
        yhost -= 1
        phost(xhost,yhost)
    if moveHost[1] == 1 :
        player(xhost,yhost,(248,252,248,255))
        yhost += 1
        phost(xhost,yhost)
    if moveHost[2] == 2 :
        player(xhost,yhost,(248,252,248,255))
        xhost -= 1
        phost(xhost,yhost)
    if moveHost[3] == 3 :
        player(xhost,yhost,(248,252,248,255))
        xhost += 1
        phost(xhost,yhost)
    pygame.time.delay(1)
    ev=pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveHost[0] += 4
            if event.key == pygame.K_DOWN:
                moveHost[1] += 4
            if event.key == pygame.K_LEFT:
                moveHost[2] += 4
            if event.key == pygame.K_RIGHT:
                moveHost[3] += 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moveHost[0] -= 4
            if event.key == pygame.K_DOWN:
                moveHost[1] -= 4
            if event.key == pygame.K_LEFT:
                moveHost[2] -= 4
            if event.key == pygame.K_RIGHT:
                moveHost[3] -= 4
        
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
