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
            self.y2.append([])
            for j in range(len(self.x[i])):
                for l in range(j, len(self.x[i])):
                    expression_x = {}
                    expression_y = {}
                    if j == l:
                        for k, v in self.x[i][j].items():
                            if isinstance(v, str):
                                expression_x[k] = v + '2'
                            else:
                                expression_x[k] = v ** 2

                        for k, v in self.y[i][j].items():
                            if isinstance(v, str):
                                expression_y[k] = v + '2'
                            else:
                                expression_y[k] = v ** 2
                    else:
                        for k, v in self.x[i][j].items():
                            if k in self.x[i][l].keys():
                                if k == 'const':
                                    expression_x[k] = 2 * v * self.x[i][l][k]
                                elif v == self.x[i][l][k]:
                                    expression_x[k] = v + '2'
                                else:
                                    expression_x[k] = v + self.x[i][l][k]
                            else:
                                expression_x[k] = v

                        for k, v in self.x[i][l].items():
                            if not k in self.x[i][j].keys():
                                expression_x[k] = v
                                
                        for k, v in self.y[i][j].items():
                            if k in self.y[i][l].keys():
                                if k == 'const':
                                    expression_y[k] = 2 * v * self.y[i][l][k]
                                elif v == self.y[i][l][k]:
                                    expression_y[k] = v + '2'
                                else:
                                    expression_y[k] = v + self.y[i][l][k]
                            else:
                                expression_y[k] = v

                        for k, v in self.y[i][l].items():
                            if not k in self.y[i][j].keys():
                                expression_y[k] = v

                    self.x2[i].append(expression_x)
                    self.y2[i].append(expression_y)
                
                

                    
               


