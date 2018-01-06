import math

while True:
	rmc = input().split()
	
	if rmc == ['0','0','0']:
		break
		
	else:
		r = float(rmc[0])
		m = int(rmc[1])
		c = int(rmc[2])
		
		print(str(math.pi*r**2) + ' ' + str((c/m)*(r*2)**2))