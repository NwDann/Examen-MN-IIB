
import numpy as np
from src import matriz_aumentada

def gauss_jordan(Ab: np.ndarray) -> np.ndarray:
    if not isinstance(Ab, np.ndarray):
        Ab = np.array(Ab)
    n = round(Ab.shape[0] / 2)

    for i in range(0, n):  # loop por columna

        # --- encontrar pivote
        p = None  # default, first element
        for pi in range(i, n):
            if Ab[pi, i] == 0:
                # must be nonzero
                continue

            if p is None:
                # first nonzero element
                p = pi
                continue

            if abs(Ab[pi, i]) < abs(Ab[p, i]):
                p = pi

        if p is None:
            # no pivot found.
            raise ValueError("No existe solución única.")

        if p != i:
            # swap rows
            _aux = Ab[i, :].copy()
            Ab[i, :] = Ab[p, :].copy()
            Ab[p, :] = _aux

        # --- Eliminación: loop por fila
        for j in range(n):
            if i == j:
                continue
            m = Ab[j, i] / Ab[i, i]
            Ab[j, i:] = Ab[j, i:] - m * Ab[i, i:]


    if Ab[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    # --- Sustitución hacia atrás
    solucion = np.zeros(n)

    for i in range(n - 1, -1, -1):
        solucion[i] = Ab[i, -1] / Ab[i, i]

    return Ab

def inv_matrix(A: np.ndarray) -> np.ndarray:
    """Inversión de una matriz cuadrada mediante método de Gauss-Jordan.
    ## Parameters
    ``A``: matriz cuadrada de tamaño n x n.

    ## Return
    ``A_inv``: matriz inversa de A.
    """
    # COMPLETAR
    # Debe basarse en la función gauss_jordan
    A_inv = gauss_jordan(matriz_aumentada(A, np.identity(len(A))))
    return A_inv

A = [
    [1, 2, 3, 4],
    [2, 5, 6, 7],
    [3, 6, 8, 9],
    [4, 7, 9, 10],
]
resp1 = inv_matrix(A)
print(resp1)
