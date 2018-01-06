cases = int(input())

for i in range(cases):
	string1 = list(input())
	string2 = list(input())
	string_err = []
	print(''.join(string1))
	print(''.join(string2))
	
	for i1 in range(len(string1)):
		if string1[i1] != string2[i1]:
			string_err.append('*')
		else:
			string_err.append('.')
			
	print(''.join(string_err))
	print('')