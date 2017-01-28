# Unit-testing for main component methods. Due to lack of player component there are no tests.

import unittest
import dealer
import components
#import player
import main

class TestMainMethods(unittest.TestCase):

  def setUp(self):
    self.game = main(4)

  def tearDown(self):
    del self.game


if __name__ == '__main__':
    unittest.main()