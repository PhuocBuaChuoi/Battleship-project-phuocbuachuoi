import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
GREY = (224, 224, 224)
BLACK = (0, 0, 0)

a = 0

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Menu Game')
font = pygame.font.SysFont('consolas', 30)
font1 = pygame.font.SysFont('consolas', 100)
textSurface1 = font.render('MULTIPLAYER', True, BLACK, GREY)
textSurface2 = font.render('SINGLEPLAYER', True, BLACK, GREY)
information = font.render('i', True, BLACK, GREY)
name = font1.render('BATTLESHIP', True, BLACK, WHITE)
logo = pygame.image.load('setting.png')
logo2 = pygame.transform.scale(logo, (55, 55))

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if a == 0:
        DISPLAYSURF.fill((255, 255, 255))

        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 470, 300, 50))
        DISPLAYSURF.blit(textSurface1, (357, 480))      #MULTIPLAYER
            

        pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 380, 300, 50))
        DISPLAYSURF.blit(textSurface2, (350, 390))      #SINGLEPLAYER
    
        DISPLAYSURF.blit(logo2, (2, -2))        #setting

        pygame.draw.circle(DISPLAYSURF, (224,224,224),(80,30), 20) #information
        DISPLAYSURF.blit(information, (72,18))  

        DISPLAYSURF.blit(name, (200,200))       #logo

        if (300 < mouse_x < 600) and (380 < mouse_y < 430):
            if mouse_press[0] == 1:
                a = 1
        elif (300 < mouse_x < 600) and (470 < mouse_y < 520):
            if mouse_press[0] == 1:
                a = 2
        elif (60 < mouse_x < 100) and (10 < mouse_y < 50):
            if mouse_press[0] == 1:
                a = 3
        elif (8 < mouse_x < 50) and (10 < mouse_y < 50):
            if mouse_press[0] == 1:
                a = 4
    if a == 1: 
        DISPLAYSURF.fill((255,255,255))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
        if (30< mouse_x < 60) and (25 < mouse_y < 60):
            if mouse_press[0] == 1:
                a = 0
    if a == 2:
        DISPLAYSURF.fill((255,255,255))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
        if (30< mouse_x < 60) and (25 < mouse_y < 60):
            if mouse_press[0] == 1:
                a = 0
    if a == 3:
        DISPLAYSURF.fill((255,255,255))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
        if (30< mouse_x < 60) and (25 < mouse_y < 60):
            if mouse_press[0] == 1:
                a = 0
    if a == 4:
        DISPLAYSURF.fill((255,255,255))
        pygame.draw.polygon(DISPLAYSURF, BLACK, ((30, 45), (60, 60), (60, 25 )))
        if (30< mouse_x < 60) and (25 < mouse_y < 60):
            if mouse_press[0] == 1:
                a = 0
