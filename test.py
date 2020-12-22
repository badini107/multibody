from lagrangian import Lagrangian
import math


class Link():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.length =  math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

links = []
links.append(Link(0, 0, 1, 0))
links.append(Link(1, 0, 2, 0))
#links.append(Link(2, 0, 3, 0))

lag = Lagrangian(links)
lag.energy()
print(lag.x)
print(lag.square(lag.x))
print(lag.y)
print(lag.square(lag.y))
