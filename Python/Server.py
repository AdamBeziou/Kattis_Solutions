nt = input().split()
n = int(nt[0])
t = int(nt[1])

tasks = input().split()
tasks = [int(x) for x in tasks]

time = 0
num_of_tasks = 0
for i in range(len(tasks)):
	if time + tasks[i] <= t:
		num_of_tasks += 1
		time += tasks[i]
	else:
		break
print(num_of_tasks)