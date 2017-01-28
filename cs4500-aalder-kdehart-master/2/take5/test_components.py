#tests for card and stack class methods
import unittest
import components

class TestComponentsMethods(unittest.TestCase):
  def setUp(self):
    self.card1 = components.Card(1)
    self.card2 = components.Card(2)
    self.stack1 = components.Stack(self.card1)


  def tearDown(self):
    del self.card1
    del self.card2
    del self.stack1

  def testGetNumber(self):
    answer = self.card1.getNumber()
    self.assertEqual(answer, 1)

  def testGetBullNumber(self):
    bullNum = self.card1.getBullNumber()
    if((bullNum <= 7) or (bullNum >= 2)) :
      self.assertEqual(True, True)
    else :
      self.assertEqual(True, False)

  def testSetBullNumber(self):
    self.card1.setBullNumber(3)
    self.assertEqual(self.card1.getBullNumber(), 3)

  def testGetCards(self):
    self.assertEqual(self.stack1.getCards()[0].getNumber(), self.card1.getNumber())

  def testSetCards(self):
    self.stack1.setCard(self.card2)
    self.assertEqual(self.stack1.getCards()[1].getNumber(), self.card2.getNumber())


if __name__ == '__main__':
  unittest.main()