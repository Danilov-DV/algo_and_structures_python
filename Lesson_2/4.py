"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

N = int(input("Количество элементов (n) "))
SUM = 0
for i in range(N):
    el = 1 / (2 ** i)
    if (i + 1) % 2 == 0:
        el = - el
    SUM += el

print(SUM)
