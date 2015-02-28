import json
import pygame

class CollisionManager(object):

    __listObjects = []
    __collisionList = []

    def __init__(self):
        self.__listObjects = []

    def loadLevelFile(self, filePath):
        with open(filePath) as collisionFile:
            self.__collisionList = json.load(collisionFile)

    def registerWorldObject(self, worldObject):
        self.__listObjects.append(worldObject)

    def checkCollisions(self):
        for element in self.__listObjects:
            if element.position is not None and element.size is not None:
                elementRectangle = pygame.Rect(element.position, element.size)
                for collision in self.__collisionList:
                    if elementRectangle.colliderect(collision["rectangle"]["left"],
                                                    collision["rectangle"]["top"],
                                                    collision["rectangle"]["width"],
                                                    collision["rectangle"]["height"]):

                        if element.handleCollision is not None:
                            element.handleCollision()
                        break



