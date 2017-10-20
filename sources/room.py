import json
import os
import numpy as np

def getRoom(n):

    c = os.path.dirname(os.path.realpath(__file__))
    o = open(os.path.join(c,'rooms/')+str(n)+'.json', 'r')
    txt = o.read()
    roomdic = json.loads(txt)
    r = Room(**roomdic)
    return r

o_furniture = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'furniture.json'))
txt = o_furniture.read()
furnituredic = json.loads(txt)

class Room:
    def __init__(self, n, name, description, size, furniture, state, neighbors):

        self.n = n
        self.name = name
        self.description = description
        self.size = size
        self.furniture = furniture
        self.state = state
        self.neighbors = neighbors

        o_furniture = open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'furniture.json'))
        txt = o_furniture.read()
        self.furnituredic = json.loads(txt)

        self.grid = np.zeros(self.size)

    def furnish_room(self):

        for f in self.furniture:
            name = f[0]
            shape = furnituredic[name]
            # populate the self.grid with furniture items