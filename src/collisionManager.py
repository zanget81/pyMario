__author__ = 'angel'


class CollisionManager:

    __listObjects = []

    def __init__(self):
        self.__listObjects = []

    def loadLevelFile(self, filePath):
        pass

    def registerWorldObject(self, worldObject):
        self.__listObjects.append(worldObject)

    def checkCollisions(self):
        pass

