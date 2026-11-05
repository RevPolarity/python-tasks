n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
s = 0
for x in a:
    s = s + x
avg = s / len(a)
k = 0
for x in a:
    if x > avg:
        print(x)
        k = k + 1
print(k)