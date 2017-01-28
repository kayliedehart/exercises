# handles JSON parsing for the game Evolution

import trait
import species
import player
import dealer
import json


class ParseJSON:

	def __init__(self):
		pass

	def parse_situation(self, situation):
		"""
		Reconstruct the JSON input of a situation into a list of
		[attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)]
		and return that list.
		"""
		species_list = []
		for speciesboard in situation:
			if speciesboard:
				s = self.parse_loSpecies([speciesboard])
				species_list = species_list + s
			else:
				species_list.append(False)
		return species_list

	def parse_traits(self, traits):
		"""
		Make a list of Traits from a given JSON list of traits
		"""
		trait_list = []
		for t in traits:
			new_trait = trait.Trait(t)
			trait_list.append(new_trait)
		return trait_list


	def parse_loSpecies(self, LOS):
		"""
		make a list of Species from a JSON LOS. A JSON Species+ is:
			[["food",Nat],
		     ["body",Nat],
		     ["population",Nat],
		     ["traits",LOT]
		     ["fat-food" ,Nat]]
		"""
		species_list = []
		for speciesboard in LOS:
			keywords = ((speciesboard[0][0] == "food") and (speciesboard[1][0] == "body")
						 and (speciesboard[2][0] == "population") and (speciesboard[3][0] == "traits"))
			if speciesboard and keywords:
				this_species = species.Species(speciesboard[0][1], speciesboard[1][1], speciesboard[2][1], self.parse_traits(speciesboard[3][1]))
				if this_species.hasFatTissue():
					try:
						this_species.setFatFood(speciesboard[4][1])
					except IndexError:
						pass
				species_list.append(this_species)
			elif not keywords:
				raise Exception("Keywords don't match")
		return species_list



	def parse_player(self, jplayer):
		"""
		make a Player from a JSON Player. A JSON Player is:
				    [["id",Natural+],
     				["species",LOS],
     				["bag",Natural]]
		"""
		keywords = ((jplayer[0][0] == "id") and (jplayer[1][0] == "species") and (jplayer[2][0] == "bag"))
		if jplayer and keywords:
			ident = jplayer[0][1]
			species = self.parse_loSpecies(jplayer[1][1])
			bag = jplayer[2][1]

			if (ident > 0) and (bag >= 0):
				return player.Player(ident, species, bag)
			else:
				raise Exception("Invalid player specifications")
		else: 
			raise Exception("No player given")



	def parse_feeding(self, feeding):
		"""
		Reconstruct the JSON input of a "feeding" into Python: Feeding is [Player, Natural+, LOP]

		"""
		current_player = self.parse_player(feeding[0])
		free_food = feeding[1]
		all_players = []
		for player in feeding[2]:
			player = self.parse_player(player)
			all_players.append(player)

		return [current_player, free_food, all_players]