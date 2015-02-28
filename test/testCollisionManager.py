import unittest
from src.collisionManager import CollisionManager
from src.constants import Constants

class Test(unittest.TestCase):

    def testLoadLevelFileCorrectly(self):
        cmInstance = CollisionManager()
        cmInstance.loadLevelFile(Constants.LEVEL1_1_COLLISIONS_FILE)

    def testCheckCollisionCorrectly(self):
        cmInstance = CollisionManager()
        cmInstance.checkCollisions()