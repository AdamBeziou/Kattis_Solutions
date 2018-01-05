cases = int(input())
for i in range(cases):
	map = {}
	rc = input().split()
	R = int(rc[0])
	C = int(rc[1])
	for x in range(R):
		map[x] = list(input())
		map[x].reverse()
	
	print("Test %d" % (i+1))
	for x in range(R):
		print(''.join(map[R-x-1]))