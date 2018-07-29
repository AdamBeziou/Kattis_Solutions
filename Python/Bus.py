testCases = int(input())

for i in range(testCases):
    numPassengers = 0
    stops = int(input())

    for j in range(stops):
        numPassengers += 1/2
        numPassengers *= 2

    print(int(numPassengers))