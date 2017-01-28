# Implements a Player in a game of 6 Nimmt! according to provided interface

class Player:
  cards = []

  def __init__(self,cards):
    self.cards=cards

  def receive_cards(self,cards):
    self.cards.extend(cards)

  def discard_card(self, game_state):
    chosen = self.cards[0]
    for card in self.cards:
      if(chosen.face_value<card.face_value):
        chosen=card

    self.cards.remove(chosen)
    return chosen

  def get_stack_bull_value(self, stack):
    stack_value = 0

    for card in stack:
      stack_value += card.bull_number

    return stack_value

  def pick_stack(self, game_state):
    try:
      smallest_stack = game_state["stacks"][0]
      smallest_value = self.get_stack_bull_value(game_state["stacks"][0])

      for stack in game_state["stacks"][1:]:
          stack_value = self.get_stack_bull_value(stack)

          if(stack_value<smallest_value):
            smallest_value = stack_value
            smallest_stack = stack
    except:
      raise TypeError("Not given a proper Game State.")

    return game_state["stacks"].index(smallest_stack)
