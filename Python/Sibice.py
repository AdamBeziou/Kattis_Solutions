nwh = input().split()
n = int(nwh[0])
w = int(nwh[1])
h = int(nwh[2])
compare = (w**2 + h**2)**(1/2)
	
for i in range(n):
	length = int(input())
	if length <= compare:
		print("DA")
		
	else:
		print("NE")