# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

VAR1 = int(input("Первое число: "))
VAR2 = int(input("Второе число: "))
VAR3 = int(input("Третье число: "))

if ((VAR1 > VAR2) and (VAR1 < VAR3)) or ((VAR1 < VAR2) and (VAR1 > VAR3)):
    print(f"{VAR1} является средним")
elif ((VAR2 > VAR1) and (VAR2 < VAR3)) or ((VAR2 < VAR1) and (VAR2 > VAR3)):
    print(f"{VAR2} является средним")
elif ((VAR3 > VAR2) and (VAR3 < VAR1)) or ((VAR2 < VAR1) and (VAR2 > VAR3)):
    print(f"{VAR3} является средним")
else:
    print("Вводятся три разных числа!")

