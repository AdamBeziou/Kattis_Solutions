ABCD = input().split()
ABCD = [int(x) for x in ABCD]
ABCD.sort(reverse = True)

if ABCD[0] > ABCD[1]:
	one = ABCD[1]
else:
	one = ABCD[0]
	
if ABCD[2] > ABCD[3]:
	two = ABCD[3]
else:
	two = ABCD[2]
	
print(one*two)