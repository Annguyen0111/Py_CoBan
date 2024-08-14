import math

a = float(input())
b = float(input())
c = float(input())

delta = b * b - 4 * a * c

if(delta > 0):
    x1 = (-b - math.sqrt(delta) / (2 * a))
    x1 = (-b + math.sqrt(delta) / (2 * a))
    print("x1 = ", x1)
    print("x2 = ", x2)
else if(delta == 0):
    x = -b / (2 * a)
    print("x1 = x2 = ", x)
else:
    print("Phuong trinh vo nghiem")
