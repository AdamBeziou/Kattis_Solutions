cfull = {'thou':1,'inch':2, 'foot':3, 'yard':4, 'chain':5, 'furlong':6, 'mile':7, 'league':8}
cacro = {'th':1, 'in':2, 'ft':3, 'yd':4, 'ch':5, 'fur':6, 'mi':7, 'lea':8}
full = {1:1000.0, 2:12.0, 3:3.0, 4:22.0, 5:10.0, 6:8.0, 7:3.0}

compare = input().split()

if compare[1] in cfull:
	cfirst = cfull[compare[1]]
else:
	cfirst = cacro[compare[1]]

if compare[3] in cfull:
	csecond = cfull[compare[3]]
else:
	csecond = cacro[compare[3]]
	
value = float(compare[0])

c = csecond - cfirst

if c == 0:
	print(value)
	
elif c < 0:
	for i in range(csecond, cfirst):
		value = value * full[i]
	print(value)
	
else:
	for i in range(cfirst, csecond):
		value = value / full[i]
	print(value)