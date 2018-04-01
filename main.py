# 3/31/2018, Chandler Supple
# Program opens window on desktop - Python 2.7 or Python 3 variant compatible

import io
from math import *
import pygame, sys
from pygame.locals import *
from urllib2 import urlopen

pygame.init()
geometry = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Just For Fun -- Chandler Supple')
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
nyan = pygame.transform.scale(nyan4,(300,100))

club1 = 'https://vignette.wikia.nocookie.net/clubpenguin/images/a/af/Jet_pack_surfer.png/revision/latest?cb=20130103185837'
club2 = urlopen(club1).read()
club3 = io.BytesIO(club2)
club4 = pygame.image.load(club3)
club = pygame.transform.scale(club4,(200,200))
image = club

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

china1 = 'http://i.imgur.com/PeyFxEw.png'
china2 = urlopen(china1).read()
china3 = io.BytesIO(china2)
china4 = pygame.image.load(china3)
china = pygame.transform.scale(china4,(120,200))
    
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
x7 = 200
y7 = 700

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
        if pressed[pygame.K_a]: image = club
        if pressed[pygame.K_d]: image = nyan
        if pressed[pygame.K_s]: image = hawking
        if pressed[pygame.K_w]: image = peppa
        
        geometry.fill((125, 125, 255))
        
        x3 = x3 + 1
        x4 = x4 + 1
        x5 = x5 + 1
        x6 = x6 + 3
        y7 = y7 + 1
        
        a = (100*(0.2*(sin((x6)))))
        b = abs(a)
        y6 = (round(b,0)) + 50
        
        a_ = (200*(0.2*(sin(0.05*(y7)))))
        b_ = abs(a_)
        x7 = (round(b_,0)) + 300
        
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
        if(y7 >=1500):
            y7 = 0
        
        geometry.blit(china,(x7,y7))
        geometry.blit(bird,(x6,y6))
        geometry.blit(image,(x,y))
        
        pygame.display.flip()
        clock.tick(60)
