num_cases = int(input())

for i in range(num_cases):
	votes_candidate = []
	total_votes = 0
	num_of_candidates = int(input())
	
	for i1 in range(num_of_candidates):
		candidate_votes = int(input())
		total_votes += candidate_votes
		votes_candidate.append(candidate_votes)
		
	test = False
	winner = max(votes_candidate)
	for i1 in range(num_of_candidates):
		if winner == votes_candidate[i1]and i1 != votes_candidate.index(winner):
			test = True
		else:
			pass
			
	if test == False and total_votes/2 < winner:
		print("majority winner %d" % (votes_candidate.index(winner) + 1))
	elif test == False:
		print("minority winner %d" % (votes_candidate.index(winner) + 1))
	else:
		print("no winner")