XYN = input().split()
X = int(XYN[0])
Y = int(XYN[1])
N = int(XYN[2])

for i in range(1, N + 1):
	if i%X == 0 and i%Y == 0:
		print("FizzBuzz")
	elif i%X == 0:
		print("Fizz")
	elif i%Y == 0:
		print("Buzz")
	else:
		print(i)