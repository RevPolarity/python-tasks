# Begin35. Скорость лодки в стоячей воде равна V км/ч, скорость течения
# реки равна U км/ч (U < V). Время движения лодки по озеру равно T1 ч,
# а по реке (против течения) — T2 ч. Найти путь S, пройденный лодкой.
v = float(input())
u = float(input())
t1 = float(input())
t2 = float(input())

s_lake = v * t1
s_river = (v - u) * t2
total_distance = s_lake + s_river

print(total_distance)
