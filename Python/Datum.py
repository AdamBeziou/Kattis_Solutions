DM = input().split()
D = int(DM[0])
M = int(DM[1])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
m_key = {1:4, 2:7, 3:7, 4:3, 5:5, 6:1, 7:3, 8:6, 9:2, 10:4, 11:7, 12:2}

if m_key[M] + D <= 7:
	print(days[m_key[M] + D - 2])
else:
	print(days[(m_key[M] + D)%7 - 2])