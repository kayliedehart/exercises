import trait
import species
import strategy

class Player:
  species_boards = []
  food_bag = 0
  hand = []
  player_id = 0
  strat = None

  def __init__(self, ident, loSpeciesBoard, bag):
    self.species_boards = loSpeciesBoard
    self.food_bag = bag
    self.hand = []
    self.player_id = ident
    self.strat = strategy.Strategy()

  def setSpeciesBoards(self, loSpeciesBoard):
    self.species_boards = loSpeciesBoard

  def getSpeciesBoards(self):
    return self.species_boards

  def setFoodBag(self, fb):
    self.food_bag = fb

  def getFoodBag(self):
    return self.food_bag

  def addToFoodBag(self, tokens):
    self.food_bag += tokens

  def setHand(self, cards):
    self.hand = cards

  def getHand(self):
    return self.hand

  def addToHand(self, cards):
    self.hand.extend(cards)

  def setPlayerId(self, ident):
    self.player_id = ident

  def getPlayerId(self):
    return self.player_id

  def canFeed(self):
    """
      Checks if the call to feed follows the sequencing constraints
      throws an error if it doesn't match specs
      Returns: A boolean regarding if this player can feed a species or not
      NOTE: WE are not supposed to be doing sequencing checks here
      We have commented out all the sequence checking code
    """
    #checks if there are not enough species boards
    # if ((len(self.species_boards) != 0)
    #   or (not ((len(self.species_boards) == 1)
    #     and (self.species_boards[0].isCarnivore())))):

    #checks if there are an appropraite number of hungry animals
    numHungry = 0
    hungryCarnivore = False
    for animal in self.species_boards:
      if animal.getPopulation() > animal.getFood():
        numHungry += 1
        if(animal.isCarnivore()):
          hungryCarnivore = True
      elif ((animal.isCarnivore() and animal.hasFatTissue())
        and ((animal.getPopulation() + animal.getBodySize()) > animal.getFood())):
        numHungry += 1
        hungryCarnivore = True
      elif (animal.hasFatTissue() and ((animal.getPopulation() + animal.getBodySize()) > (animal.getFood() + animal.getFatFood()))):
        numHungry += 1

    # if (numHungry == 1) and (not hungryCarnivore):
    #   raise Exception("Violation of Sequencing Constraints")
    if numHungry == 0:
      return False
    else:
      return True
    # else:
    #   raise Exception("Violation of Sequencing Constraints")

  def feed(self, lop, watering):
    """
    Determines which species the player is going to feed
    Given: a list of players not containing this player
    Returns: one of
      -False (if a player can't feed any species)
      -the index of a species in self.species_boards,
      -[the index of a species in self.species_boards with the trait fat_tissue, Nat]
      -[the index of a species in self.species_boards with the trait carnivore,
          the index of the player in the given list of players,
          and the index of an attackable species owned by the prior player]
    """
    if (not self.canFeed()):
      return False
    chosen, trait = self.strat.feedNext(self.species_boards)

    ichosen = self.species_boards.index(chosen)

    if (not trait):
      return ichosen
    elif (trait.carnivore is trait):
      victim = self.strat.pickVictim(chosen, lop)
      if (not victim):
        return False
      else:
        play, board = victim
        iplay = lop.index(play)
        iboard = play.getSpeciesBoards().index(board)
        return [ichosen, iplay, iboard]
    else:
      return [ichosen, min(watering, (chosen.getBodySize() - chosen.getFatFood()))]


