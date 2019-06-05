import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Shao Lin's Road")
heroImg = pygame.image.load('Assets/hero.png')
heroImg = pygame.transform.scale(heroImg, (200, 200))
herokickImg = pygame.image.load('Assets/herokick.png')
herokickImg = pygame.transform.scale(herokickImg, (200, 200))
bg = pygame.image.load("Assets/background.png")
bg = pygame.transform.scale(bg, (800, 800))
fpsClock = pygame.time.Clock()
FPS = 60

red = (255, 0, 0)

heroX = 650
heroY = 550 
enemyX = 375
enemyY = 265
enemyImg = pygame.image.load('Assets/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (200, 200))
enemykickImg = pygame.image.load('Assets/enemykick.png')
enemykickImg = pygame.transform.scale(enemykickImg, (200, 200))

kicking = False
colour = (255, 10, 15)

# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 32) 

# create a text suface object, 
# on which text is drawn on it. 
text = font.render("Shao Lin's Road", True, red, None) 

# create a rectangular object for the 
# text surface object 
textRect = text.get_rect() 

# set the center of the rectangular object. 
textRect.center = (200 , 100) 

speed = 9.5

while True: # main game loop

  # -- draw 
    DISPLAYSURF.blit(bg, (0, 0))
    DISPLAYSURF.blit(text, textRect)
    keys = pygame.key.get_pressed()

    #Enemy logic
    

    enemyX = enemyX + speed

    DISPLAYSURF.blit(enemyImg, (enemyX, enemyY))

    if (enemyX <= -10):
        speed = 9.5
        
    if (enemyX >= 650):
        speed = -9.5

    if (speed == 9.5):
        DISPLAYSURF.blit(enemykickImg, (enemyX, enemyY))


    

 # Game controls 
    if keys[pygame.K_LEFT] and heroX > -50: 
        heroX -= 10
    if keys[pygame.K_RIGHT] and heroX < 650:
        heroX += 10
    if keys[pygame.K_SPACE]:
        kicking = True
        DISPLAYSURF.blit(herokickImg, (heroX, heroY))       
    else:
        kicking = False
        DISPLAYSURF.blit(heroImg, (heroX, heroY))


    fpsClock.tick(FPS)
    pygame.display.update()


















    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    
