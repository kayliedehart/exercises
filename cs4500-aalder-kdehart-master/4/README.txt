PURPOSE: Implement and test a remote access player protocol for 6 Nimmt! Create data representation diagram and analysis document for Evolution game.


FILES:
/evolution/EvolutionDataRep.pdf is a UML diagram and analysis of the requirements analysis.

/remote/remote.py is a remote proxy wrapper for previously implemented player

/remote/test_remote.py is unit tests for non-socket methods in remote proxy wrapper

/remote/remote is a symlink to remote.py

/remote/components.py is a symlink to components.py in previous implementation

/remote/player.py is a symlink to player.py in previous implementation

/tests/1-in.json is test JSON for remote in case of choose protocol timing violation

/tests/1-out.json is the expected output for 1-in.json

/tests/2-in.json is test JSON for remote in case of start-round protocol timing violation

/tests/2-out.json is the expected output for 2-in.json

/tests/3-in.json is test JSON for remote in case of take-turn protocol violation

/tests/3-out.json is the expected output for 3-in.json

/tests/4-in.json is test JSON for remote in case of choose protocol violation

/tests/4-out.json is the expected output for 4-in.json

/tests/5-in.json is test JSON for remote in case of start-round protocol violation

/tests/5-out.json is the expected output for 5-in.json


READING THE CODE:

For remote, start in remote.py in the main method.

For tests, read the -in files and -out files staggered with eachother according to numbers.

For evolution, read the analysis first and then the UML diagram.

Note: we made a bugfix to components.py to create single point of control for min and max bull point numbers