import math

derivate_table = {
    'sin' : 'cos',
    'cos' : '-sin'
}

class Lagrangian():
    def __init__(self, links):
        self.links = links
        self.g = 10
    
    def system(self):
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
                    'theta' + str(j): 'cos'
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

    def derivate(self, expression, derivator):
        expression_d = []
        if derivator == 't':
            for i in range(len(expression)):
                expression_d.append([])
                for j in range(len(expression[i])):
                    exp = {}
                    for k, v in expression[i][j].items():
                        if k == 'const':
                            exp[k] = v
                        else:
                            if derivate_table[v][0] == '-':
                                exp['const'] *= -1
                                exp[k] = derivate_table[v][1:]
                            else:
                                exp[k] = derivate_table[v]
                            exp[k + "'"] = '1'
                    expression_d[i].append(exp)

            return expression_d
    
    def addition(self, expression):
        expression_add = []
        for i in range(len(expression)):
            expression_add.append([])
            for j in range(len(expression[i])):
                if not expression[i][j] in expression_add[i]:
                    expression_add[i].append(expression[i][j])
                else:
                    expression_add[i].remove(expression[i][j])
                    exp = expression[i][j]
                    exp['const'] += 1
                    expression_add[i].append(exp)

        return expression_add

    def potential(self):
        self.potential_energy = []
        pot = []
        for i, link in enumerate(self.links):
            pot.append({
                'const' : 0.5 * link.mass * self.g * link.length,
                'theta' + str(i): 'cos'
            })
            for j in range(i):
                pot.append({
                    'const' : self.links[j].mass * self.g * self.links[j].length,
                    'theta' + str(j): 'cos'
                })
        self.potential_energy.append(pot)
    
    def kinetic(self, velocity):
        self.kinetic_energy = []
        kin = []
        for i, bodys in enumerate(velocity):
            for vel in bodys:
                exp = vel
                exp['const'] *= 0.5 * self.links[i].mass
                kin.append(exp)
                
        self.kinetic_energy.append(kin)

                
                

                    
               


