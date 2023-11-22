from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

from minimizer.test_functions import ENERGY_SURFACES


def setup_pse(function, lower: int = -5, upper: int = 5, steps: int = 250,
                  cmap='viridis_r',
                  ):
    x = np.linspace(lower, upper, steps)
    y = np.linspace(lower, upper, steps)
    XY = X, Y = np.meshgrid(x, y)
    Z = function(XY)
    fig, ax = plt.subplots()

    k = np.arange(0, 20)
    levels = np.sqrt(k)*np.exp(0.5*k)
    levels = levels[~(levels > Z.max())]
    
    cmap = plt.cm.get_cmap(cmap)
    ax.contourf(X, Y, Z, levels=levels, alpha=0.8, cmap=cmap, norm=colors.SymLogNorm(1))
    ax.set_xlim(lower, upper)
    ax.set_ylim(lower, upper)

    return fig, ax


def main():
    parser = ArgumentParser()
    parser.add_argument('--function', default='himmelblau', type=str)

    args = parser.parse_args()
    function = ENERGY_SURFACES[args.function]
    setup_pse(function)
    plt.show()


if __name__ == '__main__':
    main()
