#!/usr/bin/env python
# a test harness for the attackable method in Dealer for a game of Evolution

import trait
import species
import parse_json
import make_json
import sys
import json


class TestHarness:
	def __init__(self):
		self.main()
		#pass

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

	def testMethod(self, given):
		"""
		For a given Situation (a JSON of [attacking:Species, defending:Species, (neighbor:Species), (neighbor:Species)],
			return a Boolean to stdout whether or not the attack is successful. (TESTS)
		"""

		p_json = parse_json.ParseJSON()
		m_json = make_json.MakeJSON()

		species_list = p_json.parse_situation(given)

		attacker, defender, neighborRight, neighborLeft = species_list

		result = attacker.attackable(species_list)

		return m_json.make_attack_test(result)

if __name__ == "__main__":
	TestHarness()
