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
common = ""
for key in d2:
    if key in d:
        common = key
d.update(d2)
print(len(d))
print(d[common])
