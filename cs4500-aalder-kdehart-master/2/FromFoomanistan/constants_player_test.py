from player import Player
from card import Card
from take5.stack import Stack

card1 = Card(1, 2)
card2 = Card(2, 3)
card3 = Card(3, 4)
card4 = Card(6, 6)
card5 = Card(4, 7)
card6 = Card(10, 5)

hand1 = [card1, card2, card3]
hand2 = [card1, card3, card2]
hand3 = [card3, card1, card2]
hand4 = [card1, card2, card3, card4, card5, card6]
hand6 = [card1, card2, card6]
hand7 = [card1]
hand8 = [card2]

stack1 = Stack([card1, card2, card3, card1])
stack2 = Stack([card6, card5, card3, card2])
stack3 = Stack([card1, card2, card5, card6])
stack4 = Stack([card5, card2, card3, card3])

stack5 = Stack([card1, card2, card3, card5])
stack6 = Stack([card1, card2])
stack7 = Stack([card1, card2, card3, card4])
stack8 = Stack([card2, card3])

stack13 = Stack([card1, card2, card3, card1, card2])
stack14 = Stack([card6, card5, card3, card2, card4])
stack15 = Stack([card1, card2, card5, card6, card5])
stack16 = Stack([card5, card2, card3, card3, card1])

stack17 = Stack([card2])
stack18 = Stack([card6])
stack19 = Stack([card3])
stack20 = Stack([card5])

stack21 = Stack([card1, card1, card1, card1, card1])
stack22 = Stack([card5, card5])
stack23 = Stack([card3, card5])
stack24 = Stack([card5, card6])

stacks = [stack1, stack2, stack3, stack4]
stacks2 = [stack5, stack6, stack7, stack8]
stacks3 = [stack13, stack14, stack15, stack16]
stacks4 = [stack17, stack18, stack19, stack20]
stacks5 = [stack21, stack22, stack23, stack24]

player1 = Player(1, 0, hand1)
player2 = Player(2, 0, hand2)
player3 = Player(3, 0, hand3)
player4 = Player(4, 0, hand3, stacks, 0)
player5 = Player(5, 0, hand2, stacks)
player6 = Player(6, 0, hand1, stacks)
player7 = Player(7, 0, hand1, stacks)
player8 = Player(8, 0, hand4, stacks2, 0)
player10 = Player(10, 0, hand6, stacks3, 0)
player11 = Player(11, 0, hand7, stacks4, 0)
player12 = Player(12, 0, hand8, stacks5, 0)
