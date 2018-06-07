for x in range(int(input())):
    decipheredMessage = []
    encodedMessage = list(input())
    squareLen = int((len(encodedMessage))**(1/2))
    encodedMessageSquare = []

    for i in range(squareLen):
        substring = []
        for j in range(squareLen):
            substring.append(encodedMessage.pop(0))
        encodedMessageSquare.append(substring)

    for i in range(squareLen):
        for j in range(squareLen):
            decipheredMessage.append(encodedMessageSquare[j][squareLen - i - 1])

    print(''.join(decipheredMessage))