num = int(input())
for i in range(num):
	calc = input().split("+")
	if calc[0] == "P=NP":
		print("skipped")
	else:
		print(int(calc[0])+int(calc[1]))
	
