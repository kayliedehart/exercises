import unittest

import constants_player_test as c
from take5.stack import Stack

class TestPlayer(unittest.TestCase):

    def test_discard1(self):
        c.player1.discard()
        self.assertEqual(c.player1.selected, 2)

    def test_discard2(self):
        c.player2.discard()
        self.assertEqual(c.player2.selected, 1)

    def test_discard3(self):
        c.player3.discard()
        self.assertEqual(c.player3.selected, 0)

    def test_sum_stacks(self):
        self.assertEqual(c.player7.sum_stacks(), [11, 19, 17, 18])
        self.assertEqual(c.player6.sum_stacks(), [11, 19, 17, 18])
        self.assertEqual(c.player5.sum_stacks(), [11, 19, 17, 18])

    def test_add_card(self):
        c.player1.add_card(c.stack5, c.card1)
        self.assert_(c.stack5 == Stack([c.card1,
                                        c.card2,
                                        c.card3,
                                        c.card5,
                                        c.card1]))

    def test_get_index_of_closest_stack(self):
        index = c.player4.get_index_of_closest_stack(c.hand2, c.card1)
        self.assertEqual(index, 0)
        cards = [c.card1, c.card2, c.card3, c.card5]
        index1 = c.player4.get_index_of_closest_stack(cards, c.card6)
        self.assertEqual(index1, 3)

    def test_pick_smallest_stack(self):
        stack = c.player4.pick_smallest_stack()
        self.assert_(stack == c.stack1)

    def test_replace_card(self):
        c.player4.replace_card(c.stack6, c.card6)
        self.assert_(c.stack6 == Stack([c.card6]))

    def test_accumulate_sum(self):
        c.player4.accumulate_sum(c.stack8)
        self.assertEqual(c.player4.bull_points, 7)

    def test_play1(self):
        c.player8.play()
        self.assertEqual(c.player8.hand, [c.card1,
                                          c.card2,
                                          c.card3,
                                          c.card4,
                                          c.card5])
        self.assert_(c.player8.current_stacks == [c.stack5,
                                                  c.stack6,
                                                  Stack([c.card1,
                                                         c.card2,
                                                         c.card3,
                                                         c.card4,
                                                         c.card6]),
                                                  c.stack8])
        self.assertEqual(c.player8.bull_points, 0)

    def test_play3(self):
        c.player10.play()
        self.assertEqual(c.player10.hand, [c.card1, c.card2])
        self.assert_(c.stack14 == Stack([c.card6]))
        self.assertEqual(c.player10.bull_points, 25)

    def test_play4(self):
        c.player11.play()
        self.assertEqual(c.player11.hand, [])
        self.assert_(c.stack17, Stack([c.card1]))
        self.assertEqual(c.player11.bull_points, 3)

    def test_play5(self):
         c.player12.play()
         self.assertEqual(c.player12.hand, [])
         self.assert_(c.stack21 == Stack([c.card2]))
         self.assertEqual(c.player12.bull_points, 10)



if __name__ == '__main__':
    unittest.main()