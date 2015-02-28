import unittest
from src.player import Player
from src.constants import Constants

class Test(unittest.TestCase):

    def testCreatePlayer(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)

    def testUpdatePlayerRight(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.update(Constants.RIGHT)

    def testUpdatePlayerLeft(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.update(Constants.LEFT)


    def testHandleKeyPlayerRight(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(Constants.RIGHT)

    def testHandleKeyPlayerLeft(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(Constants.LEFT)