Purpose: To implement the player for our own interface and design communication protocol for distributed players interacting with the game system.


FILES:
player_protocol.txt is a description of the player-server communication protocol

take5 is the folder containing our implemented interface for 6 Nimmt!

take5/player.py is our implementation our player interface

take5/components.py contains card and stack classes implementation

take5/dealer.py contains the dealer component class implementation

take5/main.py contains the game running component implementation

take5/test_player.py contains tests for player component

take5/test_components.py contains the tests for card and stack methods

take5/test_dealer.py contains tests for dealer component


RUNNING THE CODE:
All test files can be run by entering “python <filename>” on the command line.

For running our implementation of the Nimmt! game, run “python main.py [x]” where x is the number of players between 2-4 on the commandline.
 

READING THE CODE:
Read the code starting at the main.py file in the main function.

The player_protocol.txt file is read by reading the diagram first. The notes refer to the part of the diagram parallel to where they are written. Data definitions, signatures, and examples are at the bottom of the file.

bullpoints.patch patched a bug with the card object not setting bull points correctly.

stackaddcard.patch patched a bug where cards were not being added to stacks correctly. In order to do this we added a way to calculate lengths of a stack and appropriate tests.

variables.patch patched a bug where we had hard coded magic numbers into dealer.py and main.py instead of using variable. We switched these to variables.

shuffle.patch patched a bug where we were not properly shuffling the deck before the round so each game looked identical. 

wronguserinput.patch patched a bug where we were not taking the number of players as command line input and starting the game.

endround.patch patched a bug where the turn method in main was not properly handling players picking stacks correctly as it wasn’t calculating bull points correctly, nor was it ending the game properly.

comments.patch patched a bug where our one line comments were no longer accurate.

testmain.patch patched a bug with our unit tests for main which we discovered were not possible to execute.

reorg.patch is a patch that ensures the files are all in the right location in the directory.

3minbull.patch is a patch that changes the minimum number of bull points possible on a card from 2 to 3.

smallestfirst.patch is a patch that makes the player play the smallest card first. This patch is more than one line due to us patching it off a different patch.

3minbull.patch, handsize.patch, maxcardval.patch, maxstack.patch, and smallestfirst.patch all must be applied after the other patches in order for them to patch properly. 
