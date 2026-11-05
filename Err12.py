try:
    number = int(input())
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(number)
