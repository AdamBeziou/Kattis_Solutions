name = list(input())
letter = name[0]
short = [letter]

for i in range(1, len(name)):
	if name[i] == letter:
		pass
	else:
		letter = name[i]
		short.append(name[i])
		
print(''.join(short))