#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution

from attack import dealer
from attack import trait
from attack import species
from cs4500-aalder-kdehart import parse_json.ParseJSON as parse_json
from cs4500-aalder-kdehart import make_json.MakeJSON as make_json
import sys


class TestHarness:
	def __init__(self):
		self.main()

	def main(self):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)], 
			return a Boolean to stdout whether or not the attack is successful.
		"""
		situation = json.load(sys.stdin)

		p_json = parse_json.ParseJSON()
		m_json = make_json.MakeJSON()

		species_list = p_json.parse_situation(situation)

		attacker, defender, neighborRight, neighborLeft = species_list

		result = attacker.attackable(species_list)

		m_json.make_attack(result)

if __name__ == "__main__":
	TestHarness()
