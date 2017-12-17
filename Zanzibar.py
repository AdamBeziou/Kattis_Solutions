cases = int(input())
for i in range(cases):
	lower = 0
	popyr = input().split()
	popyr = [int(x) for x in popyr]
	for i in range(len(popyr)):
		if popyr[i] == 0:
			pass
		elif popyr[i+1] >= popyr[i]*2:
			lower += popyr[i+1] - (popyr[i]*2)
		else:
			pass
	print(lower)
	