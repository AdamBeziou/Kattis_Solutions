numOfSampleSquares = int(input())
baseTwoList = []
n = -1
barSize = 0

while barSize < numOfSampleSquares:
    n += 1
    barSize = 2**n
    baseTwoList.append(barSize)

if numOfSampleSquares % 2 == 0:
    nSub = n + 1
    while numOfSampleSquares > 0:
        nSub -= 1

        if numOfSampleSquares - baseTwoList[nSub] < 0:
            pass
        else:
            numOfSampleSquares -= baseTwoList[nSub]

    print("{} {}".format(barSize, n - nSub))
else:
    print("{} {}".format(barSize, n))