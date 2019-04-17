







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


all_sprites = pygame.sprite.Group()
hero_sprites = pygame.sprite.Group()
evil_sprites = pygame.sprite.Group()


hero = pygame.sprite.Sprite()
hero.image = pygame.image.load("F5S2.png")
hero.image = pygame.transform.scale(hero.image, (100, 100))
hero.image = pygame.transform.rotate(hero.image, 90)
hero.rect = hero.image.get_rect()
hero_sprites.add(hero)
hero.rect.x = x
hero.rect.y = y
gameover1 = False


class Evil(pygame.sprite.Sprite):
    image = pygame.image.load("F5S1.png")
    
    
    def __init__(self, group):
        super().__init__(group)
        self.image = Evil.image
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-100, 1)
        self.rect.y = random.randint(1, 800)
        gameover1 = False
        
    def update(self):
        if self.rect.y > 10 and self.rect.y < H - 10:
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
        elif self.rect.y < 15:
            self.rect.y = 20
        elif self.rect.y > H - 15:
            self.rect.y = H - 20
        
        
    def fired(self):
        if self.rect.y in range(y - 25, y + 25):
            self.rect.x = random.randint(-100, 1)
            self.rect.y = random.randint(1, 800)
    
    def death(self):
        self.rect.x = random.randint(-100, 1)
        self.rect.y = random.randint(1, 800)
    
    
    def move(self):
        global gameover1
        if self.rect.x > W - 40:
            gameover1 = True   
        self.rect.x += 2
         
        
        

        
Evils = []
fired = False

for _ in range(20):
    Evils.append(Evil(evil_sprites))


while 1:
    if gameover == False:
        count += 0.01 
    if paused == False:
        sc.fill((0, 0, 0))
        hero_sprites.draw(sc)
        evil_sprites.draw(sc)
        evil_sprites.update()
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
                for __ in range(len(Evils)):
                    Evils[__].fired()
            if i.key == pygame.K_p:
                if paused == False:
                    paused = True
                else:
                    paused = False
            if i.key == pygame.K_g:
                if int(count) % 5 == 0:
                    hitted1 = True
    
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
        hero.rect.x = x - 50
        hero.rect.y = y - 50   
        gameoverx = [] 
        gameovery = [] 
        
        for j in range(35):
            for k in range(35):
                gameoverx.append(x - j)
                gameoverx.append(x + j)
                gameovery.append(y - j)
                gameovery.append(y + j)
        
        for __ in range(len(Evils)):
            Evils[__].move()
        
        
        if y > 1000:
            y = -50
        if x > 850: 
            x = 850
        if y < -50: 
            y = 1000
        if x < -50: 
            x = 950
        
        
        if hitted1 == True:
            for ___ in range(len(Evils)):
                Evils[___].death()
            hitted1 = False
        
        if gameover1 == True:
            gameover = True
        
    clock.tick(FPS)

