__author__ = 'angel'

import pygame

class Level(object):

    def __init__(self, img, windowSize):
        self.img = pygame.image.load(img)
        self.tPos = (0,0);
        self.windowSize = windowSize

    def update(self, movementDirection):
        pass

    def draw(self, targetSurface):
        patch_rect = (0, 0,
                      self.windowSize[0], self.windowSize[1])
        targetSurface.blit(self.img, self.tPos, patch_rect)

    def handleKey(self, key):
        pass