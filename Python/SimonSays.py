num = int(input())
for i in range(num):
	com = input().split()
	if com[0] == "Simon" and com[1] == "says":
		print(' '.join(com[2:]))
	else:
		pass
