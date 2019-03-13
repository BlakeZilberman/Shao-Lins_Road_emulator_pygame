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

heroX = 650
heroY = 550 
enemyX = 400
enemyY = 400
enemyImg = pygame.image.load('Assets/enemy.png')
enemyImg = pygame.transform.scale(heroImg, (200, 200))
kicking = False



while True: # main game loop


    DISPLAYSURF.blit(bg, (0, 0))


 

    keys = pygame.key.get_pressed()

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



    
