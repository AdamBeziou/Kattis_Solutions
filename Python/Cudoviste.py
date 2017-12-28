def check_pattern(rows, columns, num):
	places = 0
	for i in range(rows - 1):
		for i1 in range(columns - 1):
			count = 0
			pointtl = (mapdict[i])[i1]
			if pointtl == "X":
				count += 1
			pointtr = (mapdict[i])[i1+1]
			if pointtr == "X":
				count += 1
			pointbl = (mapdict[i+1])[i1]
			if pointbl == "X":
				count += 1
			pointbr = (mapdict[i+1])[i1+1]
			if pointbr == "X":
				count += 1
			
			if pointtl == "#" or pointtr == "#" or pointbl == "#" or pointbr == "#" or count != num:
				pass
			else:
				places += 1
				
	print(places)
			


rows_columns = input().split()
rows_columns = [int(x) for x in rows_columns]
mapdict = {x: input() for x in range(rows_columns[0])}
check_pattern(rows_columns[0], rows_columns[1], 0)
check_pattern(rows_columns[0], rows_columns[1], 1)
check_pattern(rows_columns[0], rows_columns[1], 2)
check_pattern(rows_columns[0], rows_columns[1], 3)
check_pattern(rows_columns[0], rows_columns[1], 4)
