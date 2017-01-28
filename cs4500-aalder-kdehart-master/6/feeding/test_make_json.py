# unit tests for make_json for Evolution
import trait
import species
import player
import dealer
import json
import unittest
import make_json

class TestMakeJSON(unittest.TestCase):

	def setUp(self):
		self.make_json = make_json.MakeJSON()
		self.false = json.dumps(False)
		self.true = json.dumps(True)
		self.spec1 = species.Species(0,1,1,["carnivore"])
		self.spec2 = species.Species(1,3,3,["herding"])
		self.spec3 = species.Species(1,2,4,["carnivore","ambush"])
		self.spec4 = species.Species(0,3,2,[])

		self.spec5 = species.Species(0,4,2,["carnivore"])
		self.spec6 = species.Species(1,3,3,["herding"])
		self.spec7 = species.Species(1,2,4,["carnivore","ambush"])
		self.spec8 = species.Species(0,1,2,[])

		self.spec9 = species.Species(0,1,1,["symbiosis"])
		self.spec10 = species.Species(0,3,1,["warning-call"])
		self.spec11 = species.Species(2,2,2,[])
		self.spec12 = species.Species(0,1,1,[])

		self.spec13 = species.Species(0,1,1,[])
		self.spec14 = species.Species(0,5,1,["fat-tissue"])
		self.spec15 = species.Species(0,6,1,["warning-call"])
		self.spec16 = species.Species(2,2,2,[])

		self.spec17 = species.Species(0,1,1,[])
		self.spec18 = species.Species(0,1,1,[])
		self.spec19 = species.Species(0,3,2,["carnivore","fat-tissue"])
		self.spec20 = species.Species(3,3,6,[])

		self.spec21 = species.Species(0,5,4,[])
		self.spec22 = species.Species(2,2,2,[])

		self.spec14.setFatFood(5)
		self.spec19.setFatFood(3)


		self.player1 = player.Player(1, [self.spec1], 0)
		self.player2 = player.Player(2, [self.spec2, self.spec3], 0)
		self.player3 = player.Player(3, [self.spec4], 0)

		self.player4 = player.Player(1, [self.spec5], 0)
		self.player5 = player.Player(2, [self.spec6, self.spec7], 0)
		self.player6 = player.Player(3, [self.spec8], 0)

		self.player7 = player.Player(1, [self.spec9], 0)
		self.player8 = player.Player(2, [self.spec10, self.spec11], 0)
		self.player9 = player.Player(3, [self.spec12], 0)

		self.player10 = player.Player(1, [self.spec14, self.spec15], 0)
		self.player11 = player.Player(2, [self.spec16, self.spec13], 0)
		self.player12 = player.Player(3, [self.spec17], 0)

		self.player13 = player.Player(1, [self.spec19], 0)
		self.player14 = player.Player(2, [self.spec20, self.spec21], 0)
		self.player15 = player.Player(3, [self.spec22], 0)

		self.player16 = player.Player(3, [], 0)


		self.json_spec1 = '[["food",0],["body",1],["population",1],["traits",["carnivore"]]]'
		self.json_spec2 = '[["food",1],["body",3],["population",3],["traits",["herding"]]]'
		self.json_spec3 = '[["food",1],["body",2],["population",4],["traits",["carnivore","ambush"]]]'
		self.json_spec4 = '[["food",0],["body",3],["population",2],["traits",[]]]'
		self.json_spec5 = '[["food",0],["body",4],["population",2],["traits",["carnivore"]]]'
		self.json_spec6 = '[["food",1],["body",3],["population",3],["traits",["herding"]]]'
		self.json_spec7 = '[["food",1],["body",2],["population",4],["traits",["carnivore","ambush"]]]'
		self.json_spec8 = '[["food",0],["body",1],["population",2],["traits",[]]]'
		self.json_spec9 = '[["food",0],["body",1],["population",1],["traits",["symbiosis"]]]'
		self.json_spec10 = '[["food",0],["body",3],["population",1],["traits",["warning-call"]]]'
		self.json_spec11 = '[["food",2],["body",2],["population",2],["traits",[]]]'
		self.json_spec12 = '[["food",0],["body",1],["population",1],["traits",[]]]'
		self.json_spec13 = '[["food",0],["body",1],["population",1],["traits",[]]]'
		self.json_spec14 = '[["food",0],["body",5],["population",1],["traits",["fat-tissue"]],["fat-food",5]]'
		self.json_spec15 = '[["food",0],["body",6],["population",1],["traits",["warning-call"]]]'
		self.json_spec16 = '[["food",2],["body",2],["population",2],["traits",[]]]'
		self.json_spec17 = '[["food",0],["body",1],["population",1],["traits",[]]]'
		self.json_spec18 = '[["food",0],["body",1],["population",1],["traits",[]]]'
		self.json_spec19 = '[["food",0],["body",3],["population",2],["traits",["carnivore","fat-tissue"]],["fat-food",3]]'
		self.json_spec20 = '[["food",3],["body",3],["population",6],["traits",[]]]'
		self.json_spec21 = '[["food",0],["body",5],["population",4],["traits",[]]]'
		self.json_spec22 = '[["food",2],["body",2],["population",2],["traits",[]]]'

		self.json_player1 = '[["id",1],["species",[[["food",0],["body",1],["population",1],["traits",["carnivore"]]]]],["bag",0]]'
		self.json_player2 = '[["id",2],["species",[[["food",1],["body",3],["population",3],["traits",["herding"]]],[["food",1],["body",2],["population",4],["traits",["carnivore","ambush"]]]]],["bag",0]]'
		self.json_player3 = '[["id",3],["species",[[["food",0],["body",3],["population",2],["traits",[]]]]],["bag",0]]'
		self.json_player4 = '[["id",1],["species",[[["food",0],["body",4],["population",2],["traits",["carnivore"]]]]],["bag",0]]'
		self.json_player5 = '[["id",2],["species",[[["food",1],["body",3],["population",3],["traits",["herding"]]],[["food",1],["body",2],["population",4],["traits",["carnivore","ambush"]]]]],["bag",0]]'
		self.json_player6 = '[["id",3],["species",[[["food",0],["body",1],["population",2],["traits",[]]]]],["bag",0]]'
		self.json_player7 = '[["id",1],["species",[[["food",0],["body",1],["population",1],["traits",["symbiosis"]]]]],["bag",0]]'
		self.json_player8 = '[["id",2],["species",[[["food",0],["body",3],["population",1],["traits",["warning-call"]]],[["food",2],["body",2],["population",2],["traits",[]]]]],["bag",0]]'
		self.json_player9 = '[["id",3],["species",[[["food",0],["body",1],["population",1],["traits",[]]]]],["bag",0]]'
		self.json_player10 = '[["id",1],["species",[[["food",0],["body",5],["population",1],["traits",["fat-tissue"]],["fat-food",5]],[["food",0],["body",6],["population",1],["traits",["warning-call"]]]]],["bag",0]]'
		self.json_player11 = '[["id",2],["species",[[["food",2],["body",2],["population",2],["traits",[]]],[["food",0],["body",1],["population",1],["traits",[]]]]],["bag",0]]'
		self.json_player12 = '[["id",3],["species",[[["food",0],["body",1],["population",1],["traits",[]]]]],["bag",0]]'
		self.json_player13 = '[["id",1],["species",[[["food",0],["body",3],["population",2],["traits",["carnivore","fat-tissue"]],["fat-food",3]]]],["bag",0]]'
		self.json_player14 = '[["id",2],["species",[[["food",3],["body",3],["population",6],["traits",[]]],[["food",0],["body",5],["population",4],["traits",[]]]]],["bag",0]]'
		self.json_player15 = '[["id",3],["species",[[["food",2],["body",2],["population",2],["traits",[]]]]],["bag",0]]'
		self.json_player16 = '[["id",3],["species",[]],["bag",0]]'


	def tearDown(self):
		del self.false
		del self.true
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


	def test_make_speciesPlus1(self):
		"""Returns a string representing a JSON SpeciesPlus
		"""
		self.assertEqual(self.make_json.make_speciesPlus(self.spec1),self.json_spec1)

	def test_make_speciesPlus2(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec2),self.json_spec2)

	def test_make_speciesPlus3(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec3),self.json_spec3)

	def test_make_speciesPlus4(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec4),self.json_spec4)

	def test_make_speciesPlus5(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec5),self.json_spec5)

	def test_make_speciesPlus6(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec6),self.json_spec6)

	def test_make_speciesPlus7(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec7),self.json_spec7)

	def test_make_speciesPlus8(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec8),self.json_spec8)

	def test_make_speciesPlus9(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec9),self.json_spec9)

	def test_make_speciesPlus10(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec10),self.json_spec10)

	def test_make_speciesPlus11(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec11),self.json_spec11)

	def test_make_speciesPlus12(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec12),self.json_spec12)

	def test_make_speciesPlus13(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec13),self.json_spec13)

	def test_make_speciesPlus14(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec14),self.json_spec14)

	def test_make_speciesPlus15(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec15),self.json_spec15)

	def test_make_speciesPlus16(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec16),self.json_spec16)

	def test_make_speciesPlus17(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec17),self.json_spec17)

	def test_make_speciesPlus18(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec18),self.json_spec18)

	def test_make_speciesPlus19(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec19),self.json_spec19)

	def test_make_speciesPlus20(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec20),self.json_spec20)

	def test_make_speciesPlus21(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec21),self.json_spec21)

	def test_make_speciesPlus22(self):
		self.assertEqual(self.make_json.make_speciesPlus(self.spec22),self.json_spec22)


	def test_make_player1(self):
		"""Returns a string representing a JSON Player
		"""
		self.assertEqual(self.make_json.make_player(self.player1), self.json_player1)

	def test_make_player2(self):
		self.assertEqual(self.make_json.make_player(self.player2), self.json_player2)

	def test_make_player3(self):
		self.assertEqual(self.make_json.make_player(self.player3), self.json_player3)

	def test_make_player4(self):
		self.assertEqual(self.make_json.make_player(self.player4), self.json_player4)

	def test_make_player5(self):
		self.assertEqual(self.make_json.make_player(self.player5), self.json_player5)

	def test_make_player6(self):
		self.assertEqual(self.make_json.make_player(self.player6), self.json_player6)

	def test_make_player7(self):
		self.assertEqual(self.make_json.make_player(self.player7), self.json_player7)

	def test_make_player8(self):
		self.assertEqual(self.make_json.make_player(self.player8), self.json_player8)

	def test_make_player9(self):
		self.assertEqual(self.make_json.make_player(self.player9), self.json_player9)

	def test_make_player10(self):
		self.assertEqual(self.make_json.make_player(self.player10), self.json_player10)

	def test_make_player11(self):
		self.assertEqual(self.make_json.make_player(self.player11), self.json_player11)

	def test_make_player12(self):
		self.assertEqual(self.make_json.make_player(self.player12), self.json_player12)

	def test_make_player13(self):
		self.assertEqual(self.make_json.make_player(self.player13), self.json_player13)

	def test_make_player14(self):
		self.assertEqual(self.make_json.make_player(self.player14), self.json_player14)

	def test_make_player15(self):
		self.assertEqual(self.make_json.make_player(self.player15), self.json_player15)

	def test_make_player16(self):
		self.assertEqual(self.make_json.make_player(self.player16), self.json_player16)

	"""
		For the following tests, you must change the return method in make_meal and make_attack
		to json.dumps(result) rather than json.dump(result, sys.stdout) - since they need to print
		the results out, the return type is None.
	"""

	# def test_make_meal(self):
	# 	self.assertEqual(self.make_json.make_meal(False), self.false)

	# def test_make_meal2(self):
	# 	self.assertEqual(self.make_json.make_meal([self.spec1]), json.dumps(self.json_spec1))

	# def test_make_meal3(self):
	# 	self.assertEqual(self.make_json.make_meal([self.spec14]), json.dumps(self.json_spec14))

	# def test_make_meal4(self):
	# 	self.assertEqual(self.make_json.make_meal([self.spec2, 2]), json.dumps("[" + self.json_spec2 + ",2]"))

	# def test_make_attack(self):
	# 	self.assertEqual(self.make_json.make_attack(False), self.false)
	# 	self.assertEqual(self.make_json.make_attack(True), self.true)


if __name__ == '__main__':
	unittest.main()