import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib import animation


class GradientDescent:
    def __init__(self, function, x, gamma):
        self.fn = function
        self.x = x
       
        self.gamma = gamma
        self.eps = 1e-8

        self.points = np.array(x)
        self.value = function(x)
        self.steps = [self.points]

    def __call__(self, max_iter):
        for i in range(max_iter):
            # gradient
            grad = optimize.approx_fprime(self.points, self.fn, self.eps)
            if np.allclose(0, grad, rtol=self.eps):
                break

            self.points = self.points - self.gamma*grad
            self.steps.append(self.points)
        
        return i
    
    @property
    def min(self):
        return {'point': self.points,
                'value': self.fn(self.points),
                }
    
    def animate(self, fig, **kwargs):
        # xs, ys = zip(*self.steps)
        # gradient = [plt.plot(xs[i+2:i:-1], ys[i+2:i:-1], color='tab:red') for i in range(len(xs)-2)]
        gradient = [[plt.arrow(*self.steps[i], *(self.steps[i+1]-self.steps[i]), 
                               color='tab:red',
                               head_width=0.05,
                               length_includes_head=True,
                               )]
                        for i in range(len(self.steps)-1)]
        gradient.append(plt.plot(*self.points, 'o', color='tab:green'))
        anim = animation.ArtistAnimation(fig, gradient, **kwargs)
        return anim

