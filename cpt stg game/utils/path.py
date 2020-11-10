#IMPORTENT!: YOU NEED NUMPY, MATPLOTLIB TO RUN THIS FILE

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation # testing
import math


sqrt = math.sqrt
log = math.log
pow = math.pow


class B2Curve(object):
    """A mathematical curve used to calculate the trajectory of bullets
    Variables:
        ∆d: change in distance
        steps: distance
        array: the array
        p0, p1, p2: three points forming the curve
    
    """

    def __init__(self, points, ctype="equal"):
        self.points = points
        self.ctype = "equal"

        self.delta_d = 0
        self.steps = 0
        self.array = None

        self.p0 = points[0]
        self.p1 = points[1]
        self.p2 = points[2]

        a = self.p0 - 2*self.p1 + self.p2
        b = 2*(self.p1 -self.p0)

        self.A = 4*(a[0]**2 + a[1]**2)
        self.B = 4*(a[0]*b[0] + a[1]*b[1])
        self.C = a[1]**2 + b[1]**2

    def __getitem__(self, key):
        """A getter to find an item in the array"""
        if key >= self.steps:
            key = self.steps-1

        return self.array[key]

    def set_up(self, delta_d=0, steps=0):
        if self.ctype == "equal" and delta_d != 0:
            self.delta_d = delta_d
            self.steps = int(self.L(1)/delta_d)
        elif self.ctype == "unequal":
            self.steps = int(steps)
            self.delta_d = round(L(1)/steps)
        
        self.set_array()
    
    def set_type(self, ctype):
        if ctype == "equal":
            self.ctype = "equal"
        elif ctype == "unequal":
            self.ctype = "unequal"
        else:
            self.ctype = "equal" 
        
        self.set_array()

    def C(self, t):
        """Curve function"""  # 曲线函数
        return ((1 - t)**2)*self.p0 + (2*t)*(1 - t)*self.p1 + (t**2)*self.p2

    def S(self, t): 
        """Velocity function"""  # 速度函数
        return sqrt(self.A*t*t+self.B*t+self.C);

    def L(self, t): 
        """Lenth function"""  # 长度函数
        temp1 = sqrt(self.C+t*(self.B+self.A*t))
        temp2 = (2*self.A*t*temp1+self.B*(temp1-sqrt(self.C)))
        temp3 = log(self.B+2*sqrt(self.A)*sqrt(self.C))
        temp4 = log(self.B+2*self.A*t+2*sqrt(self.A)*temp1)
        temp5 = 2*sqrt(self.A)*temp2
        temp6 = (self.B*self.B-4*self.A*self.C)*(temp3-temp4)
        
        return (temp5 + temp6)/(8*pow(self.A, 1.5))
    
    def I(self, t, l): 
        """Newton's method"""  # 近似反函数 （牛顿切线计算)
        t1 = t
        while True:
            t2 = t1 - (self.L(t1)-l)/self.S(t1)
            if abs(t1 - t2) < 0.00001:
                break
            t1 = t2
        
        return t2
    
    def set_array(self):
        i = 0
        self.array = np.zeros((self.steps, 2))
        for i in range(self.steps):
            t = i/self.steps

            if self.ctype == "equal":
                l = t*self.L(1)

                t = self.I(t, l)

            v = (1-t)*(1-t)*self.p0 +2*(1-t)*t*self.p1 + t*t*self.p2

            np.rint(v)

            self.array[i] = v

    def show(self):
        def run(i):
            art1.set_data(x_dots12[i], y_dots12[i])
            art2.set_data(x_dots23[i], y_dots23[i])
            art3.set_data([x_dots12[i], x_dots23[i]], [y_dots12[i], y_dots23[i]])
            #art4.set_data(xt[i], yt[i])
            art4.set_data(self[i][0], self[i][1])
            pxt = xt[i]
            pyt = yt[i]
            return art1,art2,art3,art4

        fig, ax = plt.subplots(figsize=(8,8))
        ax.set_aspect(1)
        plt.xlim(0,1024*3/4)
        plt.ylim(0,1024*0.95)
        x1, x2 ,x3 = self.p0[0], self.p1[0], self.p2[0]
        y1, y2, y3 = self.p0[1], self.p1[1], self.p2[1]
        xt = self.array[:, 0]
        yt = self.array[:, 1]
        x_dots12 = np.linspace(self.p0, self.p1, self.steps)[:, 0]
        y_dots12 = np.linspace(self.p0, self.p1, self.steps)[:, 1]
        x_dots23 = np.linspace(self.p1, self.p2, self.steps)[:, 0]
        y_dots23 = np.linspace(self.p1, self.p2, self.steps)[:, 1]
        ax.plot([x1, x2], [y1, y2], color='#3e82fc')
        ax.plot([x2, x3], [y2, y3], color='#3e82fc')
        ax.plot(xt,yt,color='orange')
        art1, = ax.plot(x_dots12[0], y_dots12[0], color='green', marker='o') 
        art2, = ax.plot(x_dots23[0], y_dots23[0], color='green', marker='o') 
        art3, = ax.plot([x_dots12[0], x_dots23[0]], [y_dots12[0], y_dots23[0]], color = 'purple')
        art4, = ax.plot(xt[0], yt[0], color='red', marker='o')

        ani = animation.FuncAnimation(
            fig, run, frames=range(self.steps), interval=1000/60, blit=True, save_count=50)
        plt.show()


    @staticmethod
    def test_curve(points=np.array([[100, 1.0], [100 ,250.0], [400, 500.0]]), ctype="equal", delta_d=5, steps=100):
        curve = B2Curve(points, ctype)
        curve.set_up(delta_d, steps)
        curve.show()


class B1Line(object):
    """A line"""

    def __init__(self, points, delta_d):
        self.points = points

        self.delta_d = delta_d
        
        self.array = None
        self.vel = None

        self.p0 = points[0]
        self.p1 = points[1]

        self.steps = int(self.L()/delta_d)

        self.set_array()


    def __getitem__(self, key):
        if key >= self.steps:
            key = self.steps-1

        return self.array[key]


    def C(self, t): # 曲线函数
        return self.p0 + (self.p1 - self.p0)*t
    
    def L(self):
        return sqrt((self.p0[0] - self.p1[0])**2 + (self.p0[1] - self.p1[1])**2)
        
    def set_array(self):
        dx = (self.p1[0]-self.p0[0])/self.steps
        dy = (self.p1[0]-self.p0[0])/self.steps
        self.vel = np.array([dx, dy])
        i = 0
        self.array = np.zeros((self.steps, 2))
        for i in range(self.steps):
            self.array[i] = self.p0 + i*np.array([dx, dy]) 
