distance = 0

NP = input().split()
NP = [int(x) for x in NP]

listOfCars = input().split()
listOfCars = [int(x) for x in listOfCars]
listOfCars.sort()

for i, d in enumerate(listOfCars):
    distance = max(distance, (NP[1] * (1 + i)) - d)

print(distance + listOfCars[0])