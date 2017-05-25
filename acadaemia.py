#   /     Acadaemia 1.0     \
# _/     A game by Raevn     \_
import time
import random
import sources.room as room
import sources.player as player

# Commands:
see = ['see', 'look', 'examine']
dirs = ['north', 'south', 'east', 'west']
h = ['help', 'Help']

print "Welcome to Acadaemia 0.1.\nType 'help' for commands."

class Game:

	def __init__(self):

		self.loc = room.getRoom(1)
		self.player = player.Player(4.0, items=['note'])

	def examine(self, i=None):

		if i == None:
			print self.loc.name
			time.sleep(0.5)
			print self.loc.description

		else:
			print 'There are no items yet.'

	def move(self, direction):

		if direction in self.loc.neighbors:
			self.loc = room.getRoom(self.loc.neighbors[direction])
			Game.examine()
		else:
			print "You cannot go " + direction + "."

Game = Game()
inGame = True
while inGame:
	done = False
	c = raw_input('-')
	words = c.split(' ', -1)

	for i in words:
		if i in see:
			for z in words:
				if z in Game.player.items:
					Game.examine(i=z)
					done = True
					break

	if done == False:
		for i in words:
			if i in see:
				Game.examine()
				done = True
				break

			elif i == 'inventory':
				print Game.player.items
				done = True
				break

			elif i in dirs:
				Game.move(i)
				done = True
				break

	if words[0] == "exit":
		a = raw_input("Are you sure? [y/n]")
		if a == "y":
			print "Goodbye.\nClosing now..."
			time.sleep(2.5)
			exit()

	if words[0] in h:
		print "Acadaemia:\nUse `look` or `examine` to `see` things."
		print "Type {north, south, east, or west} to move in those directions."
		print "Use `inventory` to list items in your inventory [Not yet implemented]."
		print "`exit` will exit the game."
		done = True

	if done == False:
		x = random.random()
		if x < 0.95:
			print "Not a command."
		else:
			print "I'm sure you're trying your best to come up with original commands, but I'll have you know your last input was complete gibberish."
