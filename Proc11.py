def minmax(x, y):
    if x < y:
        return x, y
    return y, x


a = float(input())
b = float(input())
c = float(input())
d = float(input())
min1, max1 = minmax(a, b)
min2, max2 = minmax(c, d)
smallest, temp1 = minmax(min1, min2)
temp2, largest = minmax(max1, max2)
print(smallest)
print(largest)
