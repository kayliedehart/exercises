# Unit-testing suite for 6 Nimmt! methods in dealer component (no player component)
import unittest
import dealer
import components
#import player

class TestDealerMethods(unittest.TestCase):
	def setUp(self):
		self.dealerEmpty1 = dealer.Dealer([])
		self.dealerEmpty2 = dealer.Dealer([])

	def tearDown(self):
		del self.dealerEmpty1
		del self.dealerEmpty2

	def testGetPlayersEmpty(self):
		self.assertEqual(self.dealerEmpty1.getPlayers(), [])

	def testGetDeck(self):
		self.assertEqual(self.dealerEmpty1.getDeck(), self.dealerEmpty2.getDeck())

	def testSetStacks(self):
		self.dealerEmpty1.setStacks()
		self.assertEqual(len(self.dealerEmpty1.getStacks()), 4)

	def testGetStacksEmpty(self):
		self.assertEqual(len(self.dealerEmpty1.getStacks()), 0)

	def testDealFirst(self):
		self.dealerEmpty1.setStacks()
		self.assertEqual(len(self.dealerEmpty1.dealFirst()), 10)


if __name__ == '__main__':
		unittest.main()