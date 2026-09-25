# Begin17. Даны три точки A, B, C на числовой оси. 
# Найти длины отрезков AC и BC и их сумму.
a = float(input())
b = float(input())
c = float(input())

len_ac = abs(c - a)
len_bc = abs(c - b)
total_sum = len_ac + len_bc

print(len_ac)
print(len_bc)
print(total_sum)
