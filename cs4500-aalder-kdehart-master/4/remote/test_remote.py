# Unit tests for the remote proxy wrapper for a Player in 6 Nimmt!

import unittest
import remote
import components
import player
import json

class TestRemote(unittest.TestCase):

  def setUp(self):
    self.remote = remote.RemoteProxyPlayer()
    self.jsonStart = json.dump(["start-round", [[43, 3], [19, 4], [23, 5], [12, 3], [87, 1], [13, 5], [100, 7], [84, 3], [34, 2], [14, 4]]])
    self.jsonTakeTurn = json.dump(["take-turn", [[[74, 2], [99, 3]], [[45, 5]], [[22, 6], [67, 4]], [[102, 2]]]])
    self.jsonChoose = json.dump(["choose", [[[74, 2], [99, 3]], [[45, 5]], [[22, 6], [67, 4]], [[102, 2]]]])
    self.jsonGarbage = json.dump(["blah", [2,3]])
    self.lcard = [[43, 3], [19, 4], [23, 5], [12, 3], [87, 1], [13, 5], [100, 7], [84, 3], [34, 2], [14, 4]]
    self.deck = [[[74, 2], [99, 3]], [[45, 5]], [[22, 6], [67, 4]], [[102, 2]]]

    self.card = components.Card(100).setBullNumber(7)
    self.stack = [[components.Card(102).setBullNumber(2)]]
    self.hand = ([components.Card(43).setBullNumber(3), components.Card(19).setBullNumber(4),
                components.Card(23).setBullNumber(5), components.Card(12).setBullNumber(3),
                components.Card(87).setBullNumber(1), components.Card(13).setBullNumber(5),
                components.Card(100).setBullNumber(7), components.Card(84).setBullNumber(3),
                components.Card(34).setBullNumber(2), components.Card(14).setBullNumber(4)])
    self.deck_of_stacks = ([[components.Card(74).setBullNumber(2), components.Card(99).setBullNumber(3)],
                            [components.Card(45).setBullNumber(5)],
                            [components.Card(22).setBullNumber(6), components.Card(67).setBullNumber(4)],
                            [components.Card(102).setBullNumber(2)]])

  def tearDown(self):
    del self.remote
    del self.jsonStart
    del self.jsonTakeTurn
    del self.jsonChoose
    del self.jsonGarbage
    del self.lcard
    del self.deck
    del self.card
    del self.stack
    del self.hand
    del self.deck_of_stacks

  def testParseLcard(self):
    self.assertEqual(self.remote.parse_lcard(self.lcard), self.hand)

  def testParseDeck(self):
    self.assertEqual(self.remote.parse_deck(self.deck), self.deck_of_stacks)

  def testStartRound(self):
    self.assertEqual(self.remote.start_round(self.lcard), json.dump(True))

  def testTakeTurn(self):
    self.assertEqual(self.remote.take_turn(self.deck), json.dump(self.card))

  def testChoose(self):
    self.assertEqual(self.remote.choose(self.deck), json.dump(self.stack))

if __name__ == '__main__':
    unittest.main()

