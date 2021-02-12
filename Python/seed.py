# coding: utf8
# lang: python 3

from body import Body

class Seed(Body):
    """
    Attributes
    ----------
    """
    name = ""
    seed = []

    def __init__(self, x, y, name, seed):
        Body.__init__(self, x, y, name)
        self.seed = seed
        self.CreatBody(seed)
        self.Rise()


    def CreatBody(self, seed):
        if self._checkseed(seed) == False:
            print("FAILLLLLLLLLLLLLLLLLLLL")
        self.ReSetBody()
        ly = len(seed)
        lx_max = 0
        for y in range(ly):
            if len(seed[y]) > lx_max:
                lx_max = len(seed[y])
        x_start = int(self.x / 2) - int(lx_max / 2)
        y_start = int(self.y / 2) - int(ly / 2)
        for i in range(ly):
            for x in range(len(seed[i])):
                if seed[i][x] == 1:
                    self.body[y_start + i][x_start + x].Rise()

    def _checkseed(self, seed):
        if self.y < len(seed):
            return False
        for y in range(len(seed)):
            if self.x < len(seed[y]):
                return False
        return True
