players = [0]*8

init = int(input()) - 1
players[init] = 1
time = 0
time_max = 210

questions = int(input())

for i in range(questions):
	q = input().split()
	t = int(q[0])
	c = q[1]
	
	if time + t <= time_max:	
		if c == 'T':
			pos = players.index(1)
			players[pos] = 0
			try:
				players[pos + 1] = 1
			except IndexError:
				players[0] = 1
		else:
			pass
			
		time += t
		
	else:
		pass
		
print(players.index(1) + 1)