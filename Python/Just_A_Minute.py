obs = int(input())
den = 0
num = 0
for i in range(obs):
    MS = list(map(int, input().split()))
    den += MS[1]
    num += MS[0] * 60

if den/num <= 1:
    print("measurement error")
else:
    print(den/num)