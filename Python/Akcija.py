num = int(input())
books = []
groups = []
price = 0

for i in range(num):
	books.append(int(input()))
	
books.sort(reverse = True)

count = 0
for i in range(len(books)):
	if count <= 1:
		price += books[i]
		count += 1
	else:
		count = 0

print(price)
