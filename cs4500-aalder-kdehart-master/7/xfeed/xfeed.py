# a test harness for the feed method in Player for a game of Evolution
import player
import parse_json
import make_json
import json
import sys


class TestHarness:
	def __init__(self):
		self.main()
		#pass

	def main(self):
		"""
		Get input from stdin, parse, and get Player's response, parse, and return to stdout
		"""
		feeding = json.load(sys.stdin)

		p_json = parse_json.ParseJSON()
		m_json = make_json.MakeJSON()

		feeding_py = p_json.parse_feeding(feeding)

		if not feeding_py:
			raise Exception("No valid feeding situation received")

		test_player, free_food, players_list = feeding_py

		result = test_player.feed(players_list, free_food)

		print m_json.make_meal(result)

	def testMethod(self, given):
		"""
		Method to unit test xfeed, feeding in a JSON from the method rather than stdin and
		returning the result rather than printing tp stdout
		"""
		p_json = parse_json.ParseJSON()
		m_json = make_json.MakeJSON()

		feeding_py = p_json.parse_feeding(given)

		if not feeding_py:
			raise Exception("No valid feeding situation received")

		test_player, free_food, players_list = feeding_py

		result = test_player.feed(players_list, free_food)

		return m_json.make_meal(result)

if __name__ == "__main__":
	TestHarness()
