NM = [-1, -1]
while NM != [0, 0]:
    gold = 0

    NM = list(map(int, input().split()))
    if NM == [0, 0]:
        break

    dia = []
    height = []
    for i in range(NM[0]):
        dia.append(int(input()))
    for i in range(NM[1]):
        height.append(int(input()))

    height.sort()
    dia.sort()

    for h in height:
        if len(dia) > 0 and h >= dia[0]:
            dia.pop(0)
            gold += h

    if len(dia) > 0:
        print('Loowater is doomed!')
        continue
    else:
        print(gold)
        
            
