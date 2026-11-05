m = int(input())
n = int(input())
values = [int(input()) for i in range(m)]
a = []
for i in range(m):
    a.append([values[i]] * n)
for row in a:
    print(row)
