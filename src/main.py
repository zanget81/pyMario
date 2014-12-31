__author__ = 'angel'

import pygame
from constants import Constants

def main():
    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((Constants().WIDTH, Constants().HEIGHT))

    iconSurface = pygame.image.load(Constants().ICON)
    icon = pygame.transform.scale(iconSurface, (Constants().ICON_SIZE, Constants().ICON_SIZE))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('PyMario')
    pygame.mouse.set_visible(0)


    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()