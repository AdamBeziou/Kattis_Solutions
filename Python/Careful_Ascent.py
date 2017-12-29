firefly_coords = input().split()
fire_x = int(firefly_coords[0])
fire_y = int(firefly_coords[1])
min = fire_y

num = int(input())
for i in range(num):
	shield_att = input().split()
	lower = int(shield_att[0])
	upper = int(shield_att[1])
	rate = float(shield_att[2])
	
	min -= upper - lower
	new_min = (upper - lower) * rate
	min += new_min
	
h_rate = fire_x/min
print(h_rate)