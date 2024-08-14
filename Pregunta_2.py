
from scipy.optimize import bisect
import matplotlib.pyplot as plt
import numpy as np

def funcion(x: float):
    return x**5 - 6*x**4 + 2*x**3 + 20*x**2 - 27*x + 10

x = range(-5, 10)

plt.plot(x , [funcion(i) for i in x])
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()

# Raiz 1
root = bisect(f = funcion, a = -10, b = 0)
print(root)

# Raiz 2
root2 = bisect(f = funcion, a = 0, b = 2)
print(root2)

# Raiz 3
root3 = bisect(f = funcion, a = 2, b = 5)
print(root3)

# No hay mas raices
