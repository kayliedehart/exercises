import trait
import species
import player

class Strategy:
  def __init__(self):
    pass

  def sortByLex(self, loa):
    """
      Sorts the given list of species boards by the population, then food eaten, then body size from largest to smallest
      Given: a list of species boards
      Returns: a sorted list of species boards the same length as the list provided
    """
    sloa = []
    if(len(loa) == 0):
      return loa
    sloa.append(loa[0])

    if(len(loa) > 1):
      for animal in loa:
        for board in sloa:
          if (loa.index(animal) == 0):
            break
          elif (animal.getPopulation() > board.getPopulation()):
            sloa.insert(sloa.index(board), animal)
            break
          elif ((animal.getPopulation() == board.getPopulation())
            and (animal.getFood() > board.getFood())):
            sloa.insert(sloa.index(board), animal)
            break
          elif ((animal.getPopulation() == board.getPopulation())
            and (animal.getFood() == board.getFood())
            and (animal.getBodySize() > board.getBodySize())):
            sloa.insert(sloa.index(board), animal)
            break
          elif (sloa.index(board) == (len(sloa)-1) ):
            sloa.append(animal)
            break

    return sloa

  def stereotypeAnimals(self, lob):
    """
      sorts hungry animals into the right catagory (fat_species, carnivore, herbivore)
      Given: a list of species
      Returns: 3 lists of species of hungery animals the first of which contains only fat_tissue species, the second of which
        contains only carnivore species, and the third of which containing all animals not fitting into the prior two catagories
    """
    fat_species = []
    carnivores = []
    herbivores = []

    for animal in lob:
      if (animal.hasFatTissue() and (not animal.isCarnivore())):
        fat_species.append(animal)
      if (animal.getFood() < animal.getPopulation()):
        if (animal.isCarnivore()):
          carnivores.append(animal)
        else:
          herbivores.append(animal)
    return (fat_species, carnivores, herbivores)

  def findFattest(self, fat_species, carnivores, herbivores):
    """
      Finds the fattest type of the most prioritized animal that is still hungry
      Given: 3 lists of species, one of which only contains fat_tissue species, one of which only contains carnivore species,
      and one of which contains all non carnivore non fat_tissue species (in that order)
      Returns: A tuple of the fatest species of the most prioritized species (fat_tissue -> herbivore -> carnivore) and one of Trait.fat_tissue, Trait.carnivore, False
      corresponding to the trait that species posesses.
    """
    if fat_species:
      return (fat_species[0], trait.Trait.fat_tissue)
    elif herbivores:
      return (herbivores[0], False)
    elif carnivores:
      return (carnivores[0], trait.Trait.carnivore)
    else:
      raise Exception("Violation of Sequencing Constraints")

  def feedNext(self, lob):
    """
      Determines the next species that needs to be fed
      Given: a list of species
      Returns: A tuple of the fattest hungry species of the most prioritized species (fat_tissue -> herbivore -> carnivore) and one of Trait.fat_tissue, Trait.carnivore, False
      corresponding to the trait that species posesses.
    """
    fat_species = []
    carnivores = []
    herbivores = []

    sortedSpeciesBoards = self.sortByLex(lob)
    fat_species, carnivores, herbivores = self.stereotypeAnimals(sortedSpeciesBoards)
    return self.findFattest(fat_species, carnivores, herbivores)

  def compileSpecies(self, lop):
    """
      Compiles all the species boards from the list of players provided
      Given: a list of players
      Returns: a list of all the species the players have
    """
    boards = []
    for player in lop:
      for board in player.getSpeciesBoards():
        boards.append((board, player))
    return boards

  def sortOpponentsSpecies(self, lobap):
    """
      Sorts the opponents species in order of fattest to skinniest
      Given: a list of tuples of species and the players that contain that species
      Returns: a list of tuples ordered by species body size (large -> small) that contain a player and a species that player owns
    """
    return sorted(lobap, key=lambda board_player: board_player[0].getBodySize(), reverse = True)


  def getNeighbors(self, play, board):
    """
      Finds the neighbors of the given species
      Given: a player and a species belonging to that player
      Returns: a tuple of the left then right neighbors to the given board in the given player
    """
    boards = play.getSpeciesBoards()
    for species in boards:
      if species is board:
        index = boards.index(species)
        left = False
        right = False
        if index != 0:
          left = play.getSpeciesBoards()[index-1]
        if index != (len(boards) - 1):
          right = play.getSpeciesBoards()[index+1]
        return (left, right)
    raise Exception("Invalid Input")

  def pickVictim(self, chosen, lop):
    """
    picks a victim for the given carnivore from the list of players' species
    Given: a hungry carnivore, a list of players
    Returns: a species belonging to one of the players in the list of players that the carnivore
      can eat, and the player the species belongs to or False
    """
    #compile lists of all species
    boardsAndPlayers = self.compileSpecies(lop)


    #sort it in order of size.
    boardsAndPlayers = self.sortOpponentsSpecies(boardsAndPlayers)
    #go down the list until it finds something it can eat
    for playerSpecies in boardsAndPlayers:
      board, play = playerSpecies
      left, right = self.getNeighbors(play, board)
      situation = [board, chosen, left, right]
      if board.attackable(situation):
        return play, board

    #if it cant eat anything return false
    return False