import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
GREY = (224, 224, 224)
BLACK = (0, 0, 0)
a = 0
size_square = 32

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Menu Game')
font = pygame.font.SysFont('consolas', 30)
font1 = pygame.font.SysFont('consolas', 100)
textSurface1 = font.render('MULTIPLAYER', True, BLACK)
textSurface2 = font.render('SINGLEPLAYER', True, BLACK)
information = font.render('i', True, BLACK)
name = font1.render('BATTLESHIP', True, BLACK, WHITE)
logo = pygame.image.load('setting.png')
setting1 = pygame.image.load('setting1.png')
setting2 = pygame.transform.scale(setting1, (55,55))
logo2 = pygame.transform.scale(logo, (55, 55))
size = font.render('SIZE', True, BLACK)
size1 = font.render('-', True, BLACK)
size2 = font.render('+', True, BLACK)


def singleplayer():
    global a
    DISPLAYSURF.fill((255,255,255))
    pygame.draw.polygon(DISPLAYSURF, (155,155,155), ((30, 45), (60, 60), (60, 25 )))
    if (30< mouse_x < 60) and (25 < mouse_y < 60):
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if (30< mouse_x < 60) and (25 < mouse_y < 60):
               a = 0

def multiplayer():
    global a
    DISPLAYSURF.fill((255,255,255))
    pygame.draw.polygon(DISPLAYSURF, (155,155,155), ((30, 45), (60, 60), (60, 25 )))
    if (30< mouse_x < 60) and (25 < mouse_y < 60):
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if (30< mouse_x < 60) and (25 < mouse_y < 60):
                a = 0

def infor():
    global a
    DISPLAYSURF.fill((255,255,255))
    pygame.draw.polygon(DISPLAYSURF, (155,155,155), ((30, 45), (60, 60), (60, 25 )))
    if (30< mouse_x < 60) and (25 < mouse_y < 60):
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if (30< mouse_x < 60) and (25 < mouse_y < 60):
                a = 0

def setting():
    global size_square
    global a
    DISPLAYSURF.fill((255,255,255))
    pygame.draw.polygon(DISPLAYSURF, (155,155,155), ((30, 45), (60, 60), (60, 25 )))
    if (30< mouse_x < 60) and (25 < mouse_y < 60):
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
    pygame.draw.rect(DISPLAYSURF, GREY, (110,100,700,450))
    pygame.draw.rect(DISPLAYSURF, (155,155,155), (280,200,65,65))
    pygame.draw.rect(DISPLAYSURF, WHITE, (400,200,130,65))
    pygame.draw.rect(DISPLAYSURF, (155,155,155), (580,200,65,65))
    DISPLAYSURF.blit(size, (430,160))
    DISPLAYSURF.blit(size1, (305,215))
    DISPLAYSURF.blit(size2, (605,215))
    DISPLAYSURF.blit(size_square1, (450,220))
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if (280 < mouse_x < 345) and (200 < mouse_y < 265 ):
                size_square = size_square - 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            if (580 < mouse_x < 645) and (200 < mouse_y < 265):
                size_square = size_square + 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:        
            if (30< mouse_x < 60) and (25 < mouse_y < 60):              
                a = 0

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    size_square1 = font.render(str(size_square), True, BLACK)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if a == 0:
        DISPLAYSURF.fill((255, 255, 255))

        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 470, 300, 50))
        DISPLAYSURF.blit(textSurface1, (357, 480))      #MULTIPLAYER
        if (300 < mouse_x < 600) and (470 < mouse_y < 520):
            pygame.draw.rect(DISPLAYSURF, (155,155,155), (300, 470, 300, 50))
            DISPLAYSURF.blit(textSurface1, (357, 480))
            
        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 380, 300, 50))
        DISPLAYSURF.blit(textSurface2, (350, 390))      #SINGLEPLAYER
        if (300 < mouse_x < 600) and (380 < mouse_y < 430):     #SINGLEPLAYER
            pygame.draw.rect(DISPLAYSURF, (155,155,155), (300, 380, 300, 50))
            DISPLAYSURF.blit(textSurface2, (350, 390))  
    
        DISPLAYSURF.blit(logo2, (2, -2))        #setting
        if (8 < mouse_x < 50) and (10 < mouse_y < 50):
            DISPLAYSURF.blit(setting2, (2, -2))

        pygame.draw.circle(DISPLAYSURF, (224,224,224),(80,30), 20) #information
        DISPLAYSURF.blit(information, (72,18))
        if (60 < mouse_x < 100) and (10 < mouse_y < 50):
            pygame.draw.circle(DISPLAYSURF, (155,155,155),(80,30), 20) #information
            DISPLAYSURF.blit(information, (72,18))   

        DISPLAYSURF.blit(name, (200,200))       #name game

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (300 < mouse_x < 600) and (380 < mouse_y < 430):     #SINGLEPLAYER
                    pygame.draw.rect(DISPLAYSURF, (155,155,155), (300, 380, 300, 50))
                    DISPLAYSURF.blit(textSurface2, (350, 390))  
                    a = 1
            if (300 < mouse_x < 600) and (470 < mouse_y < 520):
                pygame.draw.rect(DISPLAYSURF, (155,155,155), (300, 470, 300, 50))
                DISPLAYSURF.blit(textSurface1, (357, 480))
                a = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (60 < mouse_x < 100) and (10 < mouse_y < 50):
                    pygame.draw.circle(DISPLAYSURF, (155,155,155),(80,30), 20) #information
                    DISPLAYSURF.blit(information, (72,18)) 
                    a = 3
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if (8 < mouse_x < 50) and (10 < mouse_y < 50):
                    DISPLAYSURF.blit(setting2, (2, -2))
                    a = 4
    if a == 1: 
        singleplayer()
    if a == 2:
        multiplayer()
    if a == 3:
        infor()
    if a == 4:
        setting()
    pygame.display.update()
