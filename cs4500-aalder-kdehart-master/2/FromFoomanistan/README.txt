NOTE: player and card files had to be copied in the sub-directory because
we could not make imports from package "2" as it is not a valid package name
(since it's a number)

The purpose of this project is to implement the player as specified by
the given specifications and implement the rest of the system based on our 
specification

README.txt: 
 understand how the program works and is read and the pupose of the files 
 making the program 

card.py: 
represent a card in a game

stack.py: 
represent a stack in a game  

player.py: 
represent a player in a game and state the functionality of a player 

dealer.py:
represent a dealer in a game and state the functionality of a dealer 

main.py: 
run the game using the numerical input as the number of players

changes.txt: 
document the changes we made to our interface 

player.txt: 
document the ambiguities and underspecification in the given interface

constants_dealer_test.py: 
the constants that are used in the dealer tests 

costants_player_test.py: 
the constants that are used in the player tests 

Test_dealer.py: 
test that the functions in dealer.py are working as expected 

Test_player.py: 
test that the functions in player.py are working as expected

Test_stack.py: 
test that the functions in stack.py are working as expected 

To run the game: 
  1) python main.py 
  2) in the command line input the number of player 
 then the game will be simulated and the results of the players will be shown


Start reading from the entry point of the program (main.py)
to understand how the game is run from a high level 
then read simulate_game and simulate round in dealer.py to understand how the game is played 
then read the other files to understand the specifics 
 



