# Begin23. Даны переменные A, B, C. Поменять их содержимое местами так,
# чтобы A получила значение B, B — значение C, а C — значение A.
a = float(input())
b = float(input())
c = float(input())

a, b, c = b, c, a

print(a)
print(b)
print(c)
