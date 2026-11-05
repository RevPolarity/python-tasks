n = int(input())
result = ""
for i in range(n):
    result += chr(ord("z") - i)
print(result)
