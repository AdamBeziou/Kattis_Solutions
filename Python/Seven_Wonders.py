sequence = list(input())
T = 0
G = 0
C = 0
triple = 0

for i in range(len(sequence)):
	if sequence[i] == 'T':
		T += 1
	elif sequence[i] == 'G':
		G += 1
	else:
		C += 1
		
for i in range(len(sequence)):
	try:
		sequence.remove('T')
	except ValueError:
		break
	try:
		sequence.remove('G')
	except ValueError:
		break
	try:
		sequence.remove('C')
	except ValueError:
		break
	triple += 1
		

print(T**2 + G**2 + C**2 + triple*7)