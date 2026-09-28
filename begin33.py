# Begin33. Известно, что X кг конфет стоят A рублей.
# Найти стоимость 1 кг и Y кг этих же конфет.
x = float(input())
a = float(input())
y = float(input())

price_per_kg = a / x
total_cost_y = price_per_kg * y

print(price_per_kg)
print(total_cost_y)
