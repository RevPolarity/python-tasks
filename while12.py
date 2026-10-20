n=int(input())

k=0
total=0

while total<=0:
    k+=1
    total +=k

total -= k
k -=1

print(total)
print(k)