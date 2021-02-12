# coding: utf8
# lang: python 3

import time
import random

class Life():
    """

    Attributes
    ----------

    life : boolean
        True is a live

    life_time : int
        updtime of life


    Methods
    -------

    Ilive()
        return life

    Kill()
        to kill life

    Rise()
        to rise life

    """
    life = False
    lifetime = 0

    def __init__(self):
        self.life = False
        self.lifetime = 0

    def ILive(self):
        return self.life

    def Kill(self):
        self.lifetime = 0
        self.life = False

    def Rise(self):
        self.life = True
        self.lifetime += 1


class Cell(Life):
    """

    Attributes
    ----------

    _nextlife : boolean
        is live in end of cycle

    neighbor : arry
       arry of 8 neighbor


    Methods
    -------

        Pos()
            for debug return pos of cell

        Link(cell_voisine)
            link current cell to neighbor

        SeeNextLife()
            set _nextlife

        TimeToDie()
            call kill if _nextlife = False and more

        ShowNeighbor()

    """
    _nextlife = False
    neighbor = {}

    def __init__(self, x, y):
        Life.__init__(self)
        self.x = x
        self.y = y

    def Kill(self):
        Life.Kill(self)
        self._nextlife = False

    def Rise(self):
        Life.Rise(self)
        self._nextlife = True

    def Pos(self):
        return "X: " + str(self.x)+ " Y: " + str(self.y) + '\n'

    def Link(self, neighbor):
        self.neighbor = neighbor

    def SeeNextLife(self):
        neighbor_life = 0
        for cell in self.neighbor:
            if self.neighbor[cell].ILive():
                neighbor_life += 1
        if self.ILive() == False and neighbor_life == 3:
                self._nextlife = True
        elif neighbor_life != 2 and neighbor_life != 3:
            self._nextlife = False

    def TimeToDie(self):
        if self._nextlife == True:
            self.Rise()
        else:
            self.Kill()

    def ShowNeighbor(self):
        """
            return map of neighbor
        """
        show = "\nI" + self.Pos()
        for cell in self.neighbor:
            show += cell + " : "
            show += self.neighbor[cell].Pos() + "\n"
        show += "End My\n"
        return show

