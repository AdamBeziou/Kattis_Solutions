length = int(input())
sequence = list(input())
scores = [0,0,0]
adrian = ['A', 'B', 'C']*length
bruno = ['B', 'A', 'B', 'C']*length
goran = ['C', 'C', 'A', 'A', 'B', 'B']*length

for i in range(length):
	if adrian[i] == sequence[i]:
		scores[0] += 1
	if bruno[i] == sequence[i]:
		scores[1] += 1
	if goran[i] == sequence[i]:
		scores[2] += 1
	else:
		pass
		
print(max(scores))
if scores[0] == max(scores):
	print("Adrian")
if scores[1] == max(scores):
	print("Bruno")
if scores[2] == max(scores):
	print("Goran")
else:
	pass