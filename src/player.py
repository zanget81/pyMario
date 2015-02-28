__author__ = 'angel'

import pygame
from constants import Constants

class Player(object):

    PLAYER1 = 1
    PLAYER2 = 2
    SPRITE_INITIAL_LEFT = 80
    SPRITE_SMALL_MARIO_TOP = 32
    SPRITE_MARIO_WIDTH = 15
    SPRITE_SMALL_MARIO_HEIGHT = 16

    INITIAL_X = 41
    INITIAL_Y = 184

    def __init__(self, img, player):
        self.img = pygame.image.load(img)
        self.tPreviousPos = (self.INITIAL_X,self.INITIAL_Y);
        self.tCurrentPos = (self.INITIAL_X,self.INITIAL_Y);
        self.player = player

    def update(self, movementDirection):
        if movementDirection == Constants.RIGHT:
            self.tPreviousPos = self.tCurrentPos
            self.tCurrentPos = (self.tCurrentPos[0]+1, self.tCurrentPos[1]);
        elif movementDirection == Constants.LEFT:
            self.tPreviousPos = self.tCurrentPos
            self.tCurrentPos = (self.tCurrentPos[0]-1, self.tCurrentPos[1]);

    def getPlayerImage(self):
        image = (self.SPRITE_INITIAL_LEFT,
                 self.SPRITE_SMALL_MARIO_TOP,
                 self.SPRITE_MARIO_WIDTH,
                 self.SPRITE_SMALL_MARIO_HEIGHT)

        return image

    @property
    def position(self):
        return self.tCurrentPos

    @position.setter
    def position(self, value):
        self.tPreviousPos = self.tCurrentPos
        self.tCurrentPos = value

    @property
    def size(self):
        image = self.getPlayerImage()
        return image[2],image[3]


    def handleCollision(self):
        self.tCurrentPos = self.tPreviousPos

    def draw(self, targetSurface):
        #cropped = pygame.Surface((self.SPRITE_MARIO_WIDTH, self.SPRITE_SMALL_MARIO_HEIGHT))
        #cropped.blit(self.img, (0, 0), self.getPlayerImage())
        #scaled = pygame.transform.scale(cropped, (75, 48))

        targetSurface.blit(self.img, self.tCurrentPos, self.getPlayerImage())

    def handleKey(self, keys):
        if keys[pygame.K_RIGHT]:
            self.update(Constants.RIGHT)
        elif keys[pygame.K_LEFT]:
            self.update(Constants.LEFT)