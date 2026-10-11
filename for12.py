n=int(input())

total = 1.0

for i in range(1, n+1):
    factor= 1.0 + i /10

    total *= factor

print(total)
