import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC= 120, 120
dimCw = width / nxC
dimCh = height / nyC

gameState = np.zeros((nxC, nyC))

gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

pauseExect = False

while True:
    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celx, celY = int(np.floor(posX / dimCw)), int(np.floor(posY / dimCh))
            newGameState[celx, celY] = not mouseClick[2]

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x)     % nxC, (y - 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                        gameState[(x - 1) % nxC, (y)     % nyC] + \
                        gameState[(x + 1) % nxC, (y)     % nyC] + \
                        gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                        gameState[(x)     % nxC, (y + 1) % nyC] + \
                        gameState[(x + 1) % nxC, (y + 1) % nyC]
                
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 1 or n_neigh > 3):
                    newGameState[x, y] = 0
                poligono = [((x)   * dimCw, y * dimCh),
                            ((x+1) * dimCw, y * dimCh),
                            ((x+1) * dimCw, (y+1) * dimCh),
                            ((x)   * dimCw, (y+1) * dimCh)]
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poligono, 1)
                else:
                    pygame.draw.polygon(screen, (255, 255, 255), poligono, 0)
                
    gameState = np.copy(newGameState)
    pygame.display.flip()
