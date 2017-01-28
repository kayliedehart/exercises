# Unit tests for initial Player Strategy in Evolution
import unittest
import dealer
import species
import trait
import strategy
import player

class TestStrategy(unittest.TestCase):
  def setUp(self):
    self.player = player.Player(1, [], 0)
    self.strat = strategy.Strategy()

    self.carnivore = species.Species(0, 1, 1, [])
    self.carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore = species.Species(0, 1, 1, [])
    self.fat_carnivore.setTraits([trait.Trait.carnivore])
    self.fat_carnivore.setBodySize(5)

    self.herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore = species.Species(0, 1, 1, [])
    self.fat_herbavore.setBodySize(4)

    self.fat_tissue = species.Species(0, 1, 1, [])
    self.fat_tissue.setBodySize(3)
    self.fat_tissue.setTraits([trait.Trait.fat_tissue])
    self.fat_fat_tissue = species.Species(0, 1, 1, [])
    self.fat_fat_tissue.setBodySize(6)
    self.fat_fat_tissue.setTraits([trait.Trait.fat_tissue])

    self.opherb = species.Species(0, 1, 1, [])
    self.opfatherb = species.Species(0, 1, 1, [])
    self.opfatherb.setBodySize(4)

    self.opponent1 = player.Player(1, [], 0)
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

  def testFatTissueFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_tissue, 4))

  def testBiggestFatTissueFirst(self):
    self.player.setSpeciesBoards([self.fat_tissue, self.fat_fat_tissue])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_fat_tissue, 7))

  def testHerbBeforeCarni(self):
    self.player.setSpeciesBoards([self.herbavore, self.carnivore])
    self.assertEqual(self.player.feed(self.opponents), (self.herbavore))

  def testLargestHerbFirst(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_herbavore])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_herbavore))

  def testLargestCarnivoreFirstIfAllHerbFed(self):
    self.herbavore.setFood(1)
    self.player.setSpeciesBoards([self.herbavore, self.carnivore, self.fat_carnivore])
    self.assertEqual(self.player.feed(self.opponents), (self.fat_carnivore, self.opponent1, self.opfatherb))

  def testWontAttackSelf(self):
    self.player.setSpeciesBoards([self.fat_carnivore])
    self.opponents = []
    self.assertEqual(self.player.feed(self.opponents), False)

  #Unit Test Helper Methods
  def testSortByLexPop(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(3)
    loa = [self.herbavore, self.carnivore]
    self.assertEqual(self.strat.sortByLex(loa), [self.carnivore, self.herbavore])

  def testSortByLexFood(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(1)
    self.herbavore.setFood(1)
    self.carnivore.setFood(3)
    loa = [self.carnivore, self.herbavore]
    self.assertEqual(self.strat.sortByLex(loa), [self.carnivore, self.herbavore])

  def testSortByLexBodySize(self):
    self.herbavore.setPopulation(1)
    self.carnivore.setPopulation(1)
    self.herbavore.setFood(1)
    self.carnivore.setFood(1)
    self.herbavore.setBodySize(1)
    self.carnivore.setBodySize(3)
    loa = [self.carnivore, self.herbavore]
    self.assertEqual(self.strat.sortByLex(loa), [self.carnivore, self.herbavore])

  def testSortByLex(self):
    self.herbavore.setPopulation(1)
    self.herbavore.setFood(1)
    self.herbavore.setBodySize(3)

    self.carnivore.setPopulation(2)
    self.carnivore.setFood(1)
    self.carnivore.setBodySize(2)

    self.fat_tissue.setPopulation(1)
    self.fat_tissue.setFood(2)
    self.fat_tissue.setBodySize(3)

    loa = [self.herbavore, self.carnivore, self.fat_tissue]
    self.assertEqual(self.strat.sortByLex(loa), [self.carnivore, self.fat_tissue, self.herbavore])

  def testStereotypeAnimals(self):
    loa = [self.fat_herbavore, self.herbavore, self.fat_carnivore, self.fat_tissue]
    expectedOutput = ([self.fat_tissue], [self.fat_carnivore], [self.fat_herbavore, self.herbavore])
    self.assertEqual(self.strat.stereotypeAnimals(loa), expectedOutput)

  def testFindFattestIfFatTissue(self):
    fat = [self.fat_tissue]
    carni = [self.fat_carnivore]
    herb = [self.fat_herbavore, self.herbavore]
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_tissue, trait.Trait.fat_tissue))

  def testFindFattestIfHerbi(self):
    fat = []
    carni = [self.fat_carnivore]
    herb = [self.fat_herbavore, self.herbavore]
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_herbavore, False))

  def testFindFattestIfCarni(self):
    fat = []
    carni = [self.fat_carnivore]
    herb = []
    self.assertEqual(self.strat.findFattest(fat, carni, herb), (self.fat_carnivore, trait.Trait.carnivore))

  def testFeedNext(self):
    loa = [self.fat_herbavore, self.herbavore, self.fat_carnivore, self.fat_tissue]
    self.assertEqual(self.strat.feedNext(loa), (self.fat_tissue, trait.Trait.fat_tissue))

  def testCompileSpecies(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.strat.compileSpecies([self.player, self.opponent1]), [(self.herbavore, self.player), (self.fat_tissue, self.player), (self.opherb, self.opponent1), (self.opfatherb, self.opponent1)])

  def testSortOpponentsSpecies(self):
    inpt = [(self.herbavore, self.player), (self.fat_tissue, self.player), (self.opherb, self.opponent1), (self.opfatherb, self.opponent1)]
    output = [(self.opfatherb, self.opponent1), (self.fat_tissue, self.player), (self.herbavore, self.player), (self.opherb, self.opponent1)]
    self.assertEqual(self.strat.sortOpponentsSpecies(inpt), output)

  def testGetNeighborsNoLeft(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.strat.getNeighbors(self.player, self.fat_tissue), (self.herbavore, False))

  def testGetNeighborsNoRight(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.strat.getNeighbors(self.player, self.herbavore), (False, self.fat_tissue))

  def pickVictim(self):
    self.player.setSpeciesBoards([self.herbavore, self.fat_tissue])
    self.assertEqual(self.strat.pickVictim(self.carnivore, [self.player, self.opponent1]), (self.player, self.herbavore))

if __name__ == '__main__':
    unittest.main()