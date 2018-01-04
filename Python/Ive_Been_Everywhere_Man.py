cases = int(input())

for x in range(cases):
	num = int(input())
	places = []
	for i in range(num):
		place = input()
		if place in places:
			pass
		else:
			places.append(place)
	print(len(places))