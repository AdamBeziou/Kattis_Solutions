pos = input().split()
pos = [int(x) for x in pos]
moves = 0

while pos[1] - pos[0] > 1 or pos[2] - pos[1] > 1:
	if pos[2] - pos[1] < pos[1] - pos[0]:
		pos[2] = pos[1] - 1
		moves += 1
		pos.sort()
	else:
		pos[0] = pos[1] + 1
		moves += 1
		pos.sort()
	
print(moves)
