import math

hv = input().split()

h = int(hv[0])
v = int(hv[1])

length = (int(h/math.sin(math.radians(v))) + 1)
print(length)