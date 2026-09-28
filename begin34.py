# Begin34. Известно, что X кг шоколадных конфет стоят A рублей,
# а Y кг ирисок стоят B рублей. Найти стоимость 1 кг шоколадных
# конфет и 1 кг ирисок, а также определить, во сколько раз
# шоколадные конфеты дороже ирисок.
x = float(input())
a = float(input())
y = float(input())
b = float(input())

cost_choco = a / x
cost_toffee = b / y
ratio = cost_choco / cost_toffee

print(cost_choco)
print(cost_toffee)
print(ratio)
