limit = int(input())
num = int(input())
final_mb = limit

for i in range(num):
	used = int(input())
	
	if used > limit:
		final_mb -= used - limit
	else:
		final_mb += limit - used
print(final_mb)