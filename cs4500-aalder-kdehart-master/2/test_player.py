# Unit tests for player.py

import unittest
import player
import collections

Card = collections.namedtuple('Card', ['face_value', 'bull_number'])

class TestPlayerMethods(unittest.TestCase):

  def setUp(self):
    self.card1 = Card(38, 2)
    self.card2 = Card(12, 7)
    self.card3 = Card(66, 5)
    self.card_impossible = Card(-2, 200)
    self.not_card = 50

    self.list_of_card = [self.card1, self.card2]
    self.default_player = player.Player(self.list_of_card)

    self.game1 = {'stacks': [self.list_of_card]}
    self.game2 = {}
    self.game3 = {'stacks':[]}
    self.game4 = {'stacks':[[self.card3, self.card3, self.card2], [self.card2, self.card1, self.card1], self.list_of_card ]}
    self.game5 = {'stacks':[self.list_of_card, [self.card3, self.card3, self.card2], [self.card2, self.card1, self.card_impossible]]}
    self.not_game = 250

  def tearDown(self):
    del self.card1
    del self.card2
    del self.card3
    del self.card_impossible
    del self.not_card

    del self.list_of_card
    del self.default_player

    del self.game1
    del self.game2
    del self.game3
    del self.game4
    del self.game5
    del self.not_game

  def test_init_(self):
    self.assertEqual(player.Player([]).cards, [])
    self.assertEqual(player.Player(self.list_of_card).cards, self.list_of_card)
    (self.assertEqual(player.Player(['bread', 76, collections.defaultdict(int)]).cards,
                      ['bread', 76, collections.defaultdict(int)]))

  def test_receive_cards_many(self):
    self.default_player.receive_cards([self.card3, self.card3])
    (self.assertEqual(self.default_player.cards,
                      [self.card1, self.card2, self.card3, self.card3]))

  def test_receive_cards_one(self):
    self.default_player.receive_cards([self.card3])
    print self.default_player.cards
    (self.assertEqual(self.default_player.cards,
                      [self.card1, self.card2, self.card3]))

  def test_receive_cards_nonsense(self):
    self.default_player.receive_cards(['Thank you!'])
    (self.assertEqual(self.default_player.cards,
                      [self.card1, self.card2, 'Thank you!']))

  def test_discard_card(self):
    self.assertEqual(self.default_player.discard_card(self.game1), self.card1)

  def test_discard_card_empty(self):
    self.assertEqual(self.default_player.discard_card(self.game3), self.card1)

  def test_discard_card_nonsense(self):
    self.assertEqual(self.default_player.discard_card(self.not_game), self.card1)

  def test_get_stack_bull_value(self):
    self.assertEqual(self.default_player.get_stack_bull_value([]), 0)
    self.default_player = player.Player(self.list_of_card)
    self.assertEqual(self.default_player.get_stack_bull_value(self.list_of_card), 9)
    with self.assertRaises(AttributeError):
      self.default_player = player.Player(self.list_of_card)
      self.assertEqual(self.default_player.get_stack_bull_value('cheese'), 0)

  def test_pick_stack(self):
    self.assertEqual(self.default_player.pick_stack(self.game4), 2)
    self.assertEqual(self.default_player.pick_stack(self.game5), 0)
    with self.assertRaises(TypeError):
      self.default_player.pick_stack(self.game1)
      self.default_player.pick_stack(self.game2)
      self.default_player.pick_stack(self.game3)
      self.default_player.pick_stack(self.not_game)

if __name__ == '__main__':
    unittest.main()

    
