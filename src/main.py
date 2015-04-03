__author__ = 'angel'

import pygame
from constants import Constants
from locale import Locale
from player import Player
from level import Level
from collisionManager import CollisionManager
from physicsManager import PhysicsManager

def main():

    localeHandler = Locale(Constants.LOCALE)
    my_clock = pygame.time.Clock()
    frameCounter = 0

    """ Set up the game and run the main game loop """
    pygame.init()  # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))

    iconSurface = pygame.image.load(Constants.ICON)
    icon = pygame.transform.scale(iconSurface, (Constants.ICON_SIZE, Constants.ICON_SIZE))
    pygame.display.set_icon(icon)
    pygame.display.set_caption(localeHandler.getString("PYGAME_WINDOW_TITLE"))
    pygame.mouse.set_visible(0)

    allSprites = [] # Keep a list of all sprites in the game

    #TODO: Some of this things needs to go into a screen manager

    # Setup for levels and players
    player1 = Player(Constants.PLAYER, Player.PLAYER1)
    level1 = Level(Constants.LEVEL1_1_BACKGROUND, (Constants.WIDTH, Constants.HEIGHT), player1)

    allSprites.append(level1)
    allSprites.append(player1)

    # game helpers
    collisionManagerInstance = CollisionManager()
    collisionManagerInstance.loadLevelFile(Constants.LEVEL1_1_COLLISIONS_FILE)

    physicsManagerInstance = PhysicsManager()

    collisionManagerInstance.registerWorldObject(player1)
    physicsManagerInstance.registerWorldObject(player1)


    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break

        player1.handleKey(keys)
        level1.handleKey(keys)

        collisionManagerInstance.checkCollisions()
        physicsManagerInstance.applyPhysics()
        collisionManagerInstance.checkCollisions()

        # Ask every sprite to draw itself.
        for sprite in allSprites:
            sprite.draw(mainSurface)

        pygame.display.update()

        #force a constant frame rate of 60fps
        my_clock.tick(Constants.FRAME_RATE)

    pygame.quit()     # Once we leave the loop, close the window.

if __name__ == "__main__":
    main()