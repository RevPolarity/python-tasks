n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
inverted = {}
for key, value in d.items():
    inverted[value] = key
for value, key in inverted.items():
    print(f"{value}: {key}")
