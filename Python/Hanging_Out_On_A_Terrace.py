limevents = input().split()
lim = int(limevents[0])
events = int(limevents[1])
current = 0
denied = 0

for i in range(events):
	event = input().split()
	
	if event[0] == 'enter':
		if current + int(event[1]) <= lim:
			current += int(event[1])
		else:
			denied += 1
	else:
		current -= int(event[1])
print(denied)