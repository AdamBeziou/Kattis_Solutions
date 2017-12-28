norm_table = {"A" : 11, "K" : 4, "Q" : 3, "J" : 2, "T" : 10, "9" : 0, "8" : 0, "7" : 0}
dom_table = {"A" : 11, "K" : 4, "Q" : 3, "J" : 20, "T" : 10, "9" : 14, "8" : 0, "7" : 0}

totpts = 0
handsuit = input().split()
for i in range(int(handsuit[0])*4):
	valuesuit = input()
	if valuesuit[1] == handsuit[1]:
		totpts += dom_table[valuesuit[0]]
	else:
		totpts += norm_table[valuesuit[0]]
		
print(totpts)
