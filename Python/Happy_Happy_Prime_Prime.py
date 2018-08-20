import math

cases = int(input())

for i in range(cases):
    happyPrime = True
    NP = input().split()
    NP = [int(x) for x in NP]

    if NP[1] == 1:
        print("{} {} NO".format(NP[0], NP[1]))
        continue

    for j in range(2, math.ceil(NP[1]**0.5) + 1):
        if NP[1] % j == 0:
            happyPrime = False
            break

    if not happyPrime:
        print("{} {} NO".format(NP[0], NP[1]))
    else:

        num = str(NP[1])
        numList = [num]

        while num != '1' and happyPrime == True:
            numReplace = 0
            for j in num:
                numReplace += int(j)**2
            numReplace = str(numReplace) 

            if numReplace in numList:
                happyPrime = False
            else:
                numList.append(numReplace)
                num = numReplace

        if not happyPrime:
            print("{} {} NO".format(NP[0], NP[1]))
        else:
            print("{} {} YES".format(NP[0], NP[1]))