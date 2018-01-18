board = []
kCount = 0

for i in range(5):
	line = input()
	kCount += line.count('k')
	board.append(line)
	
if kCount != 9:
	invalid = True
else:
	invalid = False

for y in range(5):
	if invalid == True:
		break
	for x in range(5):	
		if board[y][x] == 'k':
			try:
				if board[y - 2][x - 1] == 'k' and y >= 2 and x >= 1:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y - 2][x + 1] == 'k' and y >= 2 and x <= 4:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y - 1][x + 2] == 'k' and y >= 1 and x <= 2:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y + 1][x + 2] == 'k' and y <= 4 and x <= 2:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y + 2][x + 1] == 'k' and y <= 2 and x <= 4:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y + 2][x - 1] == 'k' and y <= 2 and x >= 1:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y + 1][x - 2] == 'k' and y <= 4 and x >= 2:
					invalid = True
			except IndexError:
				pass
			try:
				if board[y - 1][x - 2] == 'k' and y >= 1 and x >= 2:
					invalid = True
			except IndexError:
				pass
			else:
				pass
		else:
			pass
			
		if invalid == True:
			break
		
if invalid == True:
	print("invalid")
else:
	print("valid")
			
