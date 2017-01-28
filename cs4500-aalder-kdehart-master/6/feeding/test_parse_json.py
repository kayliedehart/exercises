# unit tests for parse_json

import trait
import species
import player
import dealer
import json
import unittest
import parse_json

class TestParseJSON(unittest.TestCase):

	def setUp(self):
		self.parse_json = parse_json.ParseJSON()
		self.false = json.dumps(False)
		self.spec1 = species.Species(0,1,1,["carnivore"])
		self.spec2 = species.Species(1,3,3,["herding"])
		self.spec3 = species.Species(1,2,4,["carnivore", "ambush"])
		self.spec4 = species.Species(0,3,2,[])

		self.spec5 = species.Species(0,4,2,["carnivore"])
		self.spec6 = species.Species(1,3,3,["herding"])
		self.spec7 = species.Species(1,2,4,["carnivore", "ambush"])
		self.spec8 = species.Species(0,1,2,[])

		self.spec9 = species.Species(0,1,1,["symbiosis"])
		self.spec10 = species.Species(0,3,1,["warning-call"])
		self.spec11 = species.Species(2,2,2,[])
		self.spec12 = species.Species(0,1,1,[])

		self.spec13 = species.Species(0,1,1,[])
		self.spec14 = species.Species(0,5,1,["fat-tissue"])
		self.spec14.setFatFood(5)
		self.spec15 = species.Species(0,6,1,["warning-call"])
		self.spec16 = species.Species(2,2,2,[])

		self.spec17 = species.Species(0,1,1,[])
		self.spec18 = species.Species(0,1,1,[])
		self.spec19 = species.Species(0,3,2,["carnivore", "fat-tissue"])
		self.spec19.setFatFood(3)
		self.spec20 = species.Species(3,3,6,[])

		self.spec21 = species.Species(0,5,4,[])
		self.spec22 = species.Species(2,2,2,[])


		self.player1 = player.Player(1, [self.spec1], 0)
		self.player2 = player.Player(2, [self.spec2, self.spec3], 0)
		self.player3 = player.Player(3, [self.spec4], 0)

		self.player4 = player.Player(1, [self.spec5], 0)
		self.player5 = player.Player(2, [self.spec6, self.spec7], 0)
		self.player6 = player.Player(3, [self.spec8], 0)

		self.player7 = player.Player(1, [self.spec9], 0)
		self.player8 = player.Player(2, [self.spec10, self.spec11], 0)
		self.player9 = player.Player(3, [self.spec12], 0)

		self.player10 = player.Player(1, [self.spec13], 0)
		self.player11 = player.Player(2, [self.spec14, self.spec15], 0)
		self.player12 = player.Player(3, [self.spec16], 0)

		self.player13 = player.Player(1, [self.spec17], 0)
		self.player14 = player.Player(2, [self.spec18, self.spec19], 0)
		self.player15 = player.Player(3, [self.spec20], 0)

		self.player16 = player.Player(1, [], 0)


		self.json_spec1 = [["food",0],
							  ["body",1],
							  ["population",1],
							  ["traits",
							     ["carnivore"]]]
		self.json_spec2 = [["food",1],
							["body",3],
							["population",3],
							["traits",
								["herding"]]]
		self.json_spec3 = [["food",1],
								  ["body",2],
								  ["population",4],
								  ["traits",
								     ["carnivore", "ambush"]]]
		self.json_spec4 = [["food",0],
								  ["body",3],
								  ["population",2],
								  ["traits", []]]
		self.json_spec5 = [["food",0],
							  ["body",4],
							  ["population",2],
							  ["traits",
							    ["carnivore"]]]
		self.json_spec6 = [["food",1],
							["body",3],
					        ["population",3],
							["traits",
							    ["herding"]]]
		self.json_spec7 = [["food",1],
							["body",2],
							["population",4],
							["traits",
								["carnivore", "ambush"]]]
		self.json_spec8 = [["food",0],
						 ["body",1],
						 ["population",1],
						 ["traits",[]]]
		self.json_spec9 = [["food",0],
						   ["body",1],
						   ["population",1],
						   ["traits",
							    ["symbiosis"]]]
		self.json_spec10 = [["food",0],
						   ["body",3],
					       ["population",1],
					       ["traits",
							   ["warning-call"]]]
		self.json_spec11 = [["food",2],
							 ["body",2],
							 ["population",2],
							 ["traits",[]]]
		self.json_spec12 = [["food",0],
							 ["body",1],
							 ["population",1],
							 ["traits", []]]
		self.json_spec13 = [["food",0],
							 ["body",1],
							 ["population",1],
							 ["traits",[]]]
		self.json_spec14 = [["food",0],
						   ["body",5],
						   ["population",1],
						   ["traits",
							    ["fat-tissue"]],
						   ["fat-food", 5]]
		self.json_spec15 = [["food",0],
						   ["body",6],
						   ["population",1],
						   ["traits",
							    ["warning-call"]]]
		self.json_spec16 = [["food",2],
							  ["body",2],
							  ["population",2],
							  ["traits", []]]
		self.json_spec17 = [["food",0],
							  ["body",1],
							  ["population",1],
							  ["traits", []]]
		self.json_spec18 = [["food",0],
							  ["body",1],
							  ["population",1],
							  ["traits",[]]]
		self.json_spec19 = [["food",0],
						   ["body",3],
						   ["population",2],
						   ["traits",
						   	["carnivore", "fat-tissue"]],
						   ["fat-food", 3]]
		self.json_spec20 = [["food",3],
						  ["body",3],
						  ["population",6],
						  ["traits", []]]
		self.json_spec21 = [["food",0],
							 ["body",5],
							 ["population",4],
							 ["traits", []]]
		self.json_spec22 = [["food",2],
						  ["body",2],
						  ["population",2],
						  ["traits",[]]]

		self.json_player1 = [["id",1],
							  ["species",
							     	[[["food",0],
									  ["body",1],
									  ["population",1],
									  ["traits",
									     ["carnivore"]]]]],
							  ["bag",0]]
		self.json_player2 = [["id",2],
						    ["species",
						     	[[["food",1],
								  ["body",3],
								  ["population",3],
								  ["traits",
								     ["herding"]]],
								 [["food",1],
								  ["body",2],
								  ["population",4],
								  ["traits",
								     ["carnivore", "ambush"]]]]],
						    ["bag",0]]
		self.json_player3 = [["id",3],
						    ["species",
						     	[[["food",0],
								  ["body",3],
								  ["population",2],
								  ["traits", []]]]],
						    ["bag",0]]
		self.json_player4 = [["id",1],
							  ["species",
							     	[[["food",0],
									  ["body",4],
									  ["population",2],
									  ["traits",
									    ["carnivore"]]]]],
							  ["bag",0]]
		self.json_player5 = [["id",2],
							   ["species",
							      [[["food",1],
									["body",3],
							        ["population",3],
									["traits",
									    ["herding"]]],
								   [["food",1],
									["body",2],
									["population",4],
									["traits",
									    ["carnivore", "ambush"]]]]],
							   ["bag",0]]
		self.json_player6 = [["id",3],
						    ["species",
						     	[[["food",0],
								  ["body",1],
								  ["population",2],
								  ["traits",[]]]]],
						    ["bag",0]]
		self.json_player7 = [["id",1],
							  ["species",
							     [[["food",0],
								   ["body",1],
								   ["population",1],
								   ["traits",
									    ["symbiosis"]]],
								  [["food",0],
								   ["body",3],
							       ["population",1],
							       ["traits",
									   ["warning-call"]]]]],
							  ["bag",0]]
		self.json_player8 = [["id",2],
						    ["species",
						       [[["food",2],
								 ["body",2],
								 ["population",2],
								 ["traits",[]]],
								[["food",0],
								 ["body",1],
								 ["population",1],
								 ["traits", []]]]],
						    ["bag",0]]
		self.json_player9 = [["id",3],
						    ["species",
						       [[["food",0],
								 ["body",1],
								 ["population",1],
								 ["traits",[]]]]],
						    ["bag",0]]
		self.json_player10 = [["id",1],
							  ["species",
							     [[["food",0],
								   ["body",5],
								   ["population",1],
								   ["traits",
									    ["fat-tissue"]],
								   ["fat-food", 5]],
								  [["food",0],
								   ["body",6],
								   ["population",1],
								   ["traits",
									    ["warning-call"]]]]],
							  ["bag",0]]
		self.json_player11 = [["id",2],
							    ["species",
							     	[[["food",2],
									  ["body",2],
									  ["population",2],
									  ["traits", []]],
									 [["food",0],
									  ["body",1],
									  ["population",1],
									  ["traits", []]]]],
							    ["bag",0]]
		self.json_player12 = [["id",3],
							    ["species",
							     	[[["food",0],
									  ["body",1],
									  ["population",1],
									  ["traits",[]]]]],
							    ["bag",0]]
		self.json_player13 = [["id",1],
							  ["species",
							     [[["food",0],
								   ["body",3],
								   ["population",2],
								   ["traits",
								   	["carnivore", "fat-tissue"]],
								   ["fat-food", 3]]]],
							  ["bag",0]]
		self.json_player14 = [["id",2],
							    ["species",
							     	[[["food",3],
									  ["body",3],
									  ["population",6],
									  ["traits", []]],
									[["food",0],
									 ["body",5],
									 ["population",4],
									 ["traits", []]]]],
							    ["bag",0]]
		self.json_player15 = [["id",3],
						     ["species",
						     	[[["food",2],
								  ["body",2],
								  ["population",2],
								  ["traits",[]]]]],
						     ["bag",0]]
		self.json_player16 = [["id",3],
						     ["species",[]],
						     ["bag",0]]




	def tearDown(self):
		del self.false
		del self.spec1
		del self.spec2
		del self.spec3
		del self.spec4
		del self.spec5
		del self.spec6
		del self.spec7
		del self.spec8
		del self.spec9
		del self.spec10
		del self.spec11
		del self.spec12
		del self.spec13
		del self.spec14
		del self.spec15
		del self.spec16
		del self.spec17
		del self.spec18
		del self.spec19
		del self.spec20
		del self.spec21
		del self.spec22

		del self.player1
		del self.player2
		del self.player3
		del self.player4
		del self.player5
		del self.player6
		del self.player7
		del self.player8
		del self.player9
		del self.player10
		del self.player11
		del self.player12
		del self.player13
		del self.player14
		del self.player15
		del self.player16

		del self.json_spec1
		del self.json_spec2
		del self.json_spec3
		del self.json_spec4
		del self.json_spec5
		del self.json_spec6
		del self.json_spec7
		del self.json_spec8
		del self.json_spec9
		del self.json_spec10
		del self.json_spec11
		del self.json_spec12
		del self.json_spec13
		del self.json_spec14
		del self.json_spec15
		del self.json_spec16
		del self.json_spec17
		del self.json_spec18
		del self.json_spec19
		del self.json_spec20
		del self.json_spec21
		del self.json_spec22

		del self.json_player1
		del self.json_player2
		del self.json_player3
		del self.json_player4
		del self.json_player5
		del self.json_player6
		del self.json_player7
		del self.json_player8
		del self.json_player9
		del self.json_player10
		del self.json_player11
		del self.json_player12
		del self.json_player13
		del self.json_player14
		del self.json_player15
		del self.json_player16



	def test_parseSituation(self):
		self.assertEqualSpecies(self.parse_json.parse_situation([self.json_spec1, self.json_spec2, self.false, self.false]),[self.spec1, self.spec2, False, False])
	def test_parseSituation2(self):
		self.assertEqualSpecies(self.parse_json.parse_situation([self.json_spec3, self.json_spec15, self.json_spec4, self.json_spec22]),[self.spec3, self.spec15, self.spec4, self.spec22])

	
	def assertEqualSpecies(self, jspecies, exspecies):
		"""Tests the fields in two lists of species for equivalency
		"""
		for ex, j in zip(exspecies, jspecies):
			ex_fields = "{}{}{}{}".format(ex.getFood(),ex.getBodySize(), ex.getPopulation(), ex.getTraits())
			json_fields = "{}{}{}{}".format(j.getFood(),j.getBodySize(), j.getPopulation(), j.getTraits())
			if (ex_fields != json_fields):
				return False
		return True

	def test_printMoreShit(self):
		print self.parse_json.parse_player(self.json_player1)

	def assertEqualPlayer(self, jplayer, explayer):
		"""Tests the fields in two players for equivalency
		"""
		same_specs = self.assertEqualSpecies(jplayer.getSpeciesBoards(),explayer.getSpeciesBoards())

		ex_fields = "{}{}".format(explayer.getPlayerId(),explayer.getFoodBag())
		json_fields = "{}{}".format(jplayer.getPlayerId(),jplayer.getFoodBag())
		return (ex_fields == json_fields) and same_specs


	def test_parseTraits(self):
		self.assertEqual(self.parse_json.parse_traits([]), [])
		self.assertEqual(self.parse_json.parse_traits(["carnivore"]), [trait.Trait.carnivore])
		self.assertEqual(self.parse_json.parse_traits(["carnivore", "fat-tissue"]), [trait.Trait.carnivore, trait.Trait.fat_tissue])

	def test_parseLoSpecies(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec1]),[self.spec1])
	def test_parseLoSpecies2(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec2, self.json_spec3]),[self.spec2, self.spec3])
	def test_parseLoSpecies3(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec4]),[self.spec4])
	def test_parseLoSpecies4(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec5]),[self.spec5])
	def test_parseLoSpecies5(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec6, self.json_spec7]),[self.spec6, self.spec7])
	def test_parseLoSpecies6(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec8]),[self.spec8])
	def test_parseLoSpecies7(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec9]),[self.spec9])
	def test_parseLoSpecies8(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec10, self.json_spec11]),[self.spec10, self.spec11])
	def test_parseLoSpecies9(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec12]),[self.spec12])
	def test_parseLoSpecies10(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec13]),[self.spec13])
	def test_parseLoSpecies11(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec14, self.json_spec15]),[self.spec14, self.spec15])
	def test_parseLoSpecies12(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec16]),[self.spec16])
	def test_parseLoSpecies13(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec17]),[self.spec17])
	def test_parseLoSpecies14(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec18, self.json_spec19]),[self.spec18, self.spec19])
	def test_parseLoSpecies15(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec20]),[self.spec20])
	def test_parseLoSpecies16(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec21]),[self.spec21])
	def test_parseLoSpecies17(self):
		self.assertEqualSpecies(self.parse_json.parse_loSpecies([self.json_spec22]),[self.spec22])

	def test_parsePlayer(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player1),self.player1)
	def test_parsePlayer1(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player2),self.player2)
	def test_parsePlayer2(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player3),self.player3)
	def test_parsePlayer3(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player4),self.player4)
	def test_parsePlayer4(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player5),self.player5)
	def test_parsePlayer5(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player6),self.player6)
	def test_parsePlayer6(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player7),self.player7)
	def test_parsePlayer7(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player8),self.player8)
	def test_parsePlayer8(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player9),self.player9)
	def test_parsePlayer9(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player10),self.player10)
	def test_parsePlayer10(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player11),self.player11)
	def test_parsePlayer11(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player12),self.player12)
	def test_parsePlayer12(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player13),self.player13)
	def test_parsePlayer13(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player14),self.player14)
	def test_parsePlayer14(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player15),self.player15)
	def test_parsePlayer15(self):
		self.assertEqualPlayer(self.parse_json.parse_player(self.json_player16),self.player16)

	def test_parseFeeding(self):
		# if time, add more test cases, particularly exceptions

		"""[current_player, free_food, all_players]
		"""
		feeding = [self.json_player1, 10, [self.json_player2, self.json_player3]]
		result = self.parse_json.parse_feeding(feeding)
		self.assertEqualPlayer(result[0], self.player1)
		self.assertEqual(result[1], 10)
		self.assertEqualPlayer(result[2][0], self.player2)
		self.assertEqualPlayer(result[2][1], self.player3)

	def test_parseFeeding2(self):
		feeding = [self.json_player4, 10, [self.json_player5, self.json_player6]]
		result = self.parse_json.parse_feeding(feeding)
		self.assertEqualPlayer(result[0], self.player4)
		self.assertEqual(result[1], 10)
		self.assertEqualPlayer(result[2][0], self.player5)
		self.assertEqualPlayer(result[2][1], self.player6)

	def test_parseFeeding3(self):
		feeding = [self.json_player7, 10, [self.json_player8, self.json_player9]]
		result = self.parse_json.parse_feeding(feeding)
		self.assertEqualPlayer(result[0], self.player7)
		self.assertEqual(result[1], 10)
		self.assertEqualPlayer(result[2][0], self.player8)
		self.assertEqualPlayer(result[2][1], self.player9)

	def test_parseFeeding4(self):
		feeding = [self.json_player10, 10, [self.json_player11, self.json_player12]]
		result = self.parse_json.parse_feeding(feeding)
		self.assertEqualPlayer(result[0], self.player10)
		self.assertEqual(result[1], 10)
		self.assertEqualPlayer(result[2][0], self.player11)
		self.assertEqualPlayer(result[2][1], self.player12)

	def test_parseFeeding5(self):
		feeding = [self.json_player13, 10, [self.json_player14, self.json_player15, self.json_player16]]
		result = self.parse_json.parse_feeding(feeding)
		self.assertEqualPlayer(result[0], self.player13)
		self.assertEqual(result[1], 10)
		self.assertEqualPlayer(result[2][0], self.player14)
		self.assertEqualPlayer(result[2][1], self.player15)
		self.assertEqualPlayer(result[2][2], self.player16)





if __name__ == '__main__':
	unittest.main()