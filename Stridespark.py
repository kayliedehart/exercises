import sys
import unittest
from collections import defaultdict


""" Represents a single node and it's links [direct and indirect] """
class Node:

	def __init__(self, number):
		self.number = number
		self.direct = defaultdict(lambda: False)
		self.links = defaultdict(lambda: False)


"""
Class representing the graph and maintanence/ traversal methods
Space Complexity: O(n^2n)
"""
class Graph:

	def __init__(self):
		self.graph = {}


	def prep_line(self):
		"""
		Break apart commands from stdin into a list of 3 part instruction sets
		of the format (commandString, int, int); initialize nodes in self.graph
		@return: list of (commandString, int, int)
		Time Complexity:O(n)
		"""
		global line

		line = line.split('\n')
		commands = []

		for l in line:
			if l:
				l = l.split()
				if l[0] == "is" and l[1] == "linked":
					l[0] = "is linked"
					l.remove("linked")
				
				if l[0] not in ["add", "remove", "is_linked"]:
					pass

				if not l[1] in self.graph.keys():
					self.graph[l[1]] = Node(l[1])
				if not l[2] in self.graph.keys():
					self.graph[l[2]] = Node(l[2])
				commands.append((l[0], l[1], l[2]))
		return commands


	def update_graph(self, x, y, change):
		"""
		Recursively update all connected nodes with a change
		in the graph
		@params x, y, change - x: node to be updated, 
							   y: node to iterate on, 
							   change: Boolean
		@return None
		Time Complexity: O(n^n)
		"""
		if change:
			self.graph[x].links[y] = change
		self.graph[y].links[x] = change
		for k in [k for k, v in self.graph[x].direct.items() if v == True]:
			# if the neighbors don't already know, update (else, don't loop)
			if not self.graph[k].links[x] == change:
				self.update_graph(x, k, change)


	def add_link(self, x, y):
		"""
		Helper function to add a new link to the graph
		@params: x, y - nodes to be connected
		@return: None
		Time Complexity:O(2n^n)
		"""
		self.graph[x].direct[y] = True
		self.graph[y].direct[x] = True

		self.graph[x].links[y] = True
		self.graph[y].links[x] = True

		for k in [k for k, v in self.graph[x].direct.items() if v == True]:
			self.update_graph(k, y, True)
		for k in [k for k, v in self.graph[y].direct.items() if v == True]:
			self.update_graph(k, x, True)


	def remove_link(self, x, y):
		"""
		Helper function to remove a link from the graph
		@params: x, y - nodes to be disconnected
		@return: None
		Time Complexity:O(2n^n)
		"""
		self.graph[x].direct[y] = False
		self.graph[y].direct[x] = False

		self.graph[x].links[y] = False
		self.graph[y].links[x] = False

		for k in [k for k, v in self.graph[x].direct.items() if v == True]:
			self.update_graph(k, y, False)
		for k in [k for k, v in self.graph[y].direct.items() if v == True]:
			self.update_graph(k, x, False)


	def is_linked(self, x, y):
		"""
		Helper function to determine if a link exists in the graph
		@params: x, y - nodes to check
		@return: Boolean
		Time Complexity:O(1)
		"""
		return (self.graph[x].links[y] or x == y)


	def process_links(self, line):
		"""
		Carries out commands from stdin, either updating the graph or
		printing whether the given pair of nodes are linked
		@params: line - a 3 item String command from stdin
		@return: None if update or invalid input; Boolean if Query
		Time Complexity:O(2n^n)
		"""
		command, x, y = line
		if command == "add":
			self.add_link(x, y)
		elif command == "remove":
			self.remove_link(x, y)
		elif command == "is linked":
			return self.is_linked(x, y)
		else:
			pass



""" Unit tests """

class TestUpdateGraph(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.graph[1] = Node(1)
		self.g.graph[2] = Node(2)
		self.g.graph[3] = Node(3)
		self.g.graph[2].links[3] = True
		self.g.graph[2].direct[3] = True
		self.g.graph[3].links[2] = True
		self.g.graph[3].direct[2] = True

	def tearDown(self):
		del self.g

	def test_add(self):
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.g.update_graph(1, 3, True)
		self.g.update_graph(3, 1, True)
		self.assertTrue(self.g.graph[1].links[3])
		self.assertTrue(self.g.graph[3].links[1])

	def test_remove(self):
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		
		self.g.update_graph(1, 3, True)
		self.g.update_graph(3, 1, True)
		self.assertTrue(self.g.graph[1].links[3])
		self.assertTrue(self.g.graph[3].links[1])

		self.g.update_graph(1, 3, False)
		self.g.update_graph(3, 1, False)
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])

class TestAddLink(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.graph[1] = Node(1)
		self.g.graph[2] = Node(2)
		self.g.graph[3] = Node(3)

	def tearDown(self):
		del self.g

	def test_basic(self):
		# No links
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		# New link
		self.g.add_link(1, 3)

		self.assertTrue(self.g.graph[1].links[3])
		self.assertTrue(self.g.graph[3].links[1])
		self.assertTrue(self.g.graph[1].direct[3])
		self.assertTrue(self.g.graph[3].direct[1])
	
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])

	def test_alreadyExists(self):
		# Nodes 2 and 3 start connected
		self.g.graph[2].links[3] = True
		self.g.graph[2].direct[3] = True
		self.g.graph[3].links[2] = True
		self.g.graph[3].direct[2] = True

		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])

		# Try to "add 2 3"
		self.g.add_link(2, 3)

		# No change
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])


class TestRemoveLink(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.graph[1] = Node(1)
		self.g.graph[2] = Node(2)
		self.g.graph[3] = Node(3)

	def tearDown(self):
		 del self.g

	def test_basic(self):
		# Nodes 2 and 3 start connected
		self.g.graph[2].links[3] = True
		self.g.graph[2].direct[3] = True
		self.g.graph[3].links[2] = True
		self.g.graph[3].direct[2] = True

		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])

		# Try to "remove 2 3"
		self.g.remove_link(2, 3)

		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])


	def test_doesNotExist(self):
		# No links
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		# Try to "remove 2 3"
		self.g.remove_link(2, 3)

		# No change
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])


class TestIsLinked(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.graph[1] = Node(1)
		self.g.graph[2] = Node(2)
		self.g.graph[3] = Node(3)

	def tearDown(self):
		del self.g

	def test_basicTrue(self):
		# Nodes 2 and 3 start connected
		self.g.graph[2].links[3] = True
		self.g.graph[2].direct[3] = True
		self.g.graph[3].links[2] = True
		self.g.graph[3].direct[2] = True

		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])
		
		self.assertTrue(self.g.is_linked(2, 3))
		
		# No change
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])

	def test_basicFalse(self):
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])
		
		self.assertFalse(self.g.is_linked(1, 3))
		
		self.assertFalse(self.g.graph[1].links[3])
		self.assertFalse(self.g.graph[3].links[1])
		self.assertFalse(self.g.graph[1].links[2])
		self.assertFalse(self.g.graph[2].links[1])
		self.assertFalse(self.g.graph[2].links[3])
		self.assertFalse(self.g.graph[3].links[2])
		self.assertFalse(self.g.graph[1].direct[2])
		self.assertFalse(self.g.graph[2].direct[1])
		self.assertFalse(self.g.graph[2].direct[3])
		self.assertFalse(self.g.graph[3].direct[2])
		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

	def test_indirectTrue(self):
		# Nodes 2 and 3 start connected
		self.g.graph[2].links[3] = True
		self.g.graph[2].direct[3] = True
		self.g.graph[3].links[2] = True
		self.g.graph[3].direct[2] = True

		# Nodes 2 and 1 start connected
		self.g.graph[2].links[1] = True
		self.g.graph[2].direct[1] = True
		self.g.graph[1].links[2] = True
		self.g.graph[1].direct[2] = True

		# implied links 1 & 3
		self.g.graph[3].links[1] = True
		self.g.graph[1].links[3] = True


		self.assertTrue(self.g.graph[1].links[3])
		self.assertTrue(self.g.graph[3].links[1])
		self.assertTrue(self.g.graph[1].links[2])
		self.assertTrue(self.g.graph[2].links[1])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])
		self.assertTrue(self.g.graph[1].direct[2])
		self.assertTrue(self.g.graph[2].direct[1])
		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])

		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])
		
		self.assertTrue(self.g.is_linked(1, 3))
		
		# No change
		self.assertTrue(self.g.graph[1].links[3])
		self.assertTrue(self.g.graph[3].links[1])
		self.assertTrue(self.g.graph[1].links[2])
		self.assertTrue(self.g.graph[2].links[1])
		self.assertTrue(self.g.graph[2].links[3])
		self.assertTrue(self.g.graph[3].links[2])
		self.assertTrue(self.g.graph[1].direct[2])
		self.assertTrue(self.g.graph[2].direct[1])
		self.assertTrue(self.g.graph[2].direct[3])
		self.assertTrue(self.g.graph[3].direct[2])

		self.assertFalse(self.g.graph[1].direct[3])
		self.assertFalse(self.g.graph[3].direct[1])

class TestProcessLinks(unittest.TestCase):
	def setUp(self):
		self.g = Graph()
		self.g.graph[1] = Node(1)
		self.g.graph[2] = Node(2)
		self.g.graph[3] = Node(3)
		self.g.graph[4] = Node(4)
		self.g.graph[5] = Node(5)

	def tearDown(self):
		del self.g

	def test_basic_invalid(self):
		self.assertIsNone(self.g.process_links(("skjbh", 1, 5)))
		self.assertIsNone(self.g.process_links(("skjbh", 15,"kibble 4 7")))

	def test_basic_true(self):
		self.g.process_links(("add", 1, 5))
		self.assertTrue(self.g.process_links(("is linked", 1, 5)))

	def test_basic_false(self):
		self.g.process_links(("remove", 1, 5))
		self.assertFalse(self.g.process_links(("is linked", 1, 5)))
		self.assertFalse(self.g.process_links(("is linked", 1, 5)))
		self.assertFalse(self.g.process_links(("", "", "")))

	def test_severalLinksAwayTrue(self):
		self.g.process_links(("remove", 1, 2))
		self.g.process_links(("add", 1, 2))
		self.g.process_links(("add", 2, 3))
		self.g.process_links(("add", 1, 3))
		self.g.process_links(("add", 3, 4))

		self.assertTrue(self.g.process_links(("is linked", 1, 2)))
		self.assertTrue(self.g.process_links(("is linked", 2, 3)))
		self.assertTrue(self.g.process_links(("is linked", 3, 1)))
		self.assertTrue(self.g.process_links(("is linked", 3, 4)))
		self.assertTrue(self.g.process_links(("is linked", 4, 2)))
		self.assertTrue(self.g.process_links(("is linked", 1, 3)))
		self.assertTrue(self.g.process_links(("is linked", 4, 3)))
		self.assertTrue(self.g.process_links(("is linked", 1, 1)))
		self.assertTrue(self.g.process_links(("is linked", 1, 4)))
		self.assertTrue(self.g.process_links(("is linked", 4, 1)))


# if __name__ == '__main__':
#     unittest.main()

if __name__ == '__main__':
    response = ""
    graph = Graph()

    while True:
		line = sys.stdin.readline()

		if not line:
			break

	    commands = graph.prep_line()
	    for c in commands:
	        if graph.process_links(c) is not None:
	            response += (str(graph.process_links(c)).lower() + "\n")
	print(response)


