NM = input().split()
N = int(NM[0])
M = int(NM[1])

if N > M:
	if N - M == 1:
		print("Dr. Chaz needs 1 more piece of chicken!")
	else:
		print("Dr. Chaz needs %d more pieces of chicken!" % (N - M))
else:
	if M - N == 1:
		print("Dr. Chaz will have 1 piece of chicken left over!")
	else:
		print("Dr. Chaz will have %d pieces of chicken left over!" % (M - N))