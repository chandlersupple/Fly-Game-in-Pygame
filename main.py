# 3/31/2018, Chandler Supple
# Program opens window on desktop - Python 2.7 or Python 3 variant compatible

import pygame, sys
from pygame.locals import *
from urllib2 import urlopen

pygame.init()
geometry = pygame.display.set_mode((500, 500))
pygame.display.set_caption('FLY -- Chandler Supple')
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

# SPRITES -  -  -  -  -  -  -  -  -  -  -  #

nyan1 = 'http://worldartsme.com/images/nyan-cat-clipart-1.jpg'
nyan2 = urlopen(nyan1).read()
nyan3 = io.BytesIO(nyan2)
nyan4 = pygame.image.load(nyan3)
nyan = pygame.transform.scale(nyan4,(200,66))
image = nyan

jb1 = 'http://www.clipartlord.com/wp-content/uploads/2013/01/justin-bieber2.png'
jb2 = urlopen(jb1).read()
jb3 = io.BytesIO(jb2)
jb4 = pygame.image.load(jb3)
jb = pygame.transform.scale(jb4,(200,200))

hawking1 = 'http://www.stickpng.com/assets/images/58468dfccd48624bdb8beae4.png'
hawking2 = urlopen(hawking1).read()
hawking3 = io.BytesIO(hawking2)
hawking4 = pygame.image.load(hawking3)
hawking = pygame.transform.scale(hawking4,(200,230))

peppa1 = 'https://i.pinimg.com/originals/e6/ec/8c/e6ec8cb3da432fa2a83928f3e95a883f.png'
peppa2 = urlopen(peppa1).read()
peppa3 = io.BytesIO(peppa2)
peppa4 = pygame.image.load(peppa3)
peppa = pygame.transform.scale(peppa4,(150,173))

bird1 = 'http://worldartsme.com/images/flying-bird-clipart-1.jpg'
bird2 = urlopen(bird1).read()
bird3 = io.BytesIO(bird2)
bird4 = pygame.image.load(bird3)
bird = pygame.transform.scale(bird4,(60,60))

# SPRITES -  -  -  -  -  -  -  -  -  -  -  #

geometry.blit(image,(20,20))

white = (255, 255, 255)

x3 = 200
y3 = 100
x4 = 0
y4 = 200
x5 = 300
y5 = 450
x6 = 120
y6 = 280

def cloud(x2, y2):
    pygame.draw.circle(geometry, white, (x2,y2), 40, 40)
    pygame.draw.circle(geometry, white, (x2+35,y2), 50, 50)
    pygame.draw.circle(geometry, white, (x2+85,y2-30), 50, 50)
    pygame.draw.circle(geometry, white, (x2+125,y2), 60, 60)
    
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_a]: image = jb
        if pressed[pygame.K_d]: image = nyan
        if pressed[pygame.K_s]: image = hawking
        if pressed[pygame.K_w]: image = peppa
        
        geometry.fill((125, 125, 255))
        
        x3 = x3 + 1
        x4 = x4 + 1
        x5 = x5 + 1
        x6 = x6 + 3
        
        a = (100*(0.5*(sin((x6)))))
        b = abs(a)
        y6 = (round(b,0)) + 50
        
        cloud(x3, y3)
        cloud(x4, y4)
        cloud(x5, y5)
    
        if(x3 >= 500):
            x3 = 0
        if(x4 >= 500):
            x4 = 0
        if(x5 >= 500):
            x5 = 0
        if(x6 >= 2000):
            x6 = 0
        
        
        geometry.blit(bird,(x6,y6))
        geometry.blit(image,(x,y))
        
        
        pygame.display.flip()
        clock.tick(60)
