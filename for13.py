n=int(input())

total=0.0
sign = 1

for i in range(1,n+1):
    number = 1.0 + i/10

    total +=number*sign

    sign =-sign

print(total)