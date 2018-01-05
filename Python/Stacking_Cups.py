num = int(input())

color_dict = {}

for i in range(num):
	color_num = input().split()
	
	try:
		radius = int(color_num[0])/2
		color = color_num[1]
	except ValueError:
		radius = int(color_num[1])
		color = color_num[0]
	
	color_dict[radius] = color
	
sorted_keys = sorted(color_dict.keys())

for i in range(len(sorted_keys)):
	print(color_dict[sorted_keys[i]])
				
