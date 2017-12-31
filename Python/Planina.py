iterations = int(input())
rows_columns = 2

for i in range(iterations):
	rows_columns += 2**i

print(rows_columns*rows_columns)