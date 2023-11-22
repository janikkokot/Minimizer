import matplotlib.pyplot as plt

import minimizer.parser as p
from minimizer.test_functions import ENERGY_SURFACES
import minimizer.visualize as vis
import minimizer.simplex as simplex
import minimizer.gradient_descent as gd


algorithms_implemented = {
        'simplex': simplex.Simplex,
        'gradient_descent': gd.GradientDescent,
        }


def main():
    parser = p.get_parser('Minimization')
    args = parser.parse_args()
    try:
        algorithm = algorithms_implemented[args.algorithm.strip().lower()]
    except KeyError:
        raise ValueError(f'{args.algorithm!r} not recognized')
    function = ENERGY_SURFACES[args.function]
    alg = algorithm(function, args.start, args.beta)
    iterations = alg(args.max_iter)

    fig, ax = vis.setup_pse(function)
    ax.set_title(args.function.title())
    fig.canvas.manager.set_window_title(args.algorithm.strip().title())
    anim = alg.animate(fig, interval=500, blit=True, repeat=False)
    print(alg.min)
    print(f'{iterations=}')
    plt.show()


if __name__ == '__main__':
    main()
