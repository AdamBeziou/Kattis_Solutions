cases = int(input())

for i in range(cases):
    presses = []
    backspaces = 0
    targetWord = list(input())
    writtenWord = list(input())

    while writtenWord != targetWord[:len(writtenWord)] or len(writtenWord) > len(targetWord):
        writtenWord.pop()
        backspaces += 1
    presses.append(len(targetWord) - len(writtenWord) + backspaces)

    for i in range(3):
        backspaces = 0
        sug = list(input())
        while sug != targetWord[:len(sug)] or len(sug) > len(targetWord):
            sug.pop()
            backspaces += 1
        presses.append(len(targetWord) - len(sug) + 1 + backspaces)

    presses.sort(reverse = True)

    print(presses.pop())