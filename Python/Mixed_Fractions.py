while True:
    mixedFraction = input().split()
    mixedFraction = [int(x) for x in mixedFraction]

    if mixedFraction == [0,0]:
        break

    else:
        print("%d %d / %d" % (mixedFraction[0]//mixedFraction[1], mixedFraction[0]%mixedFraction[1], mixedFraction[1]))