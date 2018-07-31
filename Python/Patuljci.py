dwarfNums = []
dwarfSum = 0

for i in range(9):
	dwarfNum = int(input())
	dwarfSum += dwarfNum
	dwarfNums.append(dwarfNum)

dwarfDifference = dwarfSum - 100

for i in range(len(dwarfNums)):
	difference = dwarfDifference - dwarfNums[i]
	if difference in dwarfNums and dwarfNums.index(difference) != i:
		dwarfNums.remove(dwarfNums[i])
		dwarfNums.remove(difference)
		break

for i in dwarfNums:
	print(i)