set = [1, 1, 2, 2, 2, 8]

iset = input().split()
iset = [int(x) for x in iset]

for i in range(len(iset)):
	iset[i] = set[i] - iset[i]

iset = [str(x) for x in iset]
print(' '.join(iset))