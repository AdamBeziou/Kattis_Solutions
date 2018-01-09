XY = input().split()
X = int(XY[0])
Y = int(XY[1])

ends = X * 4 + Y * 3

ends -= X * 4

if ends%2 != 0:
	print("impossible")
else:
	print("possible")