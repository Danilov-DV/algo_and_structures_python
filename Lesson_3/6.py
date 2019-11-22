"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint

LEFT = 1
RIGHT = 10

NUMS = []
for i in range(10):
    n = randint(LEFT, RIGHT)
    NUMS.append(n)

# NUMS = [1, 6, 5, 4, 6, 9, 5, 7, 6, 1]
print(NUMS)

MIN = RIGHT
MAX = LEFT-1

MIN_I = 0
MAX_I = 0

for i in range(len(NUMS)):
    if NUMS[i] > MAX:
        MAX = NUMS[i]
        MAX_I = i
    if NUMS[i] < MIN:
        MIN = NUMS[i]
        MIN_I = i

print(f"NUMS[{MIN_I}] = {MIN}")
print(f"NUMS[{MAX_I}] = {MAX}")

if MIN_I > MAX_I:
    MAX_I, MIN_I = MIN_I, MAX_I

SUM = 0
for i in range(MIN_I+1, MAX_I):
    SUM += NUMS[i]

print(SUM)
