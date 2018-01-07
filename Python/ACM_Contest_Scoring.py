time = 0
right = 0
wrong = []

while True:
	sequence = input()
	
	if sequence == '-1':
		break
		
	else:
		tec = sequence.split()
		t = int(tec[0])
		id = tec[1]
		rw = tec[2]
		
		if rw == 'wrong':
			wrong.append(id)
			
		else:
			right += 1
			time += t + 20*wrong.count(id)
			
print(str(right) + ' ' + str(time))