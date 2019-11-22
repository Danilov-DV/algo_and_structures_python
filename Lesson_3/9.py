# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
N = 4
M = 5

EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(1, 50))
    EXT_LST.append(b)


for i in range(M):
    s = "    "
    for j in range(N):
        s += f"{EXT_LST[j][i]:4d}"
    print(s)

print(f"    ", end='')
for i in range(N):
    print(f"  --", end='')
print()


MIN_LIST = []
S = "min:"
for i in range(N):
    S += f"{min(EXT_LST[i]):4d}"
    MIN_LIST.append(min(EXT_LST[i]))
print(S)
print()
print(f"максимальный элемент среди минимальных элементов столбцов матрицы - {max(MIN_LIST)}")