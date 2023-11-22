import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class Simplex:
# 1) order
# 2) centroid
# 3) reflect
# 4) expand
# 5) contract
# 6) shrink
    def __init__(self, function, x, *args, **kwargs):
        self.alpha = -1 # due to definition of update function
        self.gamma = 2
        self.rho = 0.5
        self.sigma = 0.5

        self.eps = 1e-8

        self.fn = function
        self.x = x

        points = [x]
        for _ in range(len(x)):
            points.append([y+random.random() for y in x])
        self.points = np.array(points)

        self.values = np.array([function(x) for x in self.points])

        self.steps = [self.points]

    def __call__(self, max_iter):
        for i in range(max_iter):
            # 1) order
            sorted_val = np.argsort(self.values)
            self.values = self.values[sorted_val]
            self.points = self.points[sorted_val]
            
            # 1b) check for termination
            if np.allclose(0, np.std(self.values), rtol=self.eps):
                break

            # 2) centroid
            assert len(self.points) - 1 == len(self.points[:-1])
            r_0 = np.average(self.points[:-1], axis=0)

            # 3) reflect
            highest = self.points[-1]
            r_reflect = update(highest, r_0, self.alpha)
            v_reflect = self.fn(r_reflect)
            
            # better but not best
            if self.values[0] <= v_reflect and v_reflect <= self.values[-2]:
                self.values[-1] = v_reflect
                self.points[-1] = r_reflect
            # best
            # 4) expand
            elif v_reflect < self.values[0]:
                r_exp = update(r_reflect, r_0, self.gamma)
                v_exp = self.fn(r_exp)
                self.values[-1] = v_exp if v_exp < v_reflect else v_reflect
                self.points[-1] = r_exp if v_exp < v_reflect else r_reflect
            # worse
            # 5) contract
            else:
                r_scnd = r_reflect if v_reflect < self.values[-1] else self.points[-1]
                v_scnd = v_reflect if v_reflect < self.values[-1] else self.values[-1]

                r_cont = update(r_scnd, r_0, self.rho)
                v_cont = self.fn(r_cont)
                if v_cont < v_scnd:
                    self.values[-1] = v_cont
                    self.points[-1] = r_cont
                # 6) shrink
                else:
                    best = self.points[0]
                    self.points = [update(r, best, self.sigma) for r in self.points]
                    self.values = [self.fn(r) for r in self.points]

            self.steps.append(self.points)
        return i
    
    @property
    def min(self):
        arg = np.argmin(self.values)
        return {'point' : self.points[arg],
                'value' : self.values[arg],
                }

    def animate(self, fig, **kwargs):
        def plot_vertix(vert, color='tab:red'):
            x, y= zip(*vert)
            x = list(x)
            y = list(y)
            x.append(x[0])
            y.append(y[0])
            return plt.plot(x, y, color=color)

        vertices = [plot_vertix(points) for points in self.steps]
        vertices.append(plt.plot(*self.min['point'], 'o', color='tab:green'))
        anim = animation.ArtistAnimation(fig, vertices, **kwargs)
        return anim


def update(point, ref_point, constant):
    return ref_point + constant * (point - ref_point)
