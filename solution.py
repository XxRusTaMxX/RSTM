










import pygame 
import sys
import random


FPS = 60
W = 900
H = 800

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50
count20 = 0
count = 0.1

motion = 0 
hitted1 = False
gameover = False
paused = False
f2 = pygame.font.SysFont('Zig', 38)
text2 = f2.render("GAMEOVER", 0, (0, 255, 0))    


fired = False

x1 = []
y1 = []
for i in range(20):
    x1.append(random.randint(-100, 1))
    y1.append(random.randint(1, 800))
hitted = []
for i in range(20):
    hitted.append(0)
while 1:
    if gameover == False:
        count += 0.01 
    if paused == False:
        sc.fill((0, 0, 0))
        for i in range(20):
            if hitted[i] == 0 and hitted1 == False:
                pygame.draw.circle(sc, (0, 255, 0), (x1[i], y1[i]), 5)
                print(x1[i])
                x1[i] += 2
                if y1[i] in range(50, 750):
                    y1[i] += random.randint(-10, 10)
                elif y1[i] < 60:
                    y1[i] += random.randint(0, 10)
                elif y1[i] > 740:
                    y1[i] += random.randint(-10, 0)
        pygame.draw.circle(sc, (0, 0, 255), (x, y), r)
        pygame.draw.circle(sc, (255, 0, 0), (x - r, y), 5)
        if fired == True:
                pygame.draw.line(sc, (255, 0, 0), (0, y), (x - r, y))
                fired = False
        if gameover == True:         
            sc.blit(text2, (W//3, H//3))
        text = f2.render('{}'.format(count), 0, (0, 255, 0)) 
        sc.blit(text, (800, 700))
        pygame.draw.rect(sc, (255, 20, 20), (W - 20, 0, 20, H))
        pygame.display.update()
        
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = -1
            if i.key == pygame.K_RIGHT:
                motion = 1
            if i.key == pygame.K_RIGHT and i.mod == pygame.KMOD_LSHIFT:
                motion = 2
            if i.key == pygame.K_LEFT and i.mod == pygame.KMOD_LSHIFT:
                motion = -2
            if i.key == pygame.K_UP:
                motion = 10
            if i.key == pygame.K_UP and i.mod == pygame.KMOD_LSHIFT:
                motion = 20
            if i.key == pygame.K_DOWN:
                motion = -10
            if i.key == pygame.K_DOWN and i.mod == pygame.KMOD_LSHIFT:
                motion = -20
            if i.key == pygame.K_f:
                fired = True
                for o in range(len(x1)):
                    if y1[o] in range(y - 25, y + 25):
                        hitted[o] = 1
                        x1[o] = random.randint(-100, 1)
                    else:
                        hitted[o] = 0
            if i.key == pygame.K_p:
                if paused == False:
                    paused = True
                else:
                    paused = False
            if i.key == pygame.K_g:
                if int(count) % 2 == 0:
                    hitted1 = True
                if int(count) == 3:
                    hitted1 = False
    
    if gameover == False and paused == False: 
        if motion == -1:
            x -= 6
        elif motion == 1:
            x += 6
        elif motion == 2:
            x += 10
        elif motion == -2:
            x -= 10
        elif motion == 10:
            y -= 6
        elif motion == 20:
            y -= 10
        elif motion == -10:
            y += 6
        elif motion == -20:
            y += 10
        
        gameoverx = [] 
        gameovery = [] 
        
        for j in range(35):
            for k in range(35):
                gameoverx.append(x - j)
                gameoverx.append(x + j)
                gameovery.append(y - j)
                gameovery.append(y + j)
        
        
        
        
        if y > 1000:
            y = -50
        if x > 850: 
            x = 850
        if y < -50: 
            y = 1000
        if x < -50: 
            x = 950
            
            
        for i in range(len(x1)):
            if x1[i] > 900:
                gameover = True
    clock.tick(FPS)
