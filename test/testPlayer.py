import unittest
import pygame
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
        keys = {pygame.K_RIGHT : True}

        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(keys)

    def testHandleKeyPlayerLeft(self):
        keys = {pygame.K_LEFT : True}

        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(keys)

    def testGetSetPosition(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.position = (0,50)
        self.assertEqual(player1.position, (0,50))