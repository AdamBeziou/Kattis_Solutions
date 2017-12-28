RN = input().split()
R = int(RN[0])
N = int(RN[1])
booked_rooms = []
list_of_all_rooms = []
for i in range(1,R + 1):
	list_of_all_rooms.append(i)

for i in range(N):
	booked_rooms.append(int(input()))
	
if R == N:
	print("too late")
	
else:
	for i in range(len(booked_rooms)):
		list_of_all_rooms.remove(booked_rooms[i])
		
	print(list_of_all_rooms[0])