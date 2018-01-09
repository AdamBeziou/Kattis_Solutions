import math

space = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', "'"]

cases = int(input())

for i in range(cases):
	spaces = 0
	seconds = 0
	aphorism = list(input())

	for i1 in range(len(aphorism)):
		pos = space.index(aphorism[i1])
		try:
			next_pos = space.index(aphorism[i1+1])
		except IndexError:
			break
		if abs(pos - next_pos) <= 14:
			spaces += abs(pos - next_pos)
			
		else:
			if pos > 14:
				spaces += (28 - pos) + next_pos
			else:
				spaces += (28 - next_pos) + pos
		seconds += 1
	
	seconds += 1
	seconds += (spaces*((60*math.pi)/28))/15
	
	print(seconds)