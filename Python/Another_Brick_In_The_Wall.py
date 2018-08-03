HWN = input().split()
HWN = [int(x) for x in HWN]

bricks = input().split()
bricks = [int(x) for x in bricks]

wallLength = 0
while HWN[0] > 0 and len(bricks) > 0:
    wallLength += bricks.pop(0)

    if wallLength == HWN[1]:
        HWN[0] -= 1
        wallLength = 0
        
    elif wallLength > HWN[1]:
        break

if HWN[0] == 0:
    print("YES")
else:
    print("NO")