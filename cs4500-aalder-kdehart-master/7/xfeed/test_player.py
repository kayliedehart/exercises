# unit tests for the Player in Evolution
import unittest
import dealer
import species
import trait
import strategy
import player

class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.player = player.Player(1, [], 0)

    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.Trait.carnivore])

    self.herbavore = species.Species(0, 1, 1, [])
    self.herbavore2 = species.Species(0, 1, 1, [])

    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setTraits([trait.Trait.fat_tissue])
    self.fat_tissue2 = species.Species(0, 1, 1, [])
    self.fat_tissue2.setBodySize(3)
    self.fat_tissue2.setTraits([trait.Trait.fat_tissue])

    self.opherb = species.Species(0, 1, 1, [])
    self.opfatherb = species.Species(0, 1, 1, [])
    self.opfatherb.setBodySize(7)

    self.opponent1 = player.Player(2, [], 0)
    self.opponent1.setSpeciesBoards([self.opherb, self.opfatherb])
    self.opponents = [self.opponent1]

    self.dealer = dealer.Dealer()
    self.dealer.setListOfPlayers([self.player, self.opponent1])
    self.dealer.setWateringHole(4)

  def tearDown(self):
    del self.player
    del self.carnivore
    del self.herbavore
    del self.fat_tissue
    del self.opherb
    del self.opfatherb
    del self.opponent1
    del self.opponents
    del self.dealer

  # Feed Tests
  def testSimpleHerbavore(self):
    self.player.setSpeciesBoards([self.herbavore, self.herbavore2])
    self.assertEqual(self.player.feed(self.opponents), 0)




  def testSimpleCarnivore(self):
    self.player.setSpeciesBoards([self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), [0, 0, 0])

  def testSimpleFatTissue(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_tissue2])
    self.assertEqual(self.player.feed(self.opponents), [1, 4])




  def testSimpleEmpty(self):
    self.assertEqual(self.player.feed(self.opponents), False)

  def testSimpleFull(self):
    self.carnivore.setFood(1)
    self.herbavore.setFood(1)
    self.player.setSpeciesBoards([self.herbavore, self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), False)



  def testImpossibleCarnivoreAttack(self):
    self.player.setSpeciesBoards([self.carnivore])
    self.opponent1.setSpeciesBoards([self.opfatherb])
    self.assertEqual(self.player.feed(self.opponents), False)




  def testSequencingConstraintOneHungry(self):
    self.player.setSpeciesBoards([self.herbavore])
    with self.assertRaises(Exception) as context:
      self.player.feed(self.opponents)
      self.assertTrue('Violation of Sequencing Constraints' in context.exception)

  def testSequencingConstraintNotEnoughFood(self):
    self.dealer.setWateringHole(0)
    self.player.setSpeciesBoards([self.herbavore])
    with self.assertRaises(Exception) as context:
      self.player.feed(self.opponents)
      self.assertTrue('Violation of Sequencing Constraints' in context.exception)


  # Getter and Setter Tests
  def testGetSetSpeciesBoards(self):
    self.player.setSpeciesBoards(self.herbavore)
    self.assertEqual(self.player.getSpeciesBoards(), self.herbavore)

  def testGetSetAddFoodBag(self):
    self.player.setFoodBag(4)
    self.player.addToFoodBag(1)
    self.assertEqual(self.player.getFoodBag(), 5)

  def testGetSetPlayerID(self):
    self.player.setPlayerId(2)
    self.assertEqual(self.player.getPlayerId(), 2)

if __name__ == '__main__':
    unittest.main()