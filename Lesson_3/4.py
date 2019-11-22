# 4.	Определить, какое число в массиве встречается чаще всего.

from random import randint

NUMS = []
for i in range(30):
    n = randint(0, 50)
    NUMS.append(n)

print(NUMS)

MAX_CNT = 0
NUM = 0
for i in range(len(NUMS)):
    CNT = 0
    for j in range(len(NUMS)):
        if NUMS[i] == NUMS[j]:
            CNT += 1
    if CNT > MAX_CNT:
        MAX_CNT = CNT
        NUM = NUMS[i]

if MAX_CNT > 1:
    print(f"число - {NUM}, кол-во повторений - {MAX_CNT} ")
else:
    print("в массиве нет дубликатов")
