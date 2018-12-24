import sys

usedWords = []

while True:
    try:
        entry = input().split()
    except EOFError:
        break

    for word in entry:
        if word.lower() in usedWords:
            print(' . ')
        else:
            usedWords.append(word.lower())
            print(word)
