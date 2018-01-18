cases = int(input())

for i in range(cases):
	sequence = input().split()
	sequence = [int(x) for x in sequence]
	for i1 in range(1, sequence[0]):
		try:
			if sequence[i1 + 1] != sequence[i1] + 1:
				print(i1 + 1)
				break
			else:
				pass
		except IndexError:
			print(i1)