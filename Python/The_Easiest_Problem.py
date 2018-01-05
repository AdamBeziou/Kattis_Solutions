while True:
	N = int(input())
	
	if N == 0:
		break
		
	else:
		sum_of_digits_N = 0
		N_list = list(str(N))
		for i in range(len(N_list)):
			sum_of_digits_N += int(N_list[i])
		
		num = 11
		while True:
			num_list = list(str(num * N))
			sum_of_digits_num = 0
			for i1 in range(len(num_list)):
				sum_of_digits_num += int(num_list[i1])
			if sum_of_digits_num != sum_of_digits_N:
				num += 1
			else:
				print(num)
				break
		