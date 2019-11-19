"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def my_f(n):
    # print(n % 10)
    if n // 10 == 0:
        return f"{n % 10}"
    else:
        return f"{n % 10}{my_f(n // 10)}"


VAR_INT = int(input("введите число "))

print(my_f(VAR_INT))

STR = ""
while True:
    if VAR_INT > 0:
        STR += str(VAR_INT % 10)
        VAR_INT = VAR_INT // 10
    else:
        VAR_INT = int(STR)
        print(VAR_INT)
        break
