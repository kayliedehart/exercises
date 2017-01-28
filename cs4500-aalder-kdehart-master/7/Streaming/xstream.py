#!/usr/bin/env python
# Echo program to count and echo JSON input from stdin
import os, sys
import json
from json import JSONDecoder

class EchoStream:
	previous = ""
	open_cbracket = 0
	open_bracket = 0

	def __init__(self):
		self.main()
		# pass

	def validate(self, frag):
		"""
		Validate input as correct JSON.
		If there are multiple JSON entities separated by a space, evaluate them separately.
		If there is an incomplete JSON array or object, buffer the fragment and wait to see
		if the object or array completes.
		Return a list of the valid JSON fragments passed in, or False.
		"""
		valid_input = []
		jsonObj = []
		end = 0
		jsonString = ""
		try:
			decoder = JSONDecoder()
			fragLength = len(frag)

			while end != fragLength:
					obj, end = decoder.raw_decode(frag, idx=end)
					jsonObj.append(obj)

			valid_input.append(jsonObj)

			return valid_input
		except ValueError:
			print "This JSON is not valid. Shutting down now"
			sys.exit()

	def getJsonInLine(self, line):
		"""
		Parses the JSON in that line appart and returns a list of the valid json bits. Puts
		the non valid bits into the buffer for storage until made good. Throws an error if invalid JSON
		Takes: A string
		Returns: A list of valid JSON objects.
		"""
		jsonList = []

		for character in line:
			if character == " ":
				if (self.open_cbracket != 0) or (self.open_bracket != 0):
					pass
				else:
					newJson = self.validate(self.previous)
					print newJson[0][0]
					jsonList.extend(newJson)
					self.previous = ""
			elif character == "{":
				if self.open_cbracket == 0 and self.open_bracket == 0 and self.previous!="":
					newJson = self.validate(self.previous)
					print newJson[0][0]
					jsonList.extend(newJson)
					self.previous=""
				self.open_cbracket += 1
				self.previous += character
			elif character == "}":
				self.open_cbracket -= 1
				self.previous += character
				if self.open_cbracket == 0 and self.open_bracket == 0:
					newJson = self.validate(self.previous)
					print newJson[0][0]
					jsonList.extend(newJson)
					self.previous=""
			elif character == "[":
				self.open_bracket += 1
				self.previous += character
			elif character == "]":
				self.open_bracket -= 1
				self.previous += character
				if self.open_cbracket == 0 and self.open_bracket == 0:
					newJson = self.validate(self.previous)
					print newJson[0][0]
					jsonList.extend(newJson)
					self.previous=""
			else:
				self.previous += character
		if (self.previous != "") and (self.open_bracket == 0) and (self.open_cbracket == 0):
			newJson = self.validate(self.previous)
			self.previous = ""
			print newJson[0][0]
			jsonList.extend(newJson)
		return jsonList

	def main(self):
		"""
		Get input from stdin, validate, and then echo. When done, return the number of
		messages received.
		"""
		msg_count = {"count": 0}
		while True:
			line = sys.stdin.readline()
			if line:
				line = line.strip("\n")
				echo_frag = self.getJsonInLine(line)
				if echo_frag:
					for echo in echo_frag:
						msg_count["count"] += 1
			else:
				print msg_count
				sys.exit()


if __name__ == "__main__":
	EchoStream()
