suit = {'P':[], 'K':[], 'H':[], 'T':[]}

sequence = list(input())
double = False

for i in range(len(sequence)//3):
	if sequence[(i*3) + 1] == '0':
		if sequence[(i*3) + 2] not in suit[sequence[i*3]]:
			suit[sequence[i*3]].append(sequence[(i*3) + 2])
		else:
			print("GRESKA")
			double = True
			break
	else:
		if sequence[(i*3) + 1] + sequence[(i*3) + 2] not in suit[sequence[i*3]]:
			suit[sequence[i*3]].append(sequence[(i*3) + 1] + sequence[(i*3) + 2])
		else:
			print("GRESKA")
			double = True
			break

if double == False:
	print("%d %d %d %d" % (13 - len(suit['P']), 13 - len(suit['K']), 13 - len(suit['H']), 13 - len(suit['T'])))
else:
	pass