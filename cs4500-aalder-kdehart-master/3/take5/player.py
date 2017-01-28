# the Player component for a game of 6 Nimmt!
import components

class Player:
	name = None
	hand = []
	current_deck = []

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def getHand(self):
		return self.hand

	def setHand(self, hand):
		self.hand = hand

	def playCard(self, deck):
		self.current_deck = deck
		chosen_card = None
		highest_face = 0
		for card in self.hand:
			if card.getNumber() > highest_face:
				chosen_card = card

		self.hand.remove(chosen_card)
		return chosen_card

	def totalBull(self, stack):
		points = 0
		if stack:
			for card in stack.getCards():
				points += card.getBullNumber()
		return points

	def pickStack(self, stacks):
		try: 
			selected_stack = stacks[0]
			for stack in stacks:
				if self.totalBull(stack) < self.totalBull(selected_stack):
					selected_stack = stack
		except:
			selected_stack = []
		return selected_stack
