"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

VAR_INT = int(input("введите число "))

COUNTER1 = 0
COUNTER2 = 0
STR1 = ""
STR2 = ""

while True:
    if VAR_INT > 0:
        NUM = VAR_INT % 10
        if NUM % 2:
            COUNTER1 += 1
            STR1 += str(NUM) + " "
        else:
            COUNTER2 += 1
            STR2 += str(NUM) + " "
        VAR_INT = VAR_INT // 10
    else:
        break

print(f"нечетных цифр - {COUNTER1}: ( {STR1})")
print(f"четных цифр - {COUNTER2}: ( {STR2})")

"""
def my_func(var_int, cnt1):
    if var_int > 0:
        num = var_int % 10
        if num % 2:
            cnt1 += 1
            STR1 += str(NUM) + " "
        else:
            COUNTER2 += 1
            STR2 += str(NUM) + " "
    else:
        my_func(var_int // 10)
"""




