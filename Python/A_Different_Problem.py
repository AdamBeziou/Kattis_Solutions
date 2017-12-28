while True:
	try:
		pair = input().split()
		pair = [int(x) for x in pair]
		pair.sort()
		print(pair[1] - pair[0])
	except EOFError:
		break
