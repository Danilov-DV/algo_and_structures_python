"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

NUMS = []
for i in range(10):
    n = randint(1, 10)
    NUMS.append(n)
# NUMS = [1, 6, 5, 1, 6, 9, 5, 7, 6, 1]
print(NUMS)

MIN1 = 10
MIN1_I = 0

for i in range(len(NUMS)):
    if NUMS[i] < MIN1:
        MIN1 = NUMS[i]
        MIN1_I = i

MIN2 = 10
for i in range(len(NUMS)):
    if (NUMS[i] < MIN2) and (MIN1_I != i):
        MIN2 = NUMS[i]

print(f"min1 : {MIN1}, min2 : {MIN2} ")
