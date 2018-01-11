cases = int(input())

for i in range(cases):
	dist = 0
	num = int(input())
	spots = input().split()
	spots = [int(x) for x in spots]
	spots.sort()
		
	for i in range(num - 1):
		dist += spots[i+1] - spots[i]
		
	print(dist * 2)