import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = (255, 255, 255)
GREY   = (224,   224,   224 )
BLACK = (  0, 0,   0)

DISPLAYSURF = pygame.display.set_mode((900, 600))
pygame.display.set_caption('Hello world!')
font = pygame.font.SysFont('consolas', 30)
textSurface1 = font.render('MULTIPLAYER', True, BLACK, GREY)
textSurface2 = font.render('SINGLEPLAYER', True, BLACK, GREY)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    DISPLAYSURF.fill((255, 255, 255))
    pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 400, 300, 50))
    DISPLAYSURF.blit(textSurface1, (357, 410))

    pygame.draw.rect(DISPLAYSURF, (224, 224, 224), (300, 300, 300, 50))
    DISPLAYSURF.blit(textSurface2, (350, 310))
    pygame.display.update()
