import math

cases = int(input())

for i in range(cases):
    XY = input().split()

    X = int(XY[0])
    Y = int(XY[1])

    h = (-(((X*-2) + (Y*-2))*2) - math.sqrt((((X*2) + (Y*2))*2)**2 - 4*12*X*Y))/(2*12)
    maxVolume = X*Y*h + ((X*-2) + (Y*-2))*(h**2) + 4*(h**3)

    print(maxVolume)