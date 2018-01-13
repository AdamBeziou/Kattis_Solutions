K = int(input())
A = 1
B = 0

for i in range(K):
	B_add = 0
	A_add = 0
	
	B_add += A
	A = 0
		
	A_add += B
	B_add += B
	B = 0
	
	B += B_add
	A += A_add
		
print("%d %d" % (A,B))