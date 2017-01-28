#unit tests for player component of 6 Nimmt!

import unittest
import components
import player

class TestPlayerMethods(unittest.TestCase):

  def setUp(self):
    self.card1 = components.Card(1)
    self.card2 = components.Card(2)
    self.stack1 = components.Stack(self.card1)
    self.stack2 = components.Stack(self.card2)
    self.player0 = player.Player(0)

  def tearDown(self):
    del self.card1
    del self.card2
    del self.stack1
    del self.player0

  def testGetName(self):
    self.assertEqual(self.player0.getName(), 0)

  def testGetHand(self):
    self.assertEqual(self.player0.getHand(), [])

  def testSetHand(self):
    self.player0.setHand([self.card1])
    self.assertEqual(len(self.player0.getHand()), 1)

  def testPlayCard(self):
    self.player0.setHand([self.card1])
    self.assertEqual(self.player0.playCard(self.stack2), self.card1)

  def testTotalBull(self):
    self.assertEqual(self.player0.totalBull(self.stack1), self.card1.getBullNumber())

  def testPickStack(self):
    self.assertEqual(self.player0.pickStack([self.stack1]), self.stack1)

  def testPickNoStack(self):
    self.assertEqual(self.player0.pickStack([]), [])

if __name__ == '__main__':
    unittest.main()

