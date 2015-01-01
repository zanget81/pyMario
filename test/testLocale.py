import unittest
import logging
from src.constants import Constants
from src.locale import Locale

class Test(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)


    def testGetStringThatExists(self):
        localeHandler = Locale(Constants().LOCALE)
        valueString = localeHandler.getString("PYGAME_WINDOW_TITLE")
        self.assertEqual(valueString, "PyMario")
