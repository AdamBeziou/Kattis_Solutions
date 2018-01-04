scores = []

for i in range(5):
	score = 0
	score_list = input().split()
	score_list = [int(x) for x in score_list]
	for i1 in range(len(score_list)):
		score += score_list[i1]
		
	scores.append(score)
	
print("%d %d" % (scores.index(max(scores)) + 1, max(scores)))