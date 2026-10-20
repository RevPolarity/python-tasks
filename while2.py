
A = 17.5
B = 3.0


temp_A = A
count = 0

while temp_A >= B:
    temp_A -= B
    count += 1

print("Количество отрезков B на отрезке A:", count)
