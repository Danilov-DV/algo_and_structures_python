#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

LEFT = 1
RIGHT = 50

NUMS = []
for i in range(10):
    n = randint(LEFT, RIGHT)
    NUMS.append(n)

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

NUMS[MAX_I] = MIN
NUMS[MIN_I] = MAX

print(NUMS)
