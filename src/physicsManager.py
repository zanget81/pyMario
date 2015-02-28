
from constants import Constants

class PhysicsManager(object):

    GRAVITY = 9.81

    __listObjects = []

    def __init__(self):
        self.__listObjects = []

    def registerWorldObject(self, worldObject):
        self.__listObjects.append(worldObject)

    def applyPhysics(self):
        for element in self.__listObjects:
            if element.position is not None:
                newPositionY = element.position[1] + self.GRAVITY / Constants.FRAME_RATE
                element.position = (element.position[0], newPositionY)