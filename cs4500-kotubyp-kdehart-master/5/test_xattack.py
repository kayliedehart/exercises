#!/usr/bin/env python2.7

import sys
import subprocess

TEST_PATH = "attack/json_tests/"
PYTHON2_PATH = "py.exe"

def xattack(testName, fileName):
    printing = testName + "\n    result: "

    try:
        result = subprocess.check_output(PYTHON2_PATH + " " + sys.path[0] +"\\"+ "xattack", stdin=fileName)
        if not result:
            printing += "program quit\n"
        else:
            printing += result
    except Exception as e:
        printing += str(e)

    print printing

with open(TEST_PATH + "/bad_io.txt", "r") as badIO:
    xattack("gibberish input (xattack should quit)", badIO)

with open(TEST_PATH + "/bad_input_1.json", "r") as badJson:
    xattack("bad json input (xattack should quit)", badJson)

with open(TEST_PATH + "burrowing_false.json", "r") as burr_false:
    xattack("burrowing and equal food/pop (should be a boolean)", burr_false)

with open(TEST_PATH + "burrowing_true.json", "r") as burr_true:
    xattack("burrowing w/o equal food/pop (should be a boolean)", burr_true)
