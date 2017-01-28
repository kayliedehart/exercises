# Automated unit tests for a xattack test harness for Evolution game
import unittest
import xattack_fixed
import species
import trait
import json

class TestXAttack(unittest.TestCase):
  def setUp(self):
    self.tester_xattack = xattack_fixed.TestHarness()
    self.case_0357_6344_1_in = [[["food",3], ["body",3], ["population",3], ["traits",[]]], [["food",3], ["body",3], ["population",3], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_1_out = json.dumps(True)

    self.case_0357_6344_5_in = [[["food",1], ["body",3], ["population",5], ["traits",["symbiosis"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], [["food",2], ["body",5], ["population",5], ["traits",[]]], False]
    self.case_0357_6344_5_out = json.dumps(True)

    self.case_0357_6344_8_in = [[["food",1], ["body",3], ["population",4], ["traits",["herding"]]], [["food",2], ["body",4], ["population",5], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_8_out = json.dumps(True)

    self.case_0357_6344_9_in =[[["food",1], ["body",3], ["population",4], ["traits",["herding"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_9_out = json.dumps(False)

    self.case_0357_6344_11_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], [["food",2], ["body",3], ["population",4], ["traits",["warning-call"]]], False]
    self.case_0357_6344_11_out = json.dumps(False)

    self.case_0357_6344_12_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore", "ambush"]]], False, False]
    self.case_0357_6344_12_out = json.dumps(True)

    self.case_0357_6344_13_in = [[["food",2], ["body",3], ["population",4], ["traits",[]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore", "ambush"]]], False, [["food",2], ["body",3], ["population",4], ["traits",["warning-call"]]]]
    self.case_0357_6344_13_out = json.dumps(True)

    self.case_0357_6344_14_in = [[["food",2], ["body",3], ["population",4], ["traits",["burrowing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_14_out = json.dumps(True)

    self.case_0357_6344_15_in = [[["food",3], ["body",3], ["population",3], ["traits",["burrowing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_15_out = json.dumps(False)

    self.case_0357_6344_16_in = [[["food",2], ["body",3], ["population",4], ["traits",["climbing"]]], [["food",2], ["body",7], ["population",3], ["traits",["carnivore"]]], False, False]
    self.case_0357_6344_16_out = json.dumps(False)

    self.case_0623_8070_1_in = [
                            [["food", 1], ["body", 0], ["population", 1], ["traits", []]],
                            [["food", 1], ["body", 0], ["population", 1], ["traits", ["carnivore"]]],
                            False,
                            False
                          ]
    self.case_0623_8070_1_out = json.dumps(True)

    self.case_1073_6112_3_in = [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["carnivore"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ]
                          ]
    self.case_1073_6112_3_out = json.dumps(True)

    self.case_1073_6112_4_in = [
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["climbing"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", ["carnivore", "climbing"]]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ],
                            [
                              ["food", 1],
                              ["body", 2],
                              ["population", 3],
                              ["traits", []]
                            ]
                          ]
    self.case_1073_6112_4_out = json.dumps(True)

    self.case_1073_6112_5_in =[
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["cooperation", "fertile", "ambush"]]
                          ],
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["carnivore"]]
                          ],
                          False,
                          [
                            ["food", 1],
                            ["body", 2],
                            ["population", 3],
                            ["traits", ["warning-call", "horns"]]
                          ]
                        ]
    self.case_1073_6112_5_out = json.dumps(False)

    self.case_2657_7498_1_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], False, False ]
    self.case_2657_7498_1_out = json.dumps(True)

    self.case_2657_7498_2_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["burrowing", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], False, False ]
    self.case_2657_7498_2_out = json.dumps(False)

    self.case_2657_7498_3_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["symbiosis", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["warning-call", "carnivore"]] ], False ]
    self.case_2657_7498_3_out = json.dumps(False)

    self.case_2657_7498_4_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["warning-call", "carnivore"]] ], False ]
    self.case_2657_7498_4_out = json.dumps(True)

    self.case_2657_7498_5_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",[]] ], False ]
    self.case_2657_7498_5_out = json.dumps(True)

    self.case_2657_7498_6_in = [ [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["symbiosis", "carnivore"]] ],
                            [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",["ambush", "carnivore"]] ],
                            [ ["food",3],
                              ["body",3],
                              ["population",3],
                              ["traits",[]] ], False ]
    self.case_2657_7498_6_out = json.dumps(True)

    self.case_2657_7498_8_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["climbing"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], False, [ ["food",3], ["body",4], ["population",3], ["traits",[]] ] ]
    self.case_2657_7498_8_out = json.dumps(False)

    self.case_2657_7498_9_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["climbing"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["climbing", "carnivore"]] ], False, [ ["food",3], ["body",4], ["population",3], ["traits",[]] ] ]
    self.case_2657_7498_9_out = json.dumps(True)

    self.case_2657_7498_10_in = [ [ ["food",3], ["body",3], ["population",3], ["traits",["hard-shell", "carnivore"]] ], [ ["food",3], ["body",3], ["population",3], ["traits",["ambush", "carnivore"]] ], False, False ]
    self.case_2657_7498_10_out = json.dumps(False)

    self.case_2657_7498_12_in = [ [ ["food",3], ["body",4], ["population",3], ["traits",["hard-shell", "carnivore"]] ], [ ["food",3], ["body",7], ["population",3], ["traits",["ambush", "carnivore"]] ], False, False ]
    self.case_2657_7498_12_out = json.dumps(False)

    self.case_2657_7498_14_in = [ [ ["food",3], ["body",4], ["population",3], ["traits",[]] ], [ ["food",1], ["body",7], ["population",1], ["traits",["carnivore"]] ], [ ["food",1], ["body",7], ["population",1], ["traits",["warning-call"]] ], False ]
    self.case_2657_7498_14_out = json.dumps(False)

    self.case_9634_1853_1_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_1_out = json.dumps(True)

    self.case_9634_1853_3_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], False]
    self.case_9634_1853_3_out = json.dumps(False)

    self.case_9634_1853_4_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]]]
    self.case_9634_1853_4_out = json.dumps(False)

    self.case_9634_1853_5_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", []]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore", "ambush"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["warning-call"]]], False]
    self.case_9634_1853_5_out = json.dumps(True)

    self.case_9634_1853_7_in = [[["food", 6], ["body", 0], ["population", 6], ["traits", ["burrowing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_7_out = json.dumps(False)

    self.case_9634_1853_8_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["climbing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_8_out = json.dumps(False)

    self.case_9634_1853_9_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["climbing"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore", "climbing"]]], False, False]
    self.case_9634_1853_9_out = json.dumps(True)

    self.case_9634_1853_10_in =[[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_10_out = json.dumps(False)

    self.case_9634_1853_11_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 3], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_11_out = json.dumps(False)

    self.case_9634_1853_13_in =[[["food", 0], ["body", 0], ["population", 1], ["traits", ["herding"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_13_out = json.dumps(False)

    self.case_9634_1853_14_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["herding"]]], [["food", 0], ["body", 0], ["population", 2], ["traits", ["carnivore"]]], False, False]
    self.case_9634_1853_14_out = json.dumps(True)

    self.case_9634_1853_18_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["symbiosis"]]], [["food", 0], ["body", 0], ["population", 1], ["traits", ["carnivore"]]], False, [["food", 0], ["body", 0], ["population", 1], ["traits", []]]]
    self.case_9634_1853_18_out = json.dumps(True)

    self.case_9634_1853_20_in = [[["food", 0], ["body", 0], ["population", 1], ["traits", ["hard-shell"]]], [["food", 0], ["body", 0], ["population", 3], ["traits", ["carnivore", "pack-hunting"]]], False, False]
    self.case_9634_1853_20_out = json.dumps(False)

    self.matthias_1_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,False]
    self.matthias_1_out = json.dumps(True)

    self.matthias_2_in = [[["food",1],["body",1],["population",1],["traits",["burrowing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,False]
    self.matthias_2_out = json.dumps(False)

    self.matthias_3_in = [[["food",3],["body",1],["population",4],["traits",["burrowing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,False]
    self.matthias_3_out = json.dumps(True)

    self.matthias_4_in = [[["food",3],["body",1],["population",4],["traits",["climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,False]
    self.matthias_4_out = json.dumps(False)

    self.matthias_5_in = [[["food",3],["body",1],["population",4],["traits",["climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","climbing"]]],False,False]
    self.matthias_5_out = json.dumps(True)

    self.matthias_6_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,False]
    self.matthias_6_out = json.dumps(False)

    self.matthias_7_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",7],["population",3],["traits",["carnivore"]]],False,False]
    self.matthias_7_out = json.dumps(True)

    self.matthias_8_in = [[["food",2],["body",2],["population",3],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","pack-hunting"]]],False,False]
    self.matthias_8_out = json.dumps(True)

    self.matthias_9_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],False]
    self.matthias_9_out = json.dumps(False)

    self.matthias_10_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],False,[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    self.matthias_10_out = json.dumps(False)

    self.matthias_11_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    self.matthias_11_out = json.dumps(False)

    self.matthias_12_in = [[["food",3],["body",1],["population",4],["traits",[]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush"]]],False,[["food",2],["body",2],["population",3],["traits",["warning-call"]]]]
    self.matthias_12_out = json.dumps(True)

    self.matthias_13_in = [[["food",2],["body",2],["population",2],["traits",["hard-shell"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],False]
    self.matthias_13_out = json.dumps(True)

    self.matthias_14_in = [[["food",2],["body",2],["population",2],["traits",["hard-shell","climbing"]]],[["food",2],["body",3],["population",4],["traits",["carnivore","ambush","pack-hunting"]]],[["food",2],["body",2],["population",3],["traits",["warning-call"]]],False]
    self.matthias_14_out = json.dumps(False)


  def tearDown(self):
    del self.tester_xattack
    del self.case_0357_6344_1_in
    del self.case_0357_6344_1_out
    del self.case_0357_6344_5_in
    del self.case_0357_6344_5_out
    del self.case_0357_6344_8_in
    del self.case_0357_6344_8_out
    del self.case_0357_6344_9_in
    del self.case_0357_6344_9_out
    del self.case_0357_6344_11_in
    del self.case_0357_6344_11_out
    del self.case_0357_6344_12_in
    del self.case_0357_6344_12_out
    del self.case_0357_6344_13_in
    del self.case_0357_6344_13_out
    del self.case_0357_6344_15_in
    del self.case_0357_6344_15_out
    del self.case_0357_6344_16_in
    del self.case_0357_6344_16_out

    del self.case_0623_8070_1_in
    del self.case_0623_8070_1_out

    del self.case_1073_6112_3_in
    del self.case_1073_6112_3_out
    del self.case_1073_6112_4_in
    del self.case_1073_6112_4_out
    del self.case_1073_6112_5_in
    del self.case_1073_6112_5_out

    del self.case_2657_7498_1_in
    del self.case_2657_7498_1_out
    del self.case_2657_7498_2_in
    del self.case_2657_7498_2_out
    del self.case_2657_7498_3_in
    del self.case_2657_7498_3_out
    del self.case_2657_7498_4_in
    del self.case_2657_7498_4_out
    del self.case_2657_7498_5_in
    del self.case_2657_7498_5_out
    del self.case_2657_7498_6_in
    del self.case_2657_7498_6_out
    del self.case_2657_7498_8_in
    del self.case_2657_7498_8_out
    del self.case_2657_7498_9_in
    del self.case_2657_7498_9_out
    del self.case_2657_7498_10_in
    del self.case_2657_7498_10_out
    del self.case_2657_7498_12_in
    del self.case_2657_7498_12_out
    del self.case_2657_7498_14_in
    del self.case_2657_7498_14_out

    del self.case_9634_1853_1_in
    del self.case_9634_1853_1_out
    del self.case_9634_1853_3_in
    del self.case_9634_1853_3_out
    del self.case_9634_1853_4_in
    del self.case_9634_1853_4_out
    del self.case_9634_1853_5_in
    del self.case_9634_1853_5_out
    del self.case_9634_1853_7_in
    del self.case_9634_1853_7_out
    del self.case_9634_1853_8_in
    del self.case_9634_1853_8_out
    del self.case_9634_1853_9_in
    del self.case_9634_1853_9_out
    del self.case_9634_1853_10_in
    del self.case_9634_1853_10_out
    del self.case_9634_1853_11_in
    del self.case_9634_1853_11_out
    del self.case_9634_1853_13_in
    del self.case_9634_1853_13_out
    del self.case_9634_1853_14_in
    del self.case_9634_1853_14_out
    del self.case_9634_1853_18_in
    del self.case_9634_1853_18_out
    del self.case_9634_1853_20_in
    del self.case_9634_1853_20_out

    del self.matthias_1_in
    del self.matthias_1_out
    del self.matthias_2_in
    del self.matthias_2_out
    del self.matthias_3_in
    del self.matthias_3_out
    del self.matthias_4_in
    del self.matthias_4_out
    del self.matthias_5_in
    del self.matthias_5_out
    del self.matthias_6_in
    del self.matthias_6_out
    del self.matthias_7_in
    del self.matthias_7_out
    del self.matthias_8_in
    del self.matthias_8_out
    del self.matthias_9_in
    del self.matthias_9_out
    del self.matthias_10_in
    del self.matthias_10_out
    del self.matthias_11_in
    del self.matthias_11_out
    del self.matthias_12_in
    del self.matthias_12_out
    del self.matthias_13_in
    del self.matthias_13_out
    del self.matthias_14_in
    del self.matthias_14_out


  def test_0357_6344(self):
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_1_in), self.case_0357_6344_1_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_5_in), self.case_0357_6344_5_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_8_in), self.case_0357_6344_8_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_9_in), self.case_0357_6344_9_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_11_in), self.case_0357_6344_11_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_12_in), self.case_0357_6344_12_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_13_in), self.case_0357_6344_13_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_14_in), self.case_0357_6344_14_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_15_in), self.case_0357_6344_15_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_0357_6344_16_in), self.case_0357_6344_16_out)

  def test_0623_8070(self):
    self.assertEqual(self.tester_xattack.testMethod(self.case_0623_8070_1_in), self.case_0623_8070_1_out)

  def test_1073_6112(self):
    self.assertEqual(self.tester_xattack.testMethod(self.case_1073_6112_3_in), self.case_1073_6112_3_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_1073_6112_4_in), self.case_1073_6112_4_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_1073_6112_5_in), self.case_1073_6112_5_out)

  def test_2657_7498(self):
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_1_in), self.case_2657_7498_1_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_2_in), self.case_2657_7498_2_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_3_in), self.case_2657_7498_3_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_4_in), self.case_2657_7498_4_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_5_in), self.case_2657_7498_5_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_6_in), self.case_2657_7498_6_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_8_in), self.case_2657_7498_8_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_9_in), self.case_2657_7498_9_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_10_in), self.case_2657_7498_10_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_12_in), self.case_2657_7498_12_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_2657_7498_14_in), self.case_2657_7498_14_out)

  def test_9634_1853(self):
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_1_in), self.case_9634_1853_1_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_3_in), self.case_9634_1853_3_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_4_in), self.case_9634_1853_4_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_5_in), self.case_9634_1853_5_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_7_in), self.case_9634_1853_7_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_8_in), self.case_9634_1853_8_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_9_in), self.case_9634_1853_9_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_10_in), self.case_9634_1853_10_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_11_in), self.case_9634_1853_11_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_13_in), self.case_9634_1853_13_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_14_in), self.case_9634_1853_14_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_18_in), self.case_9634_1853_18_out)
    self.assertEqual(self.tester_xattack.testMethod(self.case_9634_1853_20_in), self.case_9634_1853_20_out)

  def test_matthias(self):
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_1_in), self.matthias_1_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_2_in), self.matthias_2_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_3_in), self.matthias_3_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_4_in), self.matthias_4_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_5_in), self.matthias_5_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_6_in), self.matthias_6_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_7_in), self.matthias_7_out)

  def test_mattias8(self):
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_8_in), self.matthias_8_out)

  def test_mattias_rest(self):
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_9_in), self.matthias_9_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_10_in), self.matthias_10_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_11_in), self.matthias_11_out)
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_12_in), self.matthias_12_out)

  def test_mattias13(self):
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_13_in), self.matthias_13_out)

  def test_mattias14(self):
    self.assertEqual(self.tester_xattack.testMethod(self.matthias_14_in), self.matthias_14_out)



if __name__ == '__main__':
    unittest.main()