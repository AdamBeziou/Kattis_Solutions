import math

cases = int(input())

for i in range(cases):
	vthetaxh1h2 = input().split()
	v = float(vthetaxh1h2[0])
	theta = math.radians(float(vthetaxh1h2[1]))
	x = float(vthetaxh1h2[2])
	h1 = float(vthetaxh1h2[3])
	h2 = float(vthetaxh1h2[4])
	
	time = x/(v*math.cos(theta))
	
	y = v*time*math.sin(theta) - (1/2)*9.81*time**2
	
	if y >= h1 + 1 and y <= h2 - 1:
		print("Safe")
	else:
		print("Not Safe")
	