while True:
	num = int(input())
	if num == -1:
		break
	else:
		distance = 0
		speed = []
		time = []
		for i in range(num):
			speed_time = input().split()
			speed_time = [int(x) for x in speed_time]
			speed.append(speed_time[0])
			time.append(speed_time[1])
			if i != 0:
				distance += speed[i] * (time[i] - time[i-1])
			else:
				distance += speed[i] * time[i]
		print("%d miles" % (distance))