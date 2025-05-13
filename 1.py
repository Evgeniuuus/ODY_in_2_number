import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
from functions import medhod_progonki, check


correct_f1 = lambda x: x ** 2
p1 = lambda x: x
q1 = lambda x: -2
f1 = lambda x: 2


a = 0
b = 1

n = 11  # Количество узлов (10 интервалов)

h = (b - a) / (n - 1)
x = np.linspace(a, b, n)

print("Шаг равен:", h)

A = np.zeros(n - 2)  # Нижняя диагональ
B = np.zeros(n - 2)  # Главная
C = np.zeros(n - 2)  # Верхняя
D = np.zeros(n - 2)  # Правая часть

# Коэффициенты тридиагональной матрицы
for i in range(1, n - 1):
    xi = x[i]

    a_i = 1 / h ** 2 - p1(xi) / (2 * h)
    b_i = -2 / h ** 2 + q1(xi)
    c_i = 1 / h ** 2 + p1(xi) / (2 * h)
    d_i = f1(xi)

    # Это из разностного уравнения
    if i == 1:
        d_i -= a_i * 0  # y[0] = 0  для первого узла
    elif i == n - 2:
        d_i -= c_i * 1  # y[n-1] = 1    для последнего

    if i < n - 1:
        A[i - 1] = a_i
        B[i - 1] = b_i
        C[i - 1] = c_i
        D[i - 1] = d_i

y_pr = medhod_progonki(A, B, C, D)

y_num = np.zeros(n)

y_num[0] = 0  # Граничные условия
y_num[-1] = 1

y_num[1:-1] = y_pr  # Внутренность

y_correct = correct_f1(x)
error = np.zeros(n)

for i in range(n):
    error[i] = abs(y_num[i] - y_correct[i])

plt.figure(figsize=(10, 6))
plt.plot(x, y_num, 'bo-', label='Численное решение')
plt.plot(x, y_correct, 'r--', label='Точное решение')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()

table_data = []
for i in range(len(x)):
    table_data.append([
        f"{x[i]:.2f}",
        f"{y_num[i]:.10f}",
        f"{y_correct[i]:.10f}",
        f"{error[i]:.5f}",
    ])

headers = ["x", "Численное решение", "Точное значение", "Погрешность"]

print(tabulate(table_data, headers=headers, tablefmt="grid"))

print(check(y_num, y_correct))

