#Импортируем библеотеки PyGame, Sys(Для спокойного выхода из окна), Random(Для случайного появления "пуль")
import pygame 
import sys
import random

#Задаем ФПС(кол-во кадров в секунду), размеры экрана и цвета(это не важно)
FPS = 60
W = 900  # øèðèíà ýêðàíà
H = 800  # âûñîòà ýêðàíà
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
#Инициализируем окно
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# Координаты появления круга(в центре экрана) и радиус
x = W // 2
y = H // 2
r = 50
# Список координат "пуль"
x1 = []
y1 = []

count = 0 #переменная для счёта

motion = 0 #переменная для работы с нажатиями клавиш

gameover = False #переменная для определения "конца игры"
f2 = pygame.font.SysFont('serif', 48) #задаем шрифт
text2 = f2.render("GAMEOVER", 0, (0, 180, 0))    
#Главный цикл
while 1:
    #Задаем "счёт"
    if gameover == False:
        count += 1 
    #Место для рисования различных элементов
    sc.fill((0, 0, 0))
    for i in range(10):
        x1.append(random.randint(-5, 905)) #Случайные координаты "пуль"  по х
        y1.append(random.randint(-5, 905)) #Случайные координаты "пуль" по у
    
    pygame.draw.circle(sc, WHITE, (x, y), r) #Рисуем круг
    for i in range(10):
        pygame.draw.circle(sc, (255, 0, 0), (x1[i], y1[i]), 5) #Рисуем пульки
    
    if gameover == True:           #Если игра окончена(пользователь проиграл)
        sc.blit(text2, (W//3, H//4)) #Выводим "GAMEOVER"
    text = f2.render('{}'.format(count), 0, (0, 180, 0)) #Выводим счёт на экран
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
        
        for j in range(10): #Цикл движения пуль и нового появления
            x1[j] += 10 
            
            if x1[j] > 905:
                x1[j] = -5
                y1[j] = random.randint(-9, 905)
            if count > 60: # Страховка на случай, если при начале игры пуля появляется внутри круга
                if (x1[j] in gameoverx) and (y1[j] in gameovery): # Проверка на соприкосновение пуль с кругом игрока
                    gameover = True
        
        
        
        
        #Возвращение на экран с другой стороны
        if y > 1000:
            y = -50
        if x > 850: 
            x = 850
        if y < -50: 
            y = 1000
        if x < -50: 
            x = 950
    clock.tick(FPS)
