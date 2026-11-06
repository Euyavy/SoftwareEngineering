
x1 = int(input("Введите координату X1: "))
y1 = int(input("Введите координату Y1: "))
x2 = int(input("Введите координату X2: "))
y2 = int(input("Введите координату Y2: "))
if x1 > 0 and y1 > 0:
    i1 = "I"
elif x1 < 0 and y1 > 0:
    i1 = "II"
elif x1 < 0 and y1 < 0:
    i1 = "III"
else:
    i1 = "IV"

if x2 > 0 and y2 > 0:
    i2 = "I"
elif x2 < 0 and y2 > 0:
    i2 = "II"
elif x2 < 0 and y2 < 0:
    i2 = "III"
else:
    i2 = "IV"
if i1 == i2:
    print("Yes,", i1)
else:
    print("No")
