# unit tests for EchoStream's validate method
import unittest
import xstream

class TestSpecies(unittest.TestCase):

  def setUp(self):
    self.xs = xstream.EchoStream()
    self.frag1 = '3'
    self.frag2 = '[1, 3, 5]'
    self.frag3 = '4{"cookies" : 246}'
    self.frag4 = '{}'

  def tearDown(self):
    del self.frag1
    del self.frag2
    del self.frag3
    del self.frag4

  def testValidate1(self):
    self.assertEqual(self.xs.getJsonInLine(self.frag1), [[3]])

  def testValidate2(self):
    self.assertEqual(self.xs.getJsonInLine(self.frag2), [[[1, 3, 5]]])

  def testValidate3(self):
    self.assertEqual(self.xs.getJsonInLine(self.frag3), [[4], [{u'cookies' : 246}]])

  def testValidate4(self):
    self.assertEqual(self.xs.getJsonInLine(self.frag4), [[{}]])


if __name__ == '__main__':
    unittest.main()
