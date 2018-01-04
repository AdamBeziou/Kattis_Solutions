phrase = input().split()
message = 'yes'

for i in range(len(phrase)):
	count = phrase.count(phrase[i])
	
	if count > 1:
		message = 'no'
		break
	else:
		pass
		
print(message)