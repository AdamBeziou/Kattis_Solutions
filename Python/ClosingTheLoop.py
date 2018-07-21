cases = int(input())

for i in range(cases):
    length = 0
    blueSegments = []
    redSegments = []

    numSegments = int(input())
    segments = input().split()

    for j in range(numSegments):
        if segments[j][-1] == "B":
            blueSegments.append(int(segments[j].split("B")[0]))
        else:
            redSegments.append(int(segments[j].split("R")[0]))
    
    blueSegments.sort(reverse = True)
    redSegments.sort(reverse = True)

    if len(blueSegments) > len(redSegments):
        for j in range(len(redSegments)):
            length += (redSegments[j] + blueSegments[j]) - 2
    else:
        for j in range(len(blueSegments)):
            length += (redSegments[j] + blueSegments[j]) - 2

    print("Case #%d: %d" % (i + 1, length))
