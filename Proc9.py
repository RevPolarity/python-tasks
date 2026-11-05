def add_left_digit(d, k):
    power = 1
    rest = k
    while rest > 0:
        power *= 10
        rest //= 10
    return d * power + k


k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)
