import pygame
import time
import random
import pandas
import numpy

pygame.init()

hr_fishing_left = pygame.image.load('images/hero_l.png')
hr_fishing_right = pygame.image.load('images/hero_r.png')
hrl = pygame.image.load('images/hero_l_swim.png')
hrr = pygame.image.load('images/hero_r_swim.png')
main_screen = pygame.image.load('images/main_screen.jpg')
torg = pygame.image.load('images/torg.png')
invent = pygame.image.load('images/inventory.png')
fuga = pygame.image.load('images/fuga.jpg')
losos = pygame.image.load('images/losos.jpg')
treska = pygame.image.load('images/treska.png')
clown = pygame.image.load('images/clown.jpg')
piranya = pygame.image.load('images/piranya.png')
red = pygame.image.load('images/red.png')
goldfish = pygame.image.load('images/gold.jpg')


k=0
f = open('data/inventory.txt')
a = f.read()
o = a.split("\n")
for i in o:
    k+=1

o = '0'
xi = 0
yi = 108
coll = []
inventory = False
fishing = False 
loc = 'main'
run = True
x = 870
y = 380
width = 100
height = 50
speed = 12
bg_color = (0, 0, 255)
lmove = -1
screen = pygame.display.set_mode((1000, 500))
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font('freesansbold.ttf', 15)
ch1, ch2, ch3 = 0, 0, 0

class corner_moves:
    '''действия'''
    def fish():
        
        if loc == 'main':
            fishing = True
            if lmove == 1:
                screen.blit(hr_fishing_right, ((x, y)))
            else:
                screen.blit(hr_fishing_left, ((x, y)))
        pygame.display.update()
         
    def Fishing():
        o = ''
        
        rand = random.randint(0, 1000)
        if rand < 500:
            randf = random.randint(1, 4)
            if randf == 1:
                o = 'treska'
            elif randf == 2:
                o = 'losos'
            elif randf == 3:
                o = 'clown'
            elif randf == 4:
                o = 'piranya'
        elif rand < 300:
            randf = random.randint(1,2)
            if randf == 1:
                o = 'fuga'
            elif randf == 2:
                o = 'red'
        elif rand < 0:
            o = 'goldfish'
        if o != '':
            coll.append(o)   

    
class draw:
    '''отрисовка'''
    def back():
        if loc == 'main':
            screen.blit(main_screen, ((0, 0)))
        
        elif loc == 'torg':
            screen.blit(torg, ((0, 0)))
        
        pygame.display.update()
    
    def drawhero():
        if lmove == 1:
            screen.blit(hrr, ((x, y)))
            
        else:
            screen.blit(hrl, ((x, y)))
        
        pygame.display.update()
    
    def inv():
        c = 0
        f = open('data/inventory.txt')
        a = f.readline()
        b, lvl, t = a.split(' ')    
        screen.blit(invent, ((100, 100)))
        text = font.render(lvl, True, black, None)
        textRect = text.get_rect()
        textRect.center = (150, 150)
        fishing_rod = [pygame.image.load('images/freshman.jpg')]
        slot = [fuga, losos, treska, clown, piranya, red, goldfish]
        if b == 'freshman':
            screen.blit(fishing_rod[0], ((108, 108)))
            screen.blit(text, textRect)  
            yi = 108
        for i in range(len(coll)):
            xi = 108 + 59.6 * (i + 1)
            if i == 23:
                break
            elif yi == 108 and xi < 450:
                xi = 108 + 59.6 * (i + 1)
            elif (yi == 108 and xi > 450) or (yi == 171 and xi > 450) and xi < 806:
                c=1
                yi = 171
                xi = 108 + 59.6 * (i-5)
    
            elif (yi == 171 and xi > 806) or (yi == 234 and xi > 806) and xi < 1162:
                yi = 234
                xi = 108 + 59.6 * (i-11)
                
            elif (yi == 234 and xi > 1162) or (yi == 297 and xi > 1162):
                yi = 297
                xi = 108 + 59.6 * (i-17)
                
            if coll[i] == 'fuga':
                screen.blit(slot[0], ((xi, yi)))
            elif coll[i] == 'losos':
                screen.blit(slot[1], ((xi, yi)))
            elif coll[i] == 'treska':
                screen.blit(slot[2], ((xi, yi)))  
            elif coll[i] == 'clown':
                screen.blit(slot[3], ((xi, yi)))        
            elif coll[i] == 'piranya':
                screen.blit(slot[4], ((xi, yi)))    
            elif coll[i] == 'red':
                screen.blit(slot[5], ((xi, yi))) 
            elif coll[i] == 'goldfish':
                screen.blit(slot[5], ((xi, yi)))         
            
            
        pygame.display.update()
    
'''основной цикл'''
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    
    
    if fishing == False and inventory == False:
        if keys[pygame.K_w]:
            if loc == 'main' and y > 330:
                y -= speed
            if loc == 'torg' and y > 300:
                y -= speed
    
        elif keys[pygame.K_s] and y < 415:
            y += speed
        
        if keys[pygame.K_d] and x < 1000:
            x += speed
            lmove = 1
        elif keys[pygame.K_d] and x > 900 and loc == 'torg':
            loc = 'main'
            x = 100
            lmove = 1
            
            
        
        if keys[pygame.K_a] and x > -100:
            x -= speed
            lmove = -1
        elif keys[pygame.K_a] and x < -80 and loc == 'main':
            loc = 'torg'
            x = 900
            lmove = -1  
            
            
    draw.back()
    
    if inventory:
        draw.inv()
        draw.drawhero()
    
    
    if keys[pygame.K_i]:
        if inventory:
            inventory = False
        else:
            inventory = True   
    
    
    if keys[pygame.K_q] and loc == 'main':
        fishing = True
        
    elif keys[pygame.K_z]:
        fishing = False
    
    if fishing:
        corner_moves.fish()
    else:
        draw.drawhero()
    
    if fishing and keys[pygame.K_e]:
        corner_moves.Fishing()
    
pygame.quit()