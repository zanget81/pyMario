__author__ = 'angel'

import pygame
from constants import Constants

class Player:

    PLAYER1 = 1
    PLAYER2 = 2
    SPRITE_INITIAL_LEFT = 80
    SPRITE_SMALL_MARIO_TOP = 32
    SPRITE_MARIO_WIDTH = 15
    SPRITE_SMALL_MARIO_HEIGHT = 16

    def __init__(self, img, player):
        self.constantHandler = Constants()
        self.img = pygame.image.load(img)
        self.tPos = (0,0);
        self.player = player

    def update(self, movementDirection):
        if movementDirection == self.constantHandler.RIGHT:
            self.tPos = (self.tPos[0]+1, self.tPos[1]);
        elif movementDirection == self.constantHandler.LEFT:
            self.tPos = (self.tPos[0]-1, self.tPos[1]);

    def getPlayerImage(self):
        image = (self.SPRITE_INITIAL_LEFT,
                 self.SPRITE_SMALL_MARIO_TOP,
                 self.SPRITE_MARIO_WIDTH,
                 self.SPRITE_SMALL_MARIO_HEIGHT)

        return image

    def draw(self, targetSurface):
        #cropped = pygame.Surface((self.SPRITE_MARIO_WIDTH, self.SPRITE_SMALL_MARIO_HEIGHT))
        #cropped.blit(self.img, (0, 0), self.getPlayerImage())
        #scaled = pygame.transform.scale(cropped, (75, 48))

        targetSurface.blit(self.img, self.tPos, self.getPlayerImage())

    def handleKey(self, keys):
        if keys[pygame.K_RIGHT]:
            self.update(self.constantHandler.RIGHT)
        elif keys[pygame.K_LEFT]:
            self.update(self.constantHandler.LEFT)