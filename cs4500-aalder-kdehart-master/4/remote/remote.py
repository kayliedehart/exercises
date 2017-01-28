#!/usr/bin/env python
# A remote proxy wrapper for a Player in 6 Nimmt!

import socket
import sys
import json
import player
import components

PLAYER_NAME = "Joe"
BUFFERSIZE = 4096
HOST = '127.0.0.1'
PORT = 45678
HANDSIZE = 10
NUMBER_OF_DECKS = 4

class RemoteProxyPlayer:
  player = player.Player(PLAYER_NAME)
  last_received = None
  round_in_progress = False

  def __init__(self):
    self.main()

  def parse_lcard(self, lcard):
    """
    Converts the given LCard into a Stack
    """
    list_of_Cards = []
    for card in lcard:
      new_card = components.Card(card[0])
      new_card.setBullNumber(int(card[1]))
      list_of_Cards.append(new_card)

    return list_of_Cards

  def parse_deck(self, deck):
    """
    Converts a given Deck of LCards into list of Stacks
    """
    list_of_Stacks = []
    for lcard in deck:
      stack = self.parse_lcard(lcard)
      list_of_Stacks.append(stack)

    return list_of_Stacks

  def start_round(self, lcard):
    """
    Receives JSON from the server indicating the start of a round and the
    hand dealt to the Player. Passes these cards to the Player and sends
    back an acknowledgement to the game server
    """
    self.player.setHand(lcard)
    ack = json.dump(True)
    return ack

  def take_turn(self, stacks):
    """
    Receives the current stacks in play from the game server and passes them
    to the Player. Returns the Card the Player has chosen to play this turn.
    """
    players_card = self.player.playCard(stacks)
    players_card = json.dump(players_card)
    return players_card

  def choose(self, stacks):
    """
    Receives a list of Stacks the Player must choose one of to keep. Returns
    the chosen Stack.
    """
    stack_to_keep = self.player.pickStack(stacks)
    stack_to_keep = json.dump(stack_to_keep)
    return stack_to_keep

  def main(self):
    """
    Setup and manage TCP connection to game server; deliver messages as Python
    objects to the appropriate player proxy method, return their responses (as JSON)
    to the game server.
    """
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
      raise Exception('Socket error {} : {}'.format(msg[0], msg[1]))

    try:
      s.connect((HOST, PORT))
    except socket.error as msg:
      raise Exception('Socket error {} : {}'.format(msg[0], msg[1]))


    data = s.recv(BUFFERSIZE)
    message = json.load(data)
    while message:
      if 'start-round' == message[0]:
        hand = self.parse_lcard(message[1:])
        if not round_in_progress and (len(hand) == HANDSIZE):
          ack = self.start_round(hand)
          s.send(ack)
          round_in_progress = True
        else:
          s.send(json.dump(False))
          s.close()
      elif 'take-turn' == message[0]:
        list_of_Stacks = self.parse_deck(message[1:])
        if round_in_progress and (len(list_of_Stacks) == NUMBER_OF_DECKS):
          players_card = self.take_turn(list_of_Stacks)
          s.send(players_card)
          last_received == 'take-turn'
        else:
          s.send(json.dump(False))
          s.close()
      elif 'choose' == message[0]:
        list_of_Stacks = self.parse_deck(message[1:])
        if round_in_progress and (len(list_of_Stacks) == NUMBER_OF_DECKS) and (last_received == 'take-turn'):
          stack_to_keep = self.choose(list_of_Stacks)
          s.send(stack_to_keep)
          last_received == 'choose'
        else:
          s.send(json.dump(False))
          s.close()
      else:
        s.close()

if __name__ == "__main__":
  RemoteProxyPlayer()