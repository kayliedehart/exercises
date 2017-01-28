PURPOSE:
Redesign and re-test feed method according to API change to return the appropriate indexes instead of Player and Species instances. Implement and test an interactive streaming JSON echo program.
FILES:

7/Streaming/xstream.py is an interactive command-line JSON echo program.

7/Streaming/test_xstream.py is unit tests for the validation methods in xstream.py

7/xfeed/dealer.py is a copy of the dealer.py previously implemented

7/xfeed/make_json.py is a revised version of the JSON creator for xattack and xfeed

7/xfeed/parse_json.py is a copy of the JSON parser previously implemented

7/xfeed/player.py is the revised player.py now matching the API changes

7/xfeed/species.py is a copy of species.py previously implemented

7/xfeed/strategy.py is a copy of the basic player strategy previously implemented

7/xfeed/test_attackable.py is a copy of the unit tests for species.attackable()

7/xfeed/test_xfeed.py is the revised unit tests for xfeed.py

7/xfeed/test_parse_json.py is a copy of the unit tests for JSON parsing previously implemented

7/xfeed/test_player.py is a revised version of the unit tests for player.py with the new feed signature

7/xfeed/test_species.py is a copy of the previously implemented unit tests for species

7/xfeed/test_strategy.py is a copy of the previously implemented unit tests for strategy.py

7/xfeed/test_xattack.py is a revised version of the unit tests for xattack.py

7/xfeed/trait.py is a copy of the previously implemented trait.py

7/xfeed/xattack.py is a revised copy of the previous implementation of xattack.py

7/xfeed/xfeed.py is a revised copy of the previous implementation of xfeed.py

7/xfeed/xfeed is an executable for the feed method test harness

7/xfeed/xattack is an executable for the attack method test harness

7/xfeed/compile is an executable that compiles the Evolution files



READING/RUNNING THE CODE:
In order for the code to run you must run ./compile in the 7 directory

To run the test harness for the feed method, run ./xfeed from the xfeed directory

To run the test harness for the attack method, run ./xattack from the xfeed directory

To run the JSON echo program, run ./xstream from the Streaming directory

All the unit test files (named test_) can be run in a virtualenv first running 'pip install enum34' and then 'python <filename>'

	To run the unit tests of xfeed, xattack, and xstream, you must COMMENT OUT the 
	calls to main() in the __init__ methods and UNCOMMENT "pass". To run the executables themselves, you must change this back. 

To read the feed method code, start in player.py file in the feed method and read into the other files as necessary.

