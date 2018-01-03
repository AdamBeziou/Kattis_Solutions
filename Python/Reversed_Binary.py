num = int(input())
reverse = 0
binary = []

while num > 0:
	binary.append(num%2)
	num = num//2
	
for i in range(len(binary)):
	reverse += binary[len(binary) - 1 - i] * 2**i
	
print(reverse)