from lagrangian import Lagrangian
import math



class Link():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.length =  math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        self.mass = 1

links = []
links.append(Link(0, 0, 1, 0))
links.append(Link(1, 0, 2, 0))
#links.append(Link(2, 0, 3, 0))

lag = Lagrangian(links)
lag.system()
lag.potential()
#print(lag.potential_energy)
print(lag.x)
print(lag.y)
dtx = lag.derivate(lag.x,'t')
dtx2 = lag.square(dtx)
dty = lag.derivate(lag.y,'t')
#print(dty)
dty2 = lag.square(dty)
#print(dty2)
sum_dt = dtx2 + dty2
add_dt = lag.addition(sum_dt)
print(add_dt)
