wordPointPair = {}

MN = input().split()

for i in range(int(MN[0])):
    wordPoint = input().split()
    wordPointPair[wordPoint[0]] = int(wordPoint[1])

for i in range(int(MN[1])):
    points = 0

    line = input().split()

    while " ".join(line) != ".":
        for word in line:

            if word in wordPointPair:
                points += wordPointPair[word]

        line = input().split()

    print(points)