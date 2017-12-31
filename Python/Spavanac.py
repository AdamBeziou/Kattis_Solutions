time = input().split()
time = [int(x) for x in time]

twentyfour = (time[0] * 60) + time[1]
twentyfour -= 45

if twentyfour < 0:
	print("%d %d" % (23, 60 + twentyfour))
else:
	hours = twentyfour//60
	min = twentyfour%60
	print("%d %d" % (hours,min))