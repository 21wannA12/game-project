
import pgzrun, sys
from random import randint


WIDTH = 1200 #Широта экрана
HEIGHT = 700 #Высота экрана

FPS = 60
TITLE = 'The Clicker'
#Актёры
fon = Actor('background') #фон
background = Actor('background')#фон окончания игры
island = Actor('island', (600, 500))#остров на котором находится враг
#кнопки
key_1 = Actor('button', (120, 220))
key_2 = Actor('button', (120, 310))
key_3 = Actor('button', (120, 400))
key_start = Actor('button', (600, 310))
key_setting = Actor('button', (600, 400))
key_exit = Actor('button', (600, 490))
key_setting_exit = Actor('button', (600, 490))
key_exit_menu = Actor("button", (600, 450))
key_exit_game_menu = Actor("money", (1070, 650))
money = Actor('money', (1110, 40))
loss = Actor('money', (1110, 100))
enemy = Actor('enemypink', (600, 320))#враг
#Переменные/списки
coins = 100 #монеты
price1 = 15 #стоимость первого бонуса
price2 = 40 #стоимость второго бонуса
price3 = 80 #стоимость третьего бонуса
enemy_hp = 250 #хп врага
damage = 100 #урон игрока
mode = 'menu' #режим игры
enemies = 0
print(mode, coins, price1, price2, price3, enemy_hp, damage)

enemyhp_old = enemy_hp
enemyhp_lvl = enemy_hp

#Функции бонусов
def bonus1(): #бонус 1
    global enemy_hp, coins
    enemy_hp -= 1
    coins += 1
    enemy.y = 300
    animate(enemy, tween='bounce_end', duration=0.5, y=320)

def bonus2(): #бонус 2
    global coins 
    coins += 3 

def bonus3(): #бонус 3
    global damage 
    damage += 1


def draw():
    #Если режим игры "меню"
    if mode == "menu":
        fon.draw()
        key_start.draw()
        key_setting.draw()
        key_exit.draw()
        screen.draw.text("The Clicker", center = (600, 220), color = "black", fontsize = 60)
        screen.draw.text("Играть", center = (600, 310), color = "black", fontsize = 30)
        screen.draw.text("Настройки", center = (600, 400), color = "black", fontsize = 30)
        screen.draw.text("Выход", center = (600, 490), color = "black", fontsize = 30)

    elif mode == "setting":
        fon.draw()
        screen.draw.text("Здесь пока что нет никаких опций", center = (600, 350), color = "black", fontsize = 60)
        key_setting_exit.draw()
        screen.draw.text("Выход", center = (600, 490), color = "black", fontsize = 30)

    #Если режим игры "игра"   
    elif mode == 'game':
        #Отрисовка всех картинок
        fon.draw()#фон
        island.draw()#остров на котором находится наш враг
        #Отрисовка всех кнопок
        key_1.draw()
        key_2.draw()
        key_3.draw()
        key_exit_game_menu.draw()
        money.draw()#монеты игрока
        loss.draw()#урон игрока
        enemy.draw()#отрисовка нашего врага
        island.x = 600
        enemy.x = 600

        screen.draw.text("Выход", center = (1070, 650), color = "black", fontsize = 25)

        #Хп врага
        screen.draw.text('Здоровье врага:', center = (600, 120), color= 'black', fontsize=30)
        screen.draw.text(str(enemy_hp), center = (600, 140), color= 'black', fontsize=30)

        #Монеты игрока
        screen.draw.text('Ваши монеты:', (1043, 30), color= 'black', fontsize=18)
        screen.draw.text(str(coins), (1140, 30), color= 'black', fontsize=18)

        #Урон игрока
        screen.draw.text('Ваш урон:', (1050, 90), color= 'black', fontsize=18)
        screen.draw.text(str(damage), (1135, 90), color= 'black', fontsize=18)

        #Бонус 1 (описание)
        screen.draw.text('Сносит врагу по 1 хп\n и даёт 1 монеты', center = (110, 210), color= 'black', fontsize=20)
        screen.draw.text('Стоимость:', center = (90, 235), color= 'black', fontsize=20)
        screen.draw.text(str(price1), center = (150, 235), color= 'black', fontsize=20)
        #Условие, если у игрока не хватает монет для покупки бонуса, то цвет текста меняется на красный
        if coins <= price1:
            screen.draw.text('Сносит врагу по 1 хп\n и даёт 1 монеты', center = (110, 210), color= 'red', fontsize=20)
            screen.draw.text('Стоимость:', center = (90, 235), color= 'red', fontsize=20)
            screen.draw.text(str(price1), center = (150, 235), color= 'red', fontsize=20)

        #Бонус 2 (описание)
        screen.draw.text('Даёт 3 монетки\n каждые 5 секунд', center = (110, 300), color= 'black', fontsize=20)
        screen.draw.text('Стоимость:', center = (90, 325), color= 'black', fontsize=20)
        screen.draw.text(str(price2), center = (150, 325), color= 'black', fontsize=20)
        #Условие, если у игрока не хватает монет для покупки бонуса, то цвет текста меняется на красный
        if coins <= price2:
            screen.draw.text('Даёт 3 монетки\n каждые 5 секунд', center = (110, 300), color= 'red', fontsize=20)
            screen.draw.text('Стоимость:', center = (90, 325), color= 'red', fontsize=20)
            screen.draw.text(str(price2), center = (150, 325), color= 'red', fontsize=20)

        #Бонус 3 (описание)
        screen.draw.text('Даёт +1 к урону', center = (120, 390), color= 'black', fontsize=20)
        screen.draw.text('Стоимость:', center = (90, 410), color= 'black', fontsize=20)
        screen.draw.text(str(price3), center = (150, 410), color= 'black', fontsize=20)
        #Условие, если у игрока не хватает монет для покупки бонуса, то цвет текста меняется на красный
        if coins <= price3:
            screen.draw.text('Даёт +1 к урону', center = (120, 390), color= 'red', fontsize=20)
            screen.draw.text('Стоимость:', center = (90, 410), color= 'red', fontsize=20)
            screen.draw.text(str(price3), center = (150, 410), color= 'red', fontsize=20)
    elif mode == 'end':
        background.draw()#фон
        screen.draw.text('GAME OVER', center = (600, 350), color= 'red', fontsize=60)
        key_exit_menu.draw()#отрисовка кнопки выхода в главное меню в конце игры
        screen.draw.text("Выход", center = (600, 450), color = "black", fontsize = 30)



#функция для обновления экрана
def update(dt):
    global mode, enemy_hp, enemyhp_old, enemyhp_lvl, enemies
    if mode == 'game':
        if enemy_hp <= 0 and enemy.image == 'enemypink':
            enemy.image = 'enemyred'
            enemies += 1
            enemy_hp = int(enemyhp_old + 250)
            enemyhp_old = enemy_hp
        
        elif enemy_hp <= 0 and enemy.image == 'enemyred':
            enemy.image = 'enemyblue'
            enemies += 1
            enemy.y = 300
            enemy_hp = int(enemyhp_old + 250)
            enemyhp_old = enemy_hp

        elif enemy_hp <= 0 and enemy.image == 'enemyblue':
            enemy_hp = enemyhp_old
            enemy.image = 'enemyorange'
            enemies += 1
            enemy.y = 300
            enemy_hp = int(enemyhp_old + 250)
            enemyhp_old = enemy_hp
            enemyhp_lvl += 250

        elif enemy_hp <= 0 and enemy.image == 'enemyorange':
            mode = 'end'

    elif mode == "end":
        enemy_hp = 400
        enemy.image = "enemypink"

#функция для обработки позиции и кликов мыши
def on_mouse_down(button, pos):
    global enemy_hp, coins, price1, price2, price3, mode, enemyhp_old
    if button == mouse.LEFT and mode == "menu":
        if key_start.collidepoint(pos):
            mode = "game"
            print(mode)
        elif key_setting.collidepoint(pos):
            mode = "setting"
            print(mode)
        elif key_exit.collidepoint(pos):
            sys.exit()
    elif button == mouse.LEFT and mode == "setting":
        if key_setting_exit.collidepoint(pos):
            mode = "menu"
            print(mode)
    elif button == mouse.LEFT and mode == 'game':
        if enemy.collidepoint(pos):
            enemy_hp -= damage 
            coins += damage
            enemy.y = 300
            animate(enemy, tween='bounce_end', duration=0.5, y=320)
            print('enemy heatlh now:', enemy_hp)

        if key_1.collidepoint(pos):
            if coins >= price1:
                clock.schedule_interval(bonus1, 2)
                coins -= price1
                price1 *= 2

        if key_2.collidepoint(pos):
            if coins >= price2:
                clock.schedule_interval(bonus2, 4)
                coins -= price2
                price2 *= 2

        if key_3.collidepoint(pos):
            if coins >= price3:
                bonus3()
                coins -= price3
                price3 *= 2

        if key_exit_game_menu.collidepoint(pos):
            mode = 'menu'

    elif button == mouse.LEFT and mode == 'end':
        if key_exit_menu.collidepoint(pos):
            mode = 'menu'

    


pgzrun.go()