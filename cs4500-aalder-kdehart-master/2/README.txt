Purpose: to implement the provided player interface and our own game interface

FILES:
player.py is our implementation of the given player interface.

test_player.py is the tests for the player interface implementation.

take5 is the folder containing our implemented interface for the rest of the game.

take5/components.py contains the card and stack classes implementation.

take5/tests_components.py contains the tests for the card and stack methods

take5/dealer.py contains the dealer component class implementation

take5/tests_dealer.py contains the dealer class tests implementation

take5/main.py contains the game running component implementation

take5/tests_main.py contains the tests for all non dealer or player components


RUNNING THE CODE:
All test files can be run by entering python <filename> on the command line.

The player.py class is designed to be run with the rest of the game program, and will need to be integrated first before running.

For running our implementation of the Nimmt! game, run python main.py on the commandline. 

READING THE CODE:

player.py and test_player.py are read top down for easiest understanding. When implementing the provided interface we made the assumption that we needed to remove the card from the players hand in discard_card() as it wasn’t specified. We also chose to throw an out of bounds exception if the program tries to call pick_stack with a list of stacks with length < 1.

for the files in take5, the code is read starting from the main file, with the dealer being a main component and the components file containing the base object classes. We adjusted our interface to put more computational stress on the main program and less on the dealer. We realized our interface was missing method names and so implemented the program with class names we deemed appropriate. Due to the lack of method names in our provided interface, we expect player component integrations to require additional effort.

for the test files in take5, we purposefully left out tests involving methods involving the player component as we did not write our own player component. This choice was made specifically as we felt there should be a large integration factor to combining these two pieces of code. These tests will be written upon delivery of such component. The current tests cover methods that do not involve the player component.
