distinct = 0
mod = []

for i in range(10):
	num = int(input())%42
	if num not in mod:
		mod.append(num)
		distinct += 1
	else:
		pass

print(distinct)