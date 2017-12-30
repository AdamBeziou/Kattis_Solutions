num = int(input())
sum = 0
for i in range(num):
	number = list(input())
	power = int(number.pop())
	mant = int(''.join(number))
	sum += mant**power
	
print(sum)