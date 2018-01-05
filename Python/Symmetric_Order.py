set_num = 1

while True:
	names1 = []
	names2 = []
	num = int(input())
	count = 0
	
	if num == 0:
		break
	else:
		while True:
			names1.append(input())
			count += 1
			if count == num:
				break
				
			names2.append(input())
			count += 1
			if count == num:
				break
		print("SET %d" % (set_num))
		
		names2.reverse()
		
		for i in range(len(names1)):
			print(names1[i])
			
		for i in range(len(names2)):
			print(names2[i])
			
		set_num += 1