# The basic card and stack components for the main components to pass around
from random import randint

MAXBULL = 7
MINBULL = 2

class Card:
	number = 0
	bull = 0

	def __init__(self, number):
		self.number = number
		self.setBullNumber(None)

	def getNumber(self):
		return self.number

	def getBullNumber(self):
		return self.bull

	def setBullNumber(self, number):
		if (type(number) is not int) or (number < MINBULL) or (number > MAXBULL):
			random_bull = randint(MINBULL, MAXBULL+1)
			self.bull = random_bull
		else:
			self.bull = number


class Stack:
	cards = []

	def __init__(self, card):
		self.cards = [card]

	def getCards(self):
		return self.cards

	def setCard(self, card):
		self.cards.append(card)

	def getLength(self):
		length = 0
		for card in self.cards:
			length += 1
		return length