n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = int(input())
    d2[key] = value
ignored = 0
for key in d2:
    if key in d:
        ignored += 1
    else:
        d[key] = d2[key]
print(len(d))
print(ignored)
