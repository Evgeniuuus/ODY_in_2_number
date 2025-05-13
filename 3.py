import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Eq, solve

phi0 = lambda x: 1.5 - 1.25 * x
phi1 = lambda x: -0.3 * (x - 0.9) ** 2 + (x - 0.9) ** 3

d_phi0 = lambda x: -1.25
d_phi1 = lambda x: 3 * (x ** 2 - 2 * x + 99 / 100)

dd_phi0 = lambda x: 0
dd_phi1 = lambda x: 6 * (x - 1)

# Середина интервала (Будет одна точка коллокации)
x1 = 1.05

c1_symbol = sp.Symbol('c1')

y1 = phi0(x1) + c1_symbol * phi1(x1)
d_y1 = d_phi0(x1) + c1_symbol * d_phi1(x1)
dd_y1 = dd_phi0(x1) + c1_symbol * dd_phi1(x1)

# y'' - x*y' + 2y = x + 1
equation = Eq(dd_y1 - x1 * d_y1 + 2 * y1, x1 + 1)

c1_solution = solve(equation, c1_symbol)

c1 = float(c1_solution[0])  # Преобразуем

print(f"Найденный коэффициент: {c1}")

x = np.linspace(0.9, 1.2, 100)

y = phi0(x) + c1 * phi1(x) + 1

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод коллокации')
plt.grid(True)
plt.show()

