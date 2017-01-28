PURPOSE:
Design and implement feed method for player including strategy, and write test harness for feed portion of evolution game. Write memo on appropriate uses of implemented method.

FILES:

6/feeding contains code for feed implementation

6/feeding/dealer.py is partially written dealer component for attackable project 5

6/feeding/make_json.py is a JSON encoder used by the test harnesses (xfeed.py and xattack.py)

6/feeding/parse_json.py is a JSON decoder used by the test harnesses (xfeed.py and xattack.py)

6/feeding/player.py is partially written player component holding the feed method

6/feeding/species.py is the class representing a SpeciesBoard (contains attackable method)

6/feeding/strategy.py is the class containing player strategy for feed

6/feeding/test_attackable.py are the unit tests for the attackable method from project 5

6/feeding/test_make_json.py are the unit tests for make_json

6/feeding/test_parse_json.py are the unit tests for parse_json

6/feeding/test_player.py are the unit tests for the player component (including feed)

6/feeding/test_species.py are the unit tests for the species file

6/feeding/test_strategy.py are the unit tests for the strategy file

6/feeding/trait.py is the class containing the enumerated Traits

Note: the trait.py file does not have a unit test file due to it being exclusively an enumeration

6/compile is an executable that will compile xfeed.py and necessary dependencies

6/feed.pdf is a memo describing how the feed method is used by the dealer and how to interpret the
 results

6/feed_in1.json is a JSON input to unit test ./xfeed

6/feed_in2.json is a JSON input to unit test ./xfeed

6/feed_in3.json is a JSON input to unit test ./xfeed

6/feed_in4.json is a JSON input to unit test ./xfeed

6/feed_in5.json is a JSON input to unit test ./xfeed

6/feed_out1.json is the expected JSON output when running 6/feed_in1.json through ./xfeed

6/feed_out2.json is the expected JSON output when running 6/feed_in2.json through ./xfeed

6/feed_out3.json is the expected JSON output when running 6/feed_in3.json through ./xfeed

6/feed_out4.json is the expected JSON output when running 6/feed_in4.json through ./xfeed

6/feed_out5.json is the expected JSON output when running 6/feed_in5.json through ./xfeed

6/xfeed.py is a test harness for testing the player's feed method

6/xfeed is an executable for the test harness 6/xfeed.py

READING/RUNNING THE CODE:
In order for the code to run you must run ./compile in the 6 directory

To run the test harness for the feed method, run ./xfeed

All the unit test files (named test_) can be run in a virtualenv first running 'pip install enum34' and then 'python <filename>'

To read the feed method code, start in player.py file in the feed method and read into the other files as necessary.

