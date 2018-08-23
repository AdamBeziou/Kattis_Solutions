vowels = ['a', 'e', 'i', 'o', 'u', 'y']

while True:
    words = int(input())

    if words == 0:
        break

    maxCount = 0
    maxWord = ""
    
    for i in range(words):
        count = 0
        word = input()

        for j, l in enumerate(word):
            if l in vowels and j != len(word) - 1 and word[j + 1] == l:
                count += 1

        if count >= maxCount:
            maxCount = count
            maxWord = word

    print(maxWord)



                
