nums = input().split()

num1 = list(nums[0])
num1 = int(''.join(num1[2] + num1[1] + num1[0]))

num2 = list(nums[1])
num2 = int(''.join(num2[2] + num2[1] + num2[0]))

if num1 > num2:
	print(num1)
	
else:
	print(num2)