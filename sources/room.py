import json

def getRoom(n):

	o = open('/home/alex22x/bin/acadaemia/sources/rooms/'+str(n)+'.json', 'r')
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
