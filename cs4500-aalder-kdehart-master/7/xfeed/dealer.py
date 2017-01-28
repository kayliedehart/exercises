# The Dealer in a game of Evolution
import trait
import species

class Dealer:
	wateringHole = 0
	deck = None
	listOfPlayers = []

	def __init__(self):
		self.wateringHole = 0
		self.listOfPlayers = []

	def setWateringHole(self, numFoodTokens):
		self.wateringHole = numFoodTokens

	def getWateringHole(self):
		return self.wateringHole

	def setListOfPlayers(self, players):
		self.listOfPlayers = players

	def getListOfPlayers(self):
		return self.listOfPlayers

	def setDeck(self, deck):
		self.deck = deck

	def getDeck(self):
		return self.deck