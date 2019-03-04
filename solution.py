# Игра, при которой нужно уворачиваться от пуль, чтобы выиграть










#Импортируем библеотеки PyGame, Sys(Для спокойного выхода из окна), Random(Для случайного появления "пуль")
import pygame 
import sys
import random

#Задаем ФПС(кол-во кадров в секунду), размеры экрана
FPS = 60
W = 900
H = 800
#Инициализируем окно
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Координаты появления круга(в центре экрана) и радиус
x = W // 2
y = H // 2
r = 50

count = 0 #переменная для счёта

motion = 0 #переменная для работы с нажатиями клавиш

gameover = False #переменная для определения "конца игры"
f2 = pygame.font.SysFont('Zig', 38) #задаем шрифт
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
#Главный цикл
while 1:
    #Задаем "счёт"
    if gameover == False:
        count += 1 
    #Место для рисования различных элементов
    sc.fill((0, 0, 0))
    for i in range(20):
        if hitted[i] == 0:
            pygame.draw.circle(sc, (0, 255, 0), (x1[i], y1[i]), 5)
            print(x1[i])
            x1[i] += 1
            y1[i] += random.randint(-10, 10)
    pygame.draw.circle(sc, (0, 0, 255), (x, y), r)
    pygame.draw.circle(sc, (255, 0, 0), (x - r, y), 5)#Рисуем круг
    if fired == True:
            pygame.draw.line(sc, (255, 0, 0), (0, y), (x - r, y))
            fired = False
    if gameover == True:           #Если игра окончена(пользователь проиграл)
        sc.blit(text2, (W//3, H//3)) #Выводим "GAMEOVER"
    text = f2.render('{}'.format(count), 0, (0, 255, 0)) #Выводим счёт на экран
    sc.blit(text, (800, 700))
    pygame.display.update()
    
    for i in pygame.event.get(): #Цикл обработки нажатий
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
                for i in range(len(x1)):
                    if y1[i] in range(y - 25, y + 25):
                        hitted[i] = 1
                        x1[i] = random.randint(-100, 1)
                    else:
                        hitted[i] = 0
                        
    
    if gameover == False: #Цикл обработки нажатий клавиш и их восприятия
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
        
        gameoverx = [] #Координаты точек по х, при соприкосновении которых с пулями игрок проигрывает
        gameovery = [] #Координаты точек по у, при соприкосновении которых с полями игрок поигрывает
        
        for j in range(35): #Цикл заполнения списка координат проигрыша
            for k in range(35):
                gameoverx.append(x - j)
                gameoverx.append(x + j)
                gameovery.append(y - j)
                gameovery.append(y + j)
        
        
        
        
        #Возвращение на экран с другой стороны
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