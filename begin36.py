# Begin36. Скорость первого автомобиля V1 км/ч, второго — V2 км/ч,
# расстояние между ними S км. Какое расстояние будет между ними
# через T часов, если автомобили удаляются друг от друга?
v1 = float(input())
v2 = float(input())
s = float(input())
t = float(input())

total_distance = s + (v1 + v2) * t

print(total_distance)
