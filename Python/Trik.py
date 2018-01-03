pos = [1,0,0]
moves = list(input())

for i in range(len(moves)):
	if moves[i] == 'A':
		hold = pos[0]
		pos[0] = pos[1]
		pos[1] = hold
	elif moves[i] == 'B':
		hold = pos[1]
		pos[1] = pos[2]
		pos[2] = hold
	else:
		hold = pos[0]
		pos[0] = pos[2]
		pos[2] = hold

print(pos.index(1) + 1)