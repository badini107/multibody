import math


class Link():
    def __init__(self, x0, y0, x1, y1, **kwargs):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.angle = self.get_angle()
        self.length = self.get_length()
        self.ang_acc = 0
        self.ang_vel = 0
        self.calc_cg()

        if 'mass' in kwargs:
            self.mass = kwargs['mass']
        else:
            self.mass = 1

        if 'damp' in kwargs:
            self.damp = kwargs['damp']
        else:
            self.damp = 0.5
        
        if 'inertia' in kwargs:
            self.inertia = kwargs['inertia']
        else:
            self.inertia = 200
        
        if 'ts' in kwargs:
            self.ts = kwargs['ts']
        else:
            self.ts = 0.01

        if 'gravity' in kwargs:
            self.g = kwargs['gravity']
        else:
            self.g = 10

    def get_angle(self):
        return math.atan2(-(self.y1 - self.y0), self.x1 - self.x0)
    
    def get_length(self):
        return math.sqrt((self.y1 - self.y0)**2 + (self.x1 - self.x0)**2)
    
    def calc_ang_acc(self):
        self.ang_acc = (self.x0 - self.cg_x) * self.mass *  self.g / self.inertia
    
    def calc_ang_vel(self):
        self.ang_vel += self.ts * self.ang_acc
        self.ang_vel *=(1 - self.damp*self.ts)
    
    def calc_angle(self):
        self.angle += self.ts * self.ang_vel

    def calc_cg(self):
        self.cg_x =  (self.x1 + self.x0) /2
        self.cg_y =  (self.y1 + self.y0) /2 

    
    def update(self):
        self.calc_ang_acc()
        self.calc_ang_vel()
        self.calc_angle()
        self.x1 = math.cos(self.angle) * self.length + self.x0
        self.y1 = math.sin(-self.angle) * self.length + self.y0
        self.calc_cg()

    def update_position(self, x, y):
        angle = math.atan2(-(y - self.y0), x - self.x0)
        self.x1 = math.cos(angle) * self.length + self.x0
        self.y1 = math.sin(-angle) * self.length + self.y0
        self.angle = self.get_angle()
        self.ang_acc = 0
        self.ang_vel = 0
        self.calc_cg()
