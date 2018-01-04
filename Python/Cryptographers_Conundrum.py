per = ["P", "E", "R"]
count = 0
days = 0

phrase = list(input())
for i in range(len(phrase)):
	if per[count] == phrase[i]:
		pass
	else:
		days += 1
	
	if count < 2:
		count += 1
	else:
		count = 0
	
print(days)