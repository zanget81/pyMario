import unittest
from src.physicsManager import PhysicsManager
from src.player import Player
from src.constants import Constants

class Test(unittest.TestCase):

    def testRegisterObject(self):
        fmInstance = PhysicsManager()
        player1 = Player(Constants.PLAYER, Player.PLAYER1)

        fmInstance.registerWorldObject(player1)

    def testApplyPhysics(self):
        fmInstance = PhysicsManager()
        player1 = Player(Constants.PLAYER, Player.PLAYER1)

        fmInstance.registerWorldObject(player1)
        fmInstance.applyPhysics()