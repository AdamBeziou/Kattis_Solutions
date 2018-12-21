n = -1
while n != 0:
    n = int(input())
    corr = {}
    first = []
    second = []
    fCopy = []
    sCopy = []
    final = []
    for i in range(n):
        entry = int(input())
        first.append(entry)
        fCopy.append(entry)
    for i in range(n):
        entry = int(input())
        second.append(entry)
        sCopy.append(entry)

    fCopy.sort()
    sCopy.sort()

    for i in range(n):
        corr[fCopy[i]] = sCopy[i]
    
    for i in range(n):
        print(corr[first[i]])
    print("")



    
