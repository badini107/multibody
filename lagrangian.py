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

    def square(self, expression):
        expression_sqr = []
        for i in range(len(expression)):
            expression_sqr.append([])
            for j in range(len(expression[i])):
                for l in range(j, len(expression[i])):
                    exp = {}
                    if j == l:
                        for k, v in expression[i][j].items():
                            if isinstance(v, str):
                                exp[k] = v + '2'
                            else:
                                exp[k] = v ** 2
                    else:
                        for k, v in expression[i][j].items():
                            if k in expression[i][l].keys():
                                if k == 'const':
                                    exp[k] = 2 * v * expression[i][l][k]
                                elif v == expression[i][l][k]:
                                    exp[k] = v + '2'
                                else:
                                    exp[k] = v + expression[i][l][k]
                            else:
                                exp[k] = v

                        for k, v in expression[i][l].items():
                            if not k in expression[i][j].keys():
                                exp[k] = v
                    expression_sqr[i].append(exp)
        
        return expression_sqr
                
                

                    
               


