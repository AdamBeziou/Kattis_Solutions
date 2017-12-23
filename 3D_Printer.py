days = 0
models = 0
printers = 1

num = int(input())

while printers < num/2:
	printers = printers*2
	days += 1
	
while models < num:
	models += printers
	days += 1
	
print(days)


