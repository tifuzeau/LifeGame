
import time
import random

from cell import Cell, Life

class Body(Life):
    """
    Attributes
    ----------

    name : str
        name of this body

    x : int
        x size
    y : int
        y size

    _lifecell : int
        nb_of_cell_in_live

    body : arry
        map of Cell

    Methods
    -------

    _initbody()
        init body var

    ReSetBody()
        creat all cell en link togeder

    showbody()
        to show your body

    cycle_of_life()
        to see life append. test next_life() and timetodie()

    reset()
        reset the body

    move_body()
        to run life

    """
    body = []
    name = ""

    def __init__(self, x, y, name="Life"):
        Life.__init__(self)
        self.name = name
        self.x = x
        self.y = y
        self.body = [
            [Cell(x, y) for x in range(self.x)] for y in range(self.y)
        ]
        self.NeighborLink()
        self.ILive()

    def NeighborLink(self):
        for y in range(self.y):
            for x in range(self.x):
                neighbor = {}
                if x - 1 >= 0 and y + 1 < self.y:
                    neighbor.update({'topleft' : self.body[y + 1][x - 1]})
                if y + 1 < self.y:
                    neighbor.update({'top' : self.body[y + 1][x]})
                if x + 1 < self.x and y + 1 < self.y:
                    neighbor.update({'topright' : self.body[y + 1][x + 1]})
                if x - 1 >= 0:
                    neighbor.update({'left' : self.body[y][x - 1]})
                if x + 1 < self.x:
                    neighbor.update({'right' : self.body[y][x + 1]})
                if x - 1 >= 0 and y - 1 >= 0:
                    neighbor.update({'botleft' : self.body[y - 1 ][x - 1]})
                if y - 1 >= 0:
                    neighbor.update({'bot' : self.body[y - 1][x]})
                if x + 1 < self.x and y - 1 >= 0:
                    neighbor.update({'botright' : self.body[y - 1][x + 1]})
                self.body[y][x].Link(neighbor)

    def ReSetBody(self):
        self.lifetime = 0
        for y in range(self.y):
            for x in range(self.x):
                    self.body[y][x].Kill()

    def CycleOfLife(self):
        for y in range(self.y):
            for x in range(self.x):
                self.body[y][x].SeeNextLife()
        for i in range(self.y):
            for j in range(self.x):
                self.body[i][j].TimeToDie()
        self.lifetime += 1

    def _manilife(self):
        self._lifecell = 0
        for y in range(self.y):
            for x in range(self.x):
                if self.body[y][x].ILive():
                    self._lifecell += 1
        if self._lifecell > 0:
            self.life = True

    def ILive(self):
        self._manilife()
        if self._lifecell > 0:
            return True
        return False

    def ReSet(self):
        self.lifetime = 0
        self.ReSetBody()
        self._manilife()


    def ShowBody(self):
        self._manilife()
        to_print = "\t\t" + self.name
        to_print += "cycle n: "
        to_print += str(self.lifetime) + '\n'
        map_n = ""
        to_print += "live stat: " + str(self.ILive()) + '\t'
        to_print += "Cell in live: " + str(self._lifecell) + '\n'
        for y in range(self.y):
            for x in range(self.x):
                if self.body[y][x].ILive():
                    to_print += '#'
                    map_n += self.body[y][x].ShowNeighbor()
                else:
                    to_print += '.'
            to_print += '\n'
        #to_print += map_n
        to_print += 'End of cycle\n'
        return to_print

    def printbody(self):
        print("\033c")
        print(self.ShowBody())

    def MoveBody(self, maxcycle=-1, movespeed=0.20):
        while self.ILive() == True:
            self.CycleOfLife()
            self.printbody()
            time.sleep(movespeed)
            if maxcycle != -1 and self.lifetime > maxcycle:
                break

