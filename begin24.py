# Begin24. Даны переменные A, B, C. Поменять их содержимое местами так,
# чтобы A получила значение C, B — значение A, а C — значение B.
a = float(input())
b = float(input())
c = float(input())

a, b, c = c, a, b

print(a)
print(b)
print(c)
