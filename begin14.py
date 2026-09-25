# Begin14. Дана длина L окружности. Найти ее радиус R и площадь S круга.
# Учитывая, что L = 2·π·R, S = π·R². В качестве значения π использовать 3.14.
length = float(input())
pi = 3.14

radius = length / (2 * pi)
area = pi * radius ** 2

print(radius)
print(area)
