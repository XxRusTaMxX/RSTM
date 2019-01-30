import pygame
import sys
import random


FPS = 60
W = 900  # ширина экрана
H = 800  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 50

x1 = []
y1 = []

count = 0

motion = 0

gameover = False
f2 = pygame.font.SysFont('serif', 48)
text2 = f2.render("GAMEOVER", 0, (0, 180, 0))    

while 1:
    if gameover == False:
        count += 1
    sc.fill((0, 0, 0))
    for i in range(10):
        x1.append(random.randint(-5, 905))
        y1.append(random.randint(-5, 905))
    
    pygame.draw.circle(sc, WHITE, (x, y), r)
    for i in range(10):
        pygame.draw.circle(sc, (255, 0, 0), (x1[i], y1[i]), 5)
    
    if gameover == True:           
        sc.blit(text2, (W//3, H//4))
    text = f2.render('{}'.format(count), 0, (0, 180, 0))
    sc.blit(text, (800, 700))
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
    
    if gameover == False:
        if motion == -1:
            x -= 3
        elif motion == 1:
            x += 3
        elif motion == 2:
            x += 6
        elif motion == -2:
            x -= 6
        elif motion == 10:
            y -= 3
        elif motion == 20:
            y -= 6
        elif motion == -10:
            y += 3
        elif motion == -20:
            y += 6
        
        gameoverx = []
        gameovery = []
        
        for j in range(35):
            for k in range(35):
                gameoverx.append(x - j)
                gameoverx.append(x + j)
                gameovery.append(y - j)
                gameovery.append(y + j)
        
        for j in range(10):
            x1[j] += 10
            
            if x1[j] > 905:
                x1[j] = -5
                y1[j] = random.randint(-9, 905)
            if count > 60:
                if (x1[j] in gameoverx) and (y1[j] in gameovery):
                    gameover = True
        
        
        
        
        
        if y > 1000:
            y = -50
        if x > 850:
            x = 850
        if y < -50:
            y = 1000
        if x < -50:
            x = 950
    clock.tick(FPS)