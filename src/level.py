__author__ = 'angel'

import pygame
from constants import Constants

class Level(object):
    LIMIT_TO_THE_LEVEL = 85

    def __init__(self, img, windowSize, player):
        self.img = pygame.image.load(img)
        self.tPos = (0,0);
        self.windowSize = windowSize
        self.player = player


    def update(self):
        characterPosition = self.player.position

        if characterPosition[0] > self.LIMIT_TO_THE_LEVEL:
            self.tPos = (self.tPos[0]+5, self.tPos[1])

    def draw(self, targetSurface):
        patch_rect = (self.tPos[0], self.tPos[1],
                      self.windowSize[0], self.windowSize[1])
        targetSurface.blit(self.img, (0,0), patch_rect)

    def handleKey(self, keys):
        if keys[pygame.K_RIGHT]:
            self.update()
        elif keys[pygame.K_LEFT]:
            self.update()