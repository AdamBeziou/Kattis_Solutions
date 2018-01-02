hyphen = input().split('-')
acro = []

for i in range(len(hyphen)):
	acro.append(hyphen[i][0])
	
print(''.join(acro))