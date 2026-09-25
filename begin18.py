# Begin18. Даны три точки A, B, C на числовой оси. Точка C расположена 
# между точками A и B. Найти произведение длин отрезков AC и BC.
a = float(input())
b = float(input())
c = float(input())

len_ac = abs(c - a)
len_bc = abs(c - b)
product = len_ac * len_bc

print(product)
