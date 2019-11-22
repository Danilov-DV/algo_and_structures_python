#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

NUMS = []
for i in range(30):
    n = randint(-50, 50)
    NUMS.append(n)

print(NUMS)

MAX = -50
MAX_I = 0
for i in range(len(NUMS)):
    if (NUMS[i] < 0) and (NUMS[i] > MAX):
        MAX_I = i
        MAX = NUMS[i]

print(f"число : {MAX}, индекс : {MAX_I} ")
