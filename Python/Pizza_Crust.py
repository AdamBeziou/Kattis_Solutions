import math

radii = input().split()
areaTotal = (int(radii[0])**2) * math.pi
areaCheese = ((int(radii[0]) - int(radii[1]))**2) * math.pi
print((areaCheese/areaTotal) * 100)
