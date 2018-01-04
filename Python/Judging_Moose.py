lr = input().split()
l = int(lr[0])
r = int(lr[1])

if l == 0 and r == 0:
	print("Not a moose")
elif l > r:
	print("Odd %d" % (l*2))
elif r > l:
	print("Odd %d" % (r*2))
elif r == l:
	print("Even %d" % (l + r))
else:
	pass