animals = 1
listNum = 1

while animals != 0:
    animalList = {}
    animals = int(input())

    for i in range(animals):
        animal = input().split()[-1].lower()

        if animal in list(animalList):
            animalList[animal] += 1
        else:
            animalList[animal] = 1

    if animals != 0:
        print("List {}:".format(listNum))

    for i in sorted(list(animalList)):
        print("{} | {}".format(i, animalList[i]))

    listNum += 1
