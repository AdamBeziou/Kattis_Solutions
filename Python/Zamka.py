L = int(input())
D = int(input())
X = int(input())

for i in range(L, D + 1):
	num = 0
	num_list = list(str(i))
	for i1 in range(len(num_list)):
		num += int(num_list[i1])
		
	if num == X:
		print(''.join(num_list))
		break
	else:
		pass
		
for i in range(D + 1):
	num = 0
	num_list = list(str(D + 1 - i))
	for i1 in range(len(num_list)):
		num += int(num_list[i1])
		
	if num == X:
		print(''.join(num_list))
		break
	else:
		pass