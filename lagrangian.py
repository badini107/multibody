import math

class Lagrangian():
    def __init__(self, links):
        self.links = links

        self.links_vel2 = []

    def vel(self):
        for i, link in enumerate(self.links):
            x = link.ang_vel * link.length/2 * math.cos(link.angle)
            y = link.ang_vel * link.length/2 * math.sin(link.angle)
            for j in range(0, i):
                x += self.links[j].ang_vel * self.links[j].length/2 * math.cos(self.links[j].angle)
                y += self.links[j].ang_vel * self.links[j].length/2 * math.cos(self.links[j].angle)
            self.links_vel2 = x
            

    def T(self):
        for i, link in enumerate(self.links):
            self.T += self.link.mass * (self.link.ang_vel ** 2) * self.link.length/2
            for j in range(1, i):
                pass
    
    def energy(self):
        self.x = []
        self.y = []      
        for i, link in enumerate(self.links):
            self.x.append([{
                'const' : 0.5 * link.length,
                'theta' + str(i): 'sin'
            }])
            self.y.append([{
                'const' : -0.5 * link.length,
                'theta' + str(i): 'cos'
            }])
            for j in range(i):
                self.x[i].append({
                    'const' : 1 * self.links[j].length,
                    'theta' + str(j): 'sin'
                })
                self.y[i].append({
                    'const' : -1 * self.links[j].length,
                    'theta' + str(i): 'cos'
                })

    def square(self):
        self.x2 = []
        self.y2 = []  
        for i in range(len(self.x)):
            self.x2.append([])
            count  = 0
            for j in range(len(self.x[i])):
                for l in range(len(self.x[i])):
                    self.x2[i].append({})
                    for k, v in self.x[i][j].items():
                        added = 0
                        for k2, v2 in self.x[i][l].items():
                            if k == k2:
                                if k == 'const':
                                    if k in self.x2[i][j + l]:
                                        self.x2[i][j + l][k] += v * v2
                                    else:
                                        self.x2[i][j + l][k] = v * v2
                                elif v == v2:
                                    self.x2[i][j + l][k] = v + '2'
                                else:
                                    self.x2[i][j + l][k] = v + v2
                                added = 1
                                break
                        if not added:
                            if k in self.x2[i][j + l]:
                                self.x2[i][j + l][k] += v
                            else:
                                self.x2[i][j + l][k] = v

                    print(count, self.x2[i][j + l])
                    count += 1
               


