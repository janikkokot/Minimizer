def himmelblau(inp):
    x, y = inp
    first = x**2 + y - 11
    second = x + y**2 - 7
    return first**2 + second**2


def banana(inp):
    x, y = inp
    return (1-x)**2 + 100*(y-x**2)**2


def camel(inp):
    x, y = inp
    return 2*x**2 - 1.05*x**4 + x**6/6 + x*y + y**2


ENERGY_SURFACES = {
        'himmelblau': himmelblau,
        'banana': banana,
        'camel': camel,
        }
