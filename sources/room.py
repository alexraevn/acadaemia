import json
import os

def getRoom(n):

	c = os.path.dirname(os.path.realpath(__file__))
	o = open(os.path.join(c,'rooms/')+str(n)+'.json', 'r')
	txt = o.read()
	roomdic = json.loads(txt)
	r = Room(**roomdic)
	return r

class Room:
	def __init__(self, n, name, description, items, state, neighbors):

		self.n = n
		self.name = name
		self.description = description
		self.items = items
		self.state = state
		self.neighbors = neighbors
