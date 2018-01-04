cases = int(input())

for i in range(cases):
	num_of_people = int(input())
	nums = input().split()
	
	for x in range(len(nums)):
		count = nums.count(nums[x])
		if count < 2:
			print("Case #%d: %s" % (i + 1, nums[x]))
		else:
			pass