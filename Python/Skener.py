RCZZ = input().split()
map = {}
R = int(RCZZ[0])
C = int(RCZZ[1])
Z_R = int(RCZZ[2])
Z_C = int(RCZZ[3])

for i in range(R):
	map[i] = list(input())
	
for i in range(R):
	for i1 in range(C):
		map[i][i1] = map[i][i1]*Z_C
	
for i in range(R):
	for i1 in range(Z_R):
		print(''.join(map[i]))