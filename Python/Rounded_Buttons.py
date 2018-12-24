import math

cases = int(input())

for i in range(cases):
    params = input().split()
    x = float(params.pop(0))
    y = float(params.pop(0))
    w = float(params.pop(0))
    h = float(params.pop(0))
    r = float(params.pop(0))
    m = int(params.pop(0))
    
    for j in range(m):
        coordX = float(params.pop(0))
        coordY = float(params.pop(0))

        if coordX <= x + w - r and coordX >= x + r and coordY <= y + h and coordY >= y or coordX <= x + w and coordX >= x and coordY <= y + h - r and coordY >= y + r:
            print('inside')
            continue

        elif ((x + r - coordX)**2 + (y + r - coordY)**2)**(1/2) - r <= 0.00001:
            print('inside')
        elif ((x + w - r - coordX)**2 + (y + r - coordY)**2)**(1/2) - r <= 0.00001:
            print('inside')
        elif ((x + r - coordX)**2 + (y + h - r - coordY)**2)**(1/2) - r <= 0.00001:
            print('inside')
        elif ((x + w - r - coordX)**2 + (y + h - r - coordY)**2)**(1/2) - r <= 0.00001:
            print('inside')

        else:
            print('outside')

    print('')
                    
        
        

