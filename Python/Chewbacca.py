NKQ = list(map(int, input().split()))
for i in range(NKQ[2]):
    count = 0
    xy = list(map(int, input().split()))
    x = xy[0]
    y = xy[1]
    while x != y:
        if x > y:
            x = (x + NKQ[1] - 2) // NKQ[1]
        elif x < y:
            y = (y + NKQ[1] - 2) // NKQ[1]
        count += 1
    print(count)