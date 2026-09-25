# Begin15. Дана площадь S круга. Найти его диаметр D и длину L окружности.
# Учитывая, что L = 2·π·R, S = π·R². В качестве значения π использовать 3.14.
area = float(input())
pi = 3.14

radius = (area / pi) ** 0.5
diameter = 2 * radius
length = 2 * pi * radius

print(diameter)
print(length)
