# Create JSON representations of Evolution python objects
import sys
import trait
import species
import player
import dealer
import json


class MakeJSON:

	def __init__(self):
		pass

	def make_meal(self, feeding_out):
		"""
		Construct a JSON message to describe a player's feeding decision.
		The output is one of:
			false : no species is to be fed
			Nat : index of a Herbivore
			[Nat, Nat] : index of a Herbivore and the amount of Fat Food to consume
			[Nat, Nat, Nat] : index of a Carnivore, the Player index of the owner of 
				the victim species, and the index of the victim
		"""
		return json.dumps(feeding_out)

	def make_attack(self, attack):
		"""
		Construct a JSON message to describe the result of an species' attack scenario (Boolean)
		"""
		return json.dumps(attack)
