tri = input().split()
tri = [int(x) for x in tri]
one = tri[0]
two = tri[1]
three = tri[2]

if one + two == three:
	print("%d+%d=%d" % (one, two, three))
	
elif two + three == one:
	print("%d=%d+%d" % (one, two, three))
	
elif one - two == three:
	print("%d-%d=%d" % (one, two, three))
	
elif two - three == one:
	print("%d=%d-%d" % (one, two, three))
	
elif one // two == three:
	print("%d/%d=%d" % (one, two, three))
	
elif two // three == one:
	print("%d=%d/%d" % (one, two, three))
	
elif one * two == three:
	print("%d*%d=%d" % (one, two, three))
	
elif two * three == one:
	print("%d=%d*%d" % (one, two, three))