num_of_stars = int(input())
half_one = (num_of_stars//2) + 1

pairs = []

print("%d:" % (num_of_stars))
for i in range(2, half_one + 1):
	if num_of_stars%(i + (i-1)) == 0:
		print("%d,%d" % (i, i-1))
	elif num_of_stars%(i + (i-1)) - i == 0:
		print("%d,%d" % (i, i-1))
	if num_of_stars%(i + i) == 0:
		print("%d,%d" % (i, i))
	elif num_of_stars%(i + i) - i == 0:
		print("%d,%d" % (i, i))
	else:
		pass