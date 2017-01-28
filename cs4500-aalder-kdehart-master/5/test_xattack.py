# Automated unit tests for a xattack test harness for Evolution game
import unittest
import xattack
from attack import species
from attack import trait

class TestXAttack(unittest.TestCase):
	"""./xattack.py < test-in.json | diff - 1-out.json"""

  def setUp(self):
    self.spec = species.Species(0,1,1, [])

  def tearDown(self):
    del self.spec

  def diff(self, expected, output_file):
  	"""
  	Utility for comparing diffs of a given JSON file and a json expression
  	"""
  	for line in outfile.readline():

    with expected as f1, open(output_file) as f2:

  def test_json(self):
    self.assertFalse(xattack(open(attack_1.json)))
    self.assertFalse(xattack(open(attack_2.json)))
	        
    

  def testMain(self):



if __name__ == '__main__':
    unittest.main()




