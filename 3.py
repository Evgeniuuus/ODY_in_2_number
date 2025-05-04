import numpy as np
import matplotlib.pyplot as plt

phi0 = lambda x: 1
phi1 = lambda x: x
phi2 = lambda x: x ** 2

d_phi0 = lambda x: 0
d_phi1 = lambda x: 1
d_phi2 = lambda x: 2 * x

dd_phi0 = lambda x: 0
dd_phi1 = lambda x: 0
dd_phi2 = lambda x: 2


# Коллокационные точки берутся из интервала
x1 = 1.0
x2 = 1.1

A = np.zeros((4, 3))
b = np.zeros(4)

A[0, 0] = dd_phi0(x1) - x1 * d_phi0(x1) + 2 * phi0(x1)
A[0, 1] = dd_phi1(x1) - x1 * d_phi1(x1) + 2 * phi1(x1)
A[0, 2] = dd_phi2(x1) - x1 * d_phi2(x1) + 2 * phi2(x1)
b[0] = x1 + 1

A[1, 0] = dd_phi0(x2) - x2 * d_phi0(x2) + 2 * phi0(x2)
A[1, 1] = dd_phi1(x2) - x2 * d_phi1(x2) + 2 * phi1(x2)
A[1, 2] = dd_phi2(x2) - x2 * d_phi2(x2) + 2 * phi2(x2)
b[1] = x2 + 1

# y(0.9) - 0.5*y'(0.9) = 2
x_edge1 = 0.9
A[2, 0] = phi0(x_edge1) - 0.5 * d_phi0(x_edge1)
A[2, 1] = phi1(x_edge1) - 0.5 * d_phi1(x_edge1)
A[2, 2] = phi2(x_edge1) - 0.5 * d_phi2(x_edge1)
b[2] = 2

# y(1.2) = 1
x_edge2 = 1.2
A[3, 0] = phi0(x_edge2)
A[3, 1] = phi1(x_edge2)
A[3, 2] = phi2(x_edge2)
b[3] = 1

c, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

print("Найденные коэффициенты:", c)

x = np.linspace(0.9, 1.2, 100)
y = [c[0] * phi0(i) + c[1] * phi1(i) + c[2] * phi2(i) for i in x]

plt.plot(x, y, label='Решение методом коллокаций')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Решение краевой задачи')
plt.legend()
plt.grid()
plt.show()
