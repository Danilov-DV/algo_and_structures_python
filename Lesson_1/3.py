# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

X1 = int(input('X1: '))
Y1 = int(input('Y1: '))
X2 = int(input('X2: '))
Y2 = int(input('Y2: '))

VAR_K = (Y2 - Y1) / (X2 - X1)
VAR_B = Y1 - VAR_K * X1

print(f"уравнение прямой: y = {VAR_K}x + {VAR_B}")