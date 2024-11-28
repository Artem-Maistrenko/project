# Дано вещественное число X и целое число N (> 0).
# Найти значение выражения 1 + X + X^2/(2!) + ... + X^N/(N!) (N! = 12 ...N).
# Полученное число является приближенным значением функции exp в точке X.

import math

def approximate_exp(X, N):
    try:
        if N <= 0: raise ValueError("N должно быть больше 0")
        result, term = 1.0, 1.0
        for i in range(1, N + 1):
            term *= X / i
            result += term
        return result
    except Exception as e:
        return f"Ошибка: {e}"

X = float(input("Введите число X: "))
N = int(input("Введите число N (> 0): "))

print(approximate_exp(X, N))
