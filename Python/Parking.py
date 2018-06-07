totalPrice = 0
timeline = []

prices = input().split()
prices = [int(x) for x in prices]

firstTruckTimes = input().split()
firstTruckTimes = [int(x) for x in firstTruckTimes]
secondTruckTimes = input().split()
secondTruckTimes = [int(x) for x in secondTruckTimes]
thirdTruckTimes = input().split()
thirdTruckTimes = [int(x) for x in thirdTruckTimes]

totalTimeList = firstTruckTimes + secondTruckTimes + thirdTruckTimes
totalTimeList.sort()

for i in range(totalTimeList[len(totalTimeList) - 1]):
	timeline.append(0)

for i in range(firstTruckTimes[0], firstTruckTimes[1]):
	timeline[i] += 1

for i in range(secondTruckTimes[0], secondTruckTimes[1]):
	timeline[i] += 1

for i in range(thirdTruckTimes[0], thirdTruckTimes[1]):
	timeline[i] += 1

for i in range(len(timeline)):
	totalPrice += prices[timeline[i] - 1] * timeline[i]

print(totalPrice)