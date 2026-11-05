m = int(input())
n = int(input())
d = float(input())
values = [float(input()) for i in range(m)]
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(values[i] + d * j)
    a.append(row)
for row in a:
    print(row)
