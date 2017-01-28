class Player:
    """
    To represent a player in the game
    """
    def __init__(self,
                 name,
                 bull_points,
                 hand=None,
                 current_stacks=None,
                 selected=None):
        """
        :param hand: [Card]
        :param bull_points: Int
        :param current_stacks: [Stack] and len(current_stacks) = 4
        :param selected: Int
        :return: Player
        """
        self.name = name
        self.hand = hand
        self.current_stacks = current_stacks
        self.selected = selected
        self.bull_points = bull_points

    def discard(self):
        """
        Update this player's selected card index
        :return: None
        """
        face_values = map(lambda card: card.number, self.hand)
        self.selected = face_values.index(max(face_values))

    def play(self):
        """
        plays the game for one turn
        :return: None
        """
        stacks = self.current_stacks
        cards_top_stacks = map(lambda stack: stack.cards[-1], stacks)
        self.discard()
        discarded_card = self.hand.pop(self.selected)

        if discarded_card.number < min(map(lambda card: card.number,
                                             cards_top_stacks)):
            smallest_stack = self.pick_smallest_stack()
            self.accumulate_sum(smallest_stack)
            self.replace_card(smallest_stack, discarded_card)

        else:
            index = self.get_index_of_closest_stack(cards_top_stacks,
                                                    discarded_card)
            my_stack = stacks[index]
            if len(my_stack.cards) == 5:
                self.accumulate_sum(my_stack)
                self.replace_card(my_stack, discarded_card)
            else:
                self.add_card(my_stack, discarded_card)

    def accumulate_sum(self, stack):
        """
        Adds stack bull points to the player
        :param stack: Stack
        :return None
        """
        bull_points = sum(map(lambda card: card.bull, stack.cards))
        self.bull_points += bull_points

    def replace_card(self, stack, card):
        """
        Replaces stack with card
        :param stack: Stack
        """
        stack.cards = [card]

    def sum_stacks(self):
        """
        Sum of the bull points the list of stacks
        :return: [Int, ...]
        """
        sums = []
        stacks = self.current_stacks
        for stack in stacks:
            bull_points = map(lambda card: card.bull, stack.cards)
            sums.append(sum(bull_points))
        return sums

    def get_index_of_closest_stack(self, cards, card):
        """
        gets index of stack closest to card in value
        :param cards: [Card, ...]
        :return: Int
        """
        diffs = []
        for c in cards:
            diff = abs(card.number - c.number)
            diffs.append(diff)
        return diffs.index(min(diffs))

    def add_card(self, stack, card):
        """
        adds card on top of stack
        :param card: Card
        :param stack: Stack
        :return:
        """
        stack.cards.append(card)

    def pick_smallest_stack(self):
        """
        Picks the stack with the smallest value
        :return: Stack
        """
        sums = self.sum_stacks()
        return self.current_stacks[sums.index(min(sums))]

    def __str__(self):
        return "name: %s, points: %s, hand: %s, stacks: %s, selected: %s"\
               %(self.name,
                 self.bull_points,
                 [str(card) for card in self.hand],
                 self.current_stacks,
                 self.selected)