cases = int(input())
for i in range(cases):
	students_scores = input().split()
	students_scores = [int(x) for x in students_scores]
	students = students_scores.pop(0)
	
	total = 0
	for i1 in range(students):
		total += students_scores[i1]
	avg = total/students
	
	ab_avg = 0
	for i2 in range(students):
		if students_scores[i2] > avg:
			ab_avg += 1
		else:
			pass
			
	print("%s" % (format(ab_avg/students, '.3%')))