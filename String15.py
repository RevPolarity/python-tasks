s = input()
alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
count = 0
for ch in s:
    if ch in alphabet:
        count += 1
print(count)
