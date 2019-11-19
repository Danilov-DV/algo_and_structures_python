"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

N = int(input("Количество вводимых чисел "))
NUM = 0
SUM = 0

for I in range(N):
    VAR1 = VAR2 = int(input(f"{I+1} число "))
    VAR_SUM = 0
    while True:
        if VAR1 > 0:
            VAR_SUM += VAR1 % 10
            VAR1 = VAR1 // 10
        else:
            break
    if VAR_SUM > SUM:
        SUM = VAR_SUM
        NUM = VAR2

print(f"число - {NUM} сумма - {SUM}")
