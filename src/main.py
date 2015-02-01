__author__ = 'angel'

import pygame
from constants import Constants
from locale import Locale
from player import Player
from level import Level

def main():

    constantHandler = Constants()
    localeHandler = Locale(constantHandler.LOCALE)
    my_clock = pygame.time.Clock()

    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((constantHandler.WIDTH, constantHandler.HEIGHT))

    iconSurface = pygame.image.load(constantHandler.ICON)
    icon = pygame.transform.scale(iconSurface, (constantHandler.ICON_SIZE, constantHandler.ICON_SIZE))
    pygame.display.set_icon(icon)
    pygame.display.set_caption(localeHandler.getString("PYGAME_WINDOW_TITLE"))
    pygame.mouse.set_visible(0)

    allSprites = [] # Keep a list of all sprites in the game

    # Setup for levels and players
    level1 = Level(constantHandler.LEVEL1_1, (constantHandler.WIDTH, constantHandler.HEIGHT))
    allSprites.append(level1)

    player1 = Player(constantHandler.PLAYER, Player.PLAYER1)
    allSprites.append(player1)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break
        elif player1.handleKey(keys):
            pass
        elif level1.handleKey(keys):
            pass


        # Ask every sprite to draw itself.
        for sprite in allSprites:
            sprite.draw(mainSurface)

        pygame.display.update()

        #force a constant frame rate of 60fps
        my_clock.tick(60)

    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()