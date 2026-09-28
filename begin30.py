# Begin30. Дано значение угла α в радианах (0 < α < 2·π).
# Перевести его в градусы. Использовать константу math.pi.
import math

alpha_radians = float(input())

alpha_degrees = alpha_radians * (180 / math.pi)

print(alpha_degrees)
