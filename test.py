import unittest

from main import add

class MainTest(unittest.TestCase):
    def test_add(self):
        x = add(5, 5)

        self.assertEquals(x, 10)