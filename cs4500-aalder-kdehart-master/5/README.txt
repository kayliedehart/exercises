PURPOSE:
Design a data representation for the species, implement attackable, and write a test harness for that portion of the Evolution game. Design an interface between the player and the dealer for the game.


FILES:
5/player-interface.txt describes the interface between the player and dealer components

5/xattack is an executable to run the test harness for the attackable function

5/xattack.py is the file we generated the previously mentioned executable from

5/attack/dealer.py is a partially written dealer component holding the attackable method

5/attack/species.py contains the class representing a SpeciesBoard

5/attack/trait.py contains the class representing the enumerated Traits

5/attack/test_dealer.py are unit tests for the dealer's attackable method

5/attack/test_species.py are the unit tests for the species class

NOTE: the trait.py file does not have a test file due to it being exclusively an enumeration


READING/RUNNING THE CODE:
In order for the code to run you must either be using python version 3.4 or backport using the following command on the command line:
  pip install enum34

The executable file xattack is runnable by typing './xattack < expected-input-json > expected-output-json' in the command line from the 5/ directory where expected-input-json and expected-output-json are files containing valid json for testing the attackable method.

All the test classes can be run on the command line by typing 'python <filename>'. Note: all tests in test_dealer.py should be run individually from one another.

To read the attackable method code, start in the dealer and use the other class files for reference as necessary.

For the player-interface.txt file, the document should be read starting from the analysis with reference to the ascii art diagram.
