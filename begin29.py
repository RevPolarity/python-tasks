# Begin29. Дано значение угла α в градусах (0 < α < 360).
# Перевести его в радианы. Использовать константу math.pi.
import math

alpha_degrees = float(input())

alpha_radians = alpha_degrees * (math.pi / 180)

print(alpha_radians)
