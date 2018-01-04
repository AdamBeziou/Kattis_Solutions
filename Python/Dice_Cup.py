NM = input().split()
N = int(NM[0])
M = int(NM[1])

sums = []
count = []
nums = []
high = 0

for i in range(1, N + 1):
	for x in range(1, M + 1):
		sums.append(i + x)

for i in range(len(sums)):
	count.append(sums.count(sums[i]))
	
	if sums.count(sums[i]) > high:
		high = sums.count(sums[i])
	else:
		pass
		
for i in range(len(sums)):
	if count[i] == high and sums[i] not in nums:
		print(sums[i])
		nums.append(sums[i])
	else:
		pass