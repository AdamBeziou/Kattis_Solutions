frag = ['apa','epe','ipi','opo','upu']
vowel = ['a','e','i','o','u']
sentence = input().split()
sentence = [list(x) for x in sentence]
new_sentence = []
for i in range(len(sentence)):
	for i1 in range(len(sentence[i])):
		if sentence[i][i1] in vowel:
			try:
				sentence[i][i1 + 1] = ''
			except IndexError:
				pass
			try:
				sentence[i][i1 + 2] = ''
			except IndexError:
				pass
		else:
			pass
	new_sentence.append(''.join(sentence[i]))
	
print(' '.join(new_sentence))