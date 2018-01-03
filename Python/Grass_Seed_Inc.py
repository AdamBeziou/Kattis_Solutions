cost = float(input())
num_lawns = int(input())
total_cost = 0

for i in range(num_lawns):
	lw = input().split()
	area = float(lw[0]) * float(lw[1])
	total_cost += area*cost
	
print(total_cost)