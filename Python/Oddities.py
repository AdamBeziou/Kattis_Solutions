num = int(input())

for i in range(num):
	number = int(input())
	
	if number%2 == 0:
		print("%d is even" % (number))
	else:
		print("%d is odd" % (number))