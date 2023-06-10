import matplotlib.pyplot as pp
import numpy as np

def h (z):
    return np.sin(z)

x = list(range(0, 100, 1))

pp.plot(x,h(x))
pp.show()