import numpy as np


def check(a, b):
    res = a[0] - b[0]
    for i in range(len(a)):
        if a[i] - b[i] > res:
            res = a[i] - b[i]
    return res


def medhod_progonki(a, b, c, d):
    n = len(d)
    alpha = np.zeros(n)
    beta = np.zeros(n)

    # Прямой ход
    alpha[0] = -c[0] / b[0]
    beta[0] = d[0] / b[0]

    for i in range(1, n):      # Подставляем в рекурентные формулы
        alpha[i] = -c[i] / (b[i] + a[i] * alpha[i - 1])
        beta[i] = (d[i] - a[i] * beta[i - 1]) / (b[i] + a[i] * alpha[i - 1])

    # Обратный ход
    y = np.zeros(n)
    y[-1] = beta[-1]

    for i in range(n - 2, -1, -1):
        y[i] = alpha[i] * y[i + 1] + beta[i]

    return y