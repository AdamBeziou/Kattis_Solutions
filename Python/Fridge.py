permutations = []
nums = list(input())
nums = [int(x) for x in nums]
nums.sort()

smallestCount = 1001
fewestInt = 0
zeroCount = nums.count(0)

for i in range(1, 10):
    if nums.count(i) < smallestCount:
        fewestInt = i
        smallestCount = nums.count(i)

if zeroCount < smallestCount:
    print('1' + '0' * (zeroCount + 1))
else:
    print(str(fewestInt) * (smallestCount + 1))
