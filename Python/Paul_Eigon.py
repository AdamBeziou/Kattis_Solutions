NPQ = input().split()
N = int(NPQ[0])
P = int(NPQ[1])
Q = int(NPQ[2])

current_round = P + Q
check = current_round//N

if check%2 == 0:
	print("paul")
	
else:
	print("opponent")