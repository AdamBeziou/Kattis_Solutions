board = []
possibleMoves = 0

for i in range(7):
	board.append('  ' + input() + '  ')

for i in range(len(board)):
	for i1 in range(len(board[i])):
		if board[i][i1] == '.':
			try:
				if board[i][i1 + 1] == 'o' and board[i][i1 + 2] == 'o':
					possibleMoves += 1
			except IndexError:
				pass
			
			try:
				if board[i][i1 - 1] == 'o' and board[i][i1 - 2] == 'o' and i1 >= 2:
					possibleMoves += 1
			except IndexError:
				pass
				
			try:
				if board[i + 1][i1] == 'o' and board[i + 2][i1] == 'o':
					possibleMoves += 1
			except IndexError:
				pass
				
			try:
				if board[i - 1][i1] == 'o' and board[i - 2][i1] == 'o' and i >= 2:
					possibleMoves += 1
			except IndexError:
				pass
		else:
			pass
			
print(possibleMoves)