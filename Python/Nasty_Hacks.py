cases = int(input())

for i in range(cases):
	rec = input().split()
	r = int(rec[0])
	e = int(rec[1])
	c = int(rec[2])
	
	advert_income = e - r
	
	if c == advert_income:
		print("does not matter")
	elif c < advert_income:
		print("advertise")
	else:
		print("do not advertise")