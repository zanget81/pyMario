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
        print 'blaaaaaaaaaaaaa'
        keys = {pygame.K_LEFT : True, pygame.K_RIGHT : True}

        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(keys)

    def testHandleKeyPlayerLeft(self):
        keys = {pygame.K_LEFT : True, pygame.K_RIGHT : True}

        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.handleKey(keys)

    def testGetSetPosition(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        player1.position = (15,16)
        self.assertEqual(player1.position, (15,16))

    def testGetSetSize(self):
        player1 = Player(Constants.PLAYER, Player.PLAYER1)
        self.assertIsNotNone(player1)
        self.assertEqual(player1.size, (15,16))