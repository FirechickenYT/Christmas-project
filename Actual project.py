import pygame
import random


import pygame, sys
from pygame.locals import *

def main():

    pygame.init()


    (width, height) = (640, 480)
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tree decoration simulators")
    white = (255, 255, 255)
    display.fill(white)
    ScaleFactor = 480/401


    treeSprite = "/Users/Thomas/Documents/Assets/Tree.webp"
    baubleSprites = ["/Users/Thomas/Documents/Assets/Blue_Bauble.webp", "/Users/Thomas/Documents/Assets/Green_Bauble.webp", "/Users/Thomas/Documents/Assets/Red_Bauble.webp", "/Users/Thomas/Documents/Assets/Silver_Bauble.webp"]
    starSprite = "/Users/Thomas/Documents/Assets/Tree Star.webp"

    tree = pygame.image.load(treeSprite)
    treeScaled = pygame.transform.scale(tree, (250 * ScaleFactor, 401 * ScaleFactor))
    star = pygame.image.load(starSprite)
    starScaled = pygame.transform.scale(star, (64, 64))

    scoreFont = pygame.font.Font("/Users/Thomas/Documents/Assets/Roboto.ttf", 96)


    display.blit(treeScaled, (149.62593516209478,0))

    x = 0 
    positions = []
    for sprite in baubleSprites:
        baubleButton = pygame.image.load(sprite)
        baubleScaledButton = pygame.transform.scale(baubleButton, (64, 64))
        display.blit(baubleScaledButton, (x, height-64))
        positions.append([x, x+64])
        x += 64
    starButton = pygame.image.load(starSprite)
    starButtonScaled = pygame.transform.scale(starButton, (64, 64))
    display.blit(starButtonScaled, (width-64, height-64))
        

    baubleSelected = 0

    colours = ["Blue", "Green", "Red", "Silver", "Star"]
    starDown = False
    while True:
        pygame.display.set_caption("Currently Selected: " + colours[baubleSelected])
        for event in pygame.event.get():
            if event.type==QUIT: #checks if red x is pressed
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if baubleSelected == -1 and starDown == False:
                    if mousex < 320 and mousex > 280 and mousey < 40:
                        display.blit(starScaled, (mousex - 32, mousey - 32))
                        starDown = True

                if mousex > 169 and mousex < 420 and mousey < 331 and mousey > 50:
                    bauble = pygame.image.load(baubleSprites[baubleSelected])
                    baubleScaled = pygame.transform.scale(bauble, (32, 32))
                    display.blit(baubleScaled, (mousex - 16, mousey - 16))

                elif mousex >= width-64 and mousex <= width and mousey >= height-64:
                    baubleSelected = -1
                    print("Selected", colours[baubleSelected] + "!")

                else:
                    for i in range(len(positions)):
                        if mousex > positions[i][0] and mousex < positions[i][1] and mousey >= height - 64:
                            if i != baubleSelected:
                                baubleSelected = i
                                print("Selected", colours[baubleSelected] + "!")
                            break
                            
        pygame.display.update()


main()
