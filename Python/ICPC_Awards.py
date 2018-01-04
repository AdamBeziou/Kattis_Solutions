teams = int(input())
universities = []
team_list = []

for i in range(teams):
	U_team = input().split()
	U = U_team[0]
	if U not in universities and len(team_list) < 12:
		universities.append(U)
		team_list.append(' '.join(U_team))
	else:
		pass
		
for i in range(len(team_list)):
	print(team_list[i])