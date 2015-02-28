

class PhysicsManager:

    __listObjects = []

    def __init__(self):
        self.__listObjects = []

    def registerWorldObject(self, worldObject):
        self.__listObjects.append(worldObject)

    def applyPhysics(self):
        pass