# compose.py

from functools import reduce

def composite_function(*functions):

    def compose(f, g):
        return lambda x : f(g(x))

    return reduce(compose, functions, lambda x: x)