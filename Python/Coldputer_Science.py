num = int(input())
temps = input().split()
temps = [int(x) for x in temps]
below_zero_temps = 0

for i in range(num):
	if temps[i] < 0:
		below_zero_temps += 1
	else:
		pass
		
print(below_zero_temps)