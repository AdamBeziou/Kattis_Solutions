def dist(x1, y1, x2, y2, p):
	dist = (abs(x1-x2)**p + abs(y1 - y2)**p)**(1/p)
	return dist
	
while True:
	nums = input().split()
	nums = [float(x) for x in nums]
	if len(nums) == 1:
		break
	else:
		distance = dist(nums[0], nums[1], nums[2], nums[3], nums[4])
		print(round(distance, 10))