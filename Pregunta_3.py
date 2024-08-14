
import matplotlib.pyplot as plt
import numpy as np
from src import ajustar_min_cuadrados

def der_parcial_2(xs: list, ys: list) -> tuple[float, float, float, float]:
    c_2 = sum(xi**4 for xi in xs)
    c_1 = sum(xi**3 for xi in xs)
    c_0 = sum(xi**2 for xi in xs)
    c_ind = sum(yi * xi**2 for yi, xi in zip(ys, xs))
    return (c_2, c_1, c_0, c_ind)

def der_parcial_1(xs: list, ys: list) -> tuple[float, float, float, float]:
    c_2 = sum(xi**3 for xi in xs)
    c_1 = sum(xi**2 for xi in xs)
    c_0 = sum(xi for xi in xs)
    c_ind = sum(yi * xi for yi, xi in zip(ys, xs))
    return (c_2, c_1, c_0, c_ind)

def der_parcial_0(xs: list, ys: list) -> tuple[float, float, float, float]:
    c_2 = sum(xi**2 for xi in xs)
    c_1 = sum(xi for xi in xs)
    c_0 = len(xs)
    c_ind = sum(ys)
    return (c_2, c_1, c_0, c_ind)

def funcion_cuadratica(x: float, pars: tuple[float, float, float]) -> float: 
    a2, a1, a0 = pars
    return a2*x**2 + a1*x + a0

xs = [
    1.1715,
    1.3396,
    1.4163,
    1.9962,
    2.2523,
    2.2947,
    2.5793,
    2.7054,
    2.7635,
    2.8200,
    3.0317,
    3.5111,
    3.5393,
    3.9829,
    4.0323,
    4.1353,
    4.2084,
    4.4683,
    4.6509,
    4.7489,
]

ys = [
    1.1902,
    0.9564,
    0.6078,
    -0.0856,
    -0.3550,
    0.1355,
    -0.3171,
    -0.3425,
    -0.3758,
    -0.1518,
    -0.2767,
    0.6251,
    0.6447,
    2.2733,
    2.1789,
    2.6781,
    2.3818,
    3.3786,
    4.4971,
    5.1431,
]

pars1 = ajustar_min_cuadrados(xs, ys, gradiente = [der_parcial_2, der_parcial_1, der_parcial_0])

x = np.linspace(-5, 5, 100)
y = [funcion_cuadratica(xi, pars1) for xi in x]

plt.scatter(xs, ys, label="Datos")
plt.plot(x, y, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Mínimos cuadrados")
plt.legend()
plt.show()

# Error cuadrado
error_relativo = np.mean([abs(y_real - funcion_cuadratica(x_real, pars1))/abs(y_real) for y_real, x_real in zip(ys, xs)])
print(f"El error relativo es {error_relativo}")

# Ecuacion lineal
def der_parcial_lin_1(xs: list, ys: list) -> tuple[float, float, float]:
    c_ind = sum(ys)
    c_1 = sum(xs)
    c_0 = len(xs)
    return (c_1, c_0, c_ind)


def der_parcial_lin_0(xs: list, ys: list) -> tuple[float, float, float]:
    c_1 = 0
    c_0 = 0
    c_ind = 0
    for xi, yi in zip(xs, ys):
        c_ind += xi * yi
        c_1 += xi * xi
        c_0 += xi
    return (c_1, c_0, c_ind)

def funcion_lineal(x: float, pars: tuple[float, float]) -> float:
    a1, a0 = pars
    return a1*x + a0

pars2 = ajustar_min_cuadrados(xs, ys, gradiente = [der_parcial_lin_0, der_parcial_lin_1])

x = np.linspace(-5, 5, 100)
y = [funcion_lineal(xi, pars2) for xi in x]

plt.scatter(xs, ys, label="Datos")
plt.plot(x, y, color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Mínimos cuadrados")
plt.legend()
plt.show()

# Error lineal
error_relativo = np.mean([abs(y_real - funcion_lineal(x_real, pars2))/abs(y_real) for y_real, x_real in zip(ys, xs)])
print(f"El error relativo es {error_relativo}")
