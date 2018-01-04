x_coords = []
y_coords = []

for x in range(3):
	xy = input().split()
	x_coords.append(xy[0])
	y_coords.append(xy[1])
	
for x in range(3):
	x_count = x_coords.count(x_coords[x])
	if x_count == 1:
		x_coord = x_coords[x]
		break
	else:
		pass
		
for x in range(3):
	y_count = y_coords.count(y_coords[x])
	if y_count == 1:
		y_coord = y_coords[x]
		break
	else:
		pass
		
print(x_coord + ' ' + y_coord)