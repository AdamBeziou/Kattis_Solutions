hexConv = {'0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'a':10,
            'b':11,
            'c':12,
            'd':13,
            'e':14,
            'f':15,
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15}

while True:
    try:
        line = input()
    except EOFError:
        break

    prefix = ''
    hex = ''
    decimal = 0
    hexRecord = False
    for i, n in enumerate(line[1:]):
        if len(hex) == 8 or (hexRecord and line[i + 1] not in list(hexConv)):
            hexRecord = False
            for j, s in enumerate(hex[::-1]):
                decimal += hexConv[s] * (16**j)
            print(f"{prefix}{hex} {decimal}")
            hex = ''
            decimal = 0

        if hexRecord:
            hex = hex + line[i + 1]
        if line[i] + n == '0x' or line[i] + n == '0X':
            prefix = line[i] + n
            hexRecord = True
    if len(hex) != 0:
        for j, s in enumerate(hex[::-1]):
            decimal += hexConv[s] * (16**j)
        print(f"{prefix}{hex} {decimal}")
            
