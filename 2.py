import numpy as np
import matplotlib.pyplot as plt
from functions import medhod_progonki


def solve(n):
    a = 0.9
    b = 1.2

    # Краевые условия
    q = -0.5
    f = 2

    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)

    A = np.zeros(n)
    B = np.zeros(n)
    C = np.zeros(n)
    D = np.zeros(n)

    for i in range(1, n - 1):
        A[i] = 1 / h ** 2 - x[i] / (2 * h)
        B[i] = -2 / h ** 2 + 2
        C[i] = 1 / h ** 2 + x[i] / (2 * h)
        D[i] = x[i]

    # Левое краевое условие: y(0.9) - 0.5 y'(0.9) = 2
    # Когда подставим аппроксимацию, получим вот это: y[0] - 0.5((y[1] - y[0]) / h) = 2
    # Упрощая получим это: y[0](1+0.5/h) - y[1](0.5/h) = 2
    B[0] = 1 - q / h    # после значения функции нулевого узла
    C[0] = q / h        # после значения функции первого узла
    D[0] = f            # правая часть это 2

    # Правое краевое условие: y(1.2) = 1
    # Когда подставим аппроксимацию, получим вот это: y[-1] = 1
    B[-1] = 1           # при y [-1]
    D[-1] = 1           # правая часть это 1

    y = medhod_progonki(A, B, C, D)

    return x, y


x10, y10 = solve(10)
x50, y50 = solve(50)
x100, y100 = solve(100)

plt.figure(figsize=(10, 6))
plt.plot(x10, y10, 'o-', label='10 узлов', markersize=4)
plt.plot(x50, y50, 's-', label='50 узлов', markersize=2, alpha=0.7)
plt.plot(x100, y100, '^-', label='100 узлов', markersize=2, alpha=0.7)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Решение краевой задачи методом конечных разностей')
plt.legend()
plt.grid(True)
plt.show()


