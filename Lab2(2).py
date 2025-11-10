import math
from mymodule import sum_squares

def compute_z(x, y):
    return math.cos(x)**2 + math.sin(y)**2

x_rad = float(input("Введіть x в радіанах: "))
y_rad = float(input("Введіть y в радіанах: "))
z = compute_z(x_rad, y_rad)
print("z =", z)

n = int(input("Введіть N (ціле додатнє число): "))
S = sum_squares(n)
print(f"Сума квадратів від 1 до {n} = {S}")