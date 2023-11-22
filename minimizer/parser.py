from argparse import ArgumentParser


def get_parser(name):
    parser = ArgumentParser(prog =name)
    parser.add_argument('algorithm', type=str, default='simplex')
    parser.add_argument('--start', nargs=2, type=float, default=[0, 0])
    parser.add_argument('--beta', type=float, default=5e-3)
    parser.add_argument('--max_iter', default=100, type=int)
    parser.add_argument('--function', default='himmelblau', type=str)
    return parser
