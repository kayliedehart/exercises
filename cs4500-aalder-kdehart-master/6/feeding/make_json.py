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

	def parseTraits(self, traits):
		"""
		Corrects the quotes so that the object returns correctly
		"""
		new_str = "["
		for t in traits:
			str_trait = '\"' + t.value + '\"'
			if (traits.index(t) != len(traits)-1):
				str_trait = str_trait + ','
			new_str = new_str + str_trait
		new_str = new_str + "]"
		new_str =  new_str.replace("'", '"')
		return new_str

	def make_speciesPlus(self, speciesPlus):
		"""
		Construct a string in the format of a JSON Species+
		"""
		str_species = ('[["food",{}],["body",{}],["population",{}],'.format(
																							 speciesPlus.getFood(),
																						   speciesPlus.getBodySize(),
																						   speciesPlus.getPopulation()))
		str_species = str_species + '["traits",{}]'.format(self.parseTraits(speciesPlus.getTraits()))

		if trait.Trait.fat_tissue in speciesPlus.getTraits():
			str_species = str_species + ',["fat-food",{}]]'.format(speciesPlus.getFatFood())
		else:
			str_species = str_species + "]"
		return str_species

	def make_player(self, player):
		"""
		Construct a string in the format of a JSON Player
		"""
		str_player = '[["id",{}],["species",['.format(player.getPlayerId())
		sb = player.getSpeciesBoards()

		for s in sb:
			str_player = str_player + self.make_speciesPlus(s)
			if(sb.index(s) != len(sb)-1):
				str_player = str_player + ','

		str_player = str_player + ']],["bag",{}]]'.format(player.getFoodBag())

		return str_player

	def make_meal(self, feeding_out):
		"""
		Construct a JSON message to describe a player's feeding decision.
		The output is one of:
			false,
			Species+,
			[Species+, Nat],
			[Species+, Player, Species+]
		"""
		if not feeding_out:
			return json.dump(False, sys.stdout)
		if len(feeding_out) == 1:
			return json.dump(json.loads(self.make_speciesPlus(feeding_out[0])), sys.stdout)
		else:
			meal = "["
			for item in feeding_out:
				if isinstance(item, species.Species):
					meal = meal + self.make_speciesPlus(item)
				elif isinstance(item, int):
					meal = meal + "," + str(item)
				elif isinstance(item, player.Player):
					meal = meal + "," + (self.make_player(item)) + ","
			meal = meal + "]"
			meal = meal[1:-1]
			m = json.load(meal)
		return json.dump(m, sys.stdout)
		#return json.dumps(m)

	def make_attack(self, attack):
		"""
		Construct a JSON message to describe the result of an species' attack scenario (Boolean)
		"""

		return json.dump(attack, sys.stdout)

	def make_attack_test(self, attack):
		"""
		Show the result of an attack, but don't print to stdout (for testing purposes)
		"""

		return json.dumps(attack)