# Integer3. Дан размер файла в байтах.
# Найти количество полных килобайтов (1 Кб = 1024 байта).
bytes_size = int(input())

kilobytes = bytes_size // 1024

print(kilobytes)
