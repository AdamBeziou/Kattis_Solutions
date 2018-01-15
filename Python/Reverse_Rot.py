sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
	rotString = input().split()
	rot = int(rotString[0])
	
	if rot == 0:
		break
		
	else:
		string = rotString[1]
	
		repString = []
		
		for i in range(len(string)):
			repString.append(sequence[(sequence.index(string[i]) + rot) % 28])
			
		repString.reverse()
			
		print(''.join(repString))