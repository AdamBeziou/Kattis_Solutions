lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

total = 0
up = 0
low = 0
white = 0
symbol = 0

sequence = list(input())

for i in range(len(sequence)):
	if sequence[i] in lower:
		low += 1
	elif sequence[i] in upper:
		up += 1
	elif sequence[i] == '_':
		white += 1
	else:
		symbol += 1
	total += 1
	
print(white/total)
print(low/total)
print(up/total)
print(symbol/total)
