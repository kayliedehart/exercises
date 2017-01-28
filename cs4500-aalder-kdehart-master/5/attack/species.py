# A Species (Species board) for the game Evolution

import trait
from random import randint

MAXTRAITS = 3

class Species:
	food = 0
	population = 1
	bodysize = 1
	traits = []

	def __init__(self, food, population, bodysize, traits):
		self.food = food
		self.population = population
		self.bodysize = bodysize
		self.traits = traits

	def getFood(self):
		"""
		Get the number of food tokens of this species.
		"""
		return self.food

	def setFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		if nat < 0:
			raise Exception("Cannot set food to a negative value")
		else:
			self.food = nat

	def addToFood(self, nat):
		"""
		Update the number of food tokens for this species.
		"""
		newFood = self.food + nat
		if newFood < 0:
			raise Exception("Cannot set food to a negative value")
		else:
			self.food = newFood

	def getPopulation(self):
		"""
		Get the current population size for this species.
		"""
		return self.population

	def setPopulation(self, nat):
		"""
		Update the population size of this species.
		"""
		if (nat < 0) or (nat > 7):
			raise Exception("Cannot set population to a negative value or a value greater than 7")
		else:
			self.population = nat

	def addToPopulation(self, nat):
		"""
		Update the population size of this species.
		"""
		newPop = self.population + nat
		if (nat < 0) or (newPop > 7):
			raise Exception("Cannot add a negative value, and cannot set population to a value over 7")
		else:
			self.population = newPop

	def getBodySize(self):
		"""
		Get the current body size of this species.
		"""
		return self.bodysize

	def setBodySize(self, nat):
		"""
		Update the body size of this species.
		"""
		if (nat < 0) or (nat > 7):
			raise Exception("Cannot set body size to a negative value or a value greater than 7")
		else:
			self.bodysize = nat

	def getTraits(self):
		return self.traits

	def discardTrait(self, index):
		"""
		Choose a trait in the current set of self.traits to discard.
		"""
		if index > len(self.traits):
			raise Exception("Not a valid index for traits")
		self.traits.pop(index)

	def setTraits(self, lot):
		"""
		Update the set of Traits this species has.
		"""
		for trait in lot:
			if len(self.traits) < MAXTRAITS:
				self.traits.append(trait)
			else:
				#for now, FIFO
				self.discardTrait(0)
				self.traits.append(trait)

	def isCarnivore(self):
		"""
		Checks if this species has the carnivore trait
		"""
		return ("carnivore" in self.getTraits())

	def hasFatTissue(self):
		"""
		Checks if this species has the fat_tissue trait
		"""
		return ("fat_tissue" in self.getTraits())

	def neighborsHelp(self, neighborLeft, neighborRight):
		"""
		Returns boolean value for if a Species' neighbors can help prevent an attack,
		given a list of neighboring Species
		"""
		for neighbor in [neighborLeft, neighborRight]:
			if neighbor:
				if trait.Trait.warning_call in neighbor.traits:
					return True
		return False

	def canBurrow(self, defender):
		"""
		Returns boolean whether a defender can successfully use burrowing
		"""
		return  defender.getFood() == defender.getPopulation()

	def goodSymbiosis(self, defender, neighborRight):
		"""
		Returns whether symbiosis helps the defender avoid attack, ie:
		if the neighbor to their right has a larger body size then the defender
		"""
		if neighborRight:
			return defender.getBodySize() < neighborRight.getBodySize()
		return False

	def blockingShell(self, attacker, defender):
		"""
		Returns whether a defender with hard_shell can defend against their attacker
		"""
		return (attacker.getBodySize() - defender.getBodySize()) <= 3

	def herdingHelp(self, attacker, defender):
		"""
		Returns whether a defender with herding can successfully block an attacker
		"""
	 	attackers_popsize = attacker.getPopulation()
		if trait.Trait.pack_hunting in attacker.traits:
			attackers_popsize += attacker.getBodySize()

		return attackers_popsize <= defender.getPopulation()


	def attackable(self, situation):
			"""
			Checks to see if an attack is successful in the given Situation.
			A Situation is [defender:Species, attacker:Species, (optional neighbor:Species, neighbor:Species)]
			Returns a Boolean.
			"""
			attacker, defender, neighborLeft, neighborRight = situation
			if trait.Trait.carnivore in attacker.traits:
				if attacker is defender:
					raise Exception("A species cannot attack itself")
				if defender.getPopulation() == 0:
					return False
				if (trait.Trait.ambush not in attacker.traits) and self.neighborsHelp(neighborLeft, neighborRight):
					return False
				if (trait.Trait.climbing in defender.traits) and not (trait.Trait.climbing in attacker.traits):
					return False
				if trait.Trait.burrowing in defender.traits and self.canBurrow(defender):
					return False
				if trait.Trait.symbiosis in defender.traits and self.goodSymbiosis(defender, neighborRight):
					return False
				if trait.Trait.hard_shell in defender.traits and self.blockingShell(attacker, defender):
					return False
				if trait.Trait.herding in defender.traits and self.herdingHelp(attacker, defender):
					return False
				else:
					return True
			else:
				raise Exception("Attacking Species must be a carnivore")








