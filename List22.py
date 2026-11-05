n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
mult = [x * d for x in a]
equal = [x for x in a if x == d]
print(mult)
print(len(equal))
