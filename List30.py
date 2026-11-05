n = int(input())
s = []
for i in range(n):
    s.append(input())
lengths = [len(x) for x in s]
print(lengths)
print(sum(lengths))
