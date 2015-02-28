import unittest
from src.player import Player
from src.constants import Constants

class Test(unittest.TestCase):

    def testCreatePlayer(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
