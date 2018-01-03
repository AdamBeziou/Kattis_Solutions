num = int(input())
score = 0
scores = input().split()

for i in range(len(scores)):
	if int(scores[i]) == -1:
		num -= 1
	else:
		score += int(scores[i])
		
print(score/num)