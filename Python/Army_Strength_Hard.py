cases = int(input())

for i in range(cases):
    blank = input()
    GM = input().split()
    #GM = [int(x) for x in GM]
    #GArmy = [0] * GM[0]
    #MGArmy = [] * GM[1]
    gArmy = input().split()
    gArmy = [int(x) for x in gArmy]
    gArmy.sort(reverse = True)

    mArmy = input().split()
    mArmy = [int(x) for x in mArmy]
    mArmy.sort(reverse = True)

    while len(gArmy) != 0 and len(mArmy) != 0:
        gStren = gArmy.pop()
        mStren = mArmy.pop()

        if gStren > mStren:
            gArmy.append(gStren)
        elif mStren > gStren:
            mArmy.append(mStren)
        else:
            gArmy.append(gStren)

    if len(gArmy) == 0:
        print("MechaGodzilla")
    else:
        print("Godzilla")


