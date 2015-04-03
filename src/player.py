__author__ = 'angel'

import pygame
import math
from constants import Constants

class Player(object):

    PLAYER1 = 1
    PLAYER2 = 2
    SPRITE_INITIAL_LEFT = 80
    SPRITE_WALK1_LEFT = 98
    SPRITE_WALK2_LEFT = 115
    SPRITE_WALK3_LEFT = 128
    SPRITE_SMALL_MARIO_TOP = 32
    SPRITE_MARIO_STANDARD_WIDTH = 15
    SPRITE_MARIO_WALK1_WIDTH = 12
    SPRITE_MARIO_WALK2_WIDTH = 11
    SPRITE_MARIO_WALK3_WIDTH = 15
    SPRITE_SMALL_MARIO_HEIGHT = 16
    SPRITE_SMALL_MARIO_GAP = 18

    SPRITE_NUMBER_OF_WALKING_ANIMATIONS = 4

    INITIAL_X = 41
    INITIAL_Y = 184
    DISTANCE_TRAVELLED = 0.5

    def __init__(self, img, player):
        self.img = pygame.image.load(img)
        self.tPreviousPos = (self.INITIAL_X,self.INITIAL_Y);
        self.tCurrentPos = (self.INITIAL_X,self.INITIAL_Y);
        self.player = player
        self.currentAnimNumber = 0
        self.animationRate = Constants.FRAME_RATE / self.SPRITE_NUMBER_OF_WALKING_ANIMATIONS
        self.runningPos = [self.SPRITE_INITIAL_LEFT, self.SPRITE_WALK1_LEFT, self.SPRITE_WALK2_LEFT, self.SPRITE_WALK3_LEFT]
        self.runningWidth = [self.SPRITE_MARIO_STANDARD_WIDTH, self.SPRITE_MARIO_WALK1_WIDTH, self.SPRITE_MARIO_WALK2_WIDTH, self.SPRITE_MARIO_WALK3_WIDTH]

    def update(self, movementDirection):
        if movementDirection == Constants.RIGHT:
            self.tPreviousPos = self.tCurrentPos
            self.tCurrentPos = (self.tCurrentPos[0] + self.DISTANCE_TRAVELLED, self.tCurrentPos[1]);

            if (self.currentAnimNumber != (self.SPRITE_NUMBER_OF_WALKING_ANIMATIONS -1)):
                self.currentAnimNumber = (self.currentAnimNumber+1)

        elif movementDirection == Constants.LEFT:
            self.tPreviousPos = self.tCurrentPos
            self.tCurrentPos = (self.tCurrentPos[0] - self.DISTANCE_TRAVELLED, self.tCurrentPos[1]);

    def getPlayerImage(self):
        image = (self.runningPos[self.currentAnimNumber],
                 self.SPRITE_SMALL_MARIO_TOP,
                 self.runningWidth[self.currentAnimNumber],
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
        else:
            self.currentAnimNumber = 0;
