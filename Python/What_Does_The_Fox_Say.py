cases = int(input())

for i in range(cases):
    animalIdentificationList = []

    animalSounds = input().split()

    animalIdentification = input().split()

    while ' '.join(animalIdentification) != "what does the fox say?":
        animalIdentificationList.append(animalIdentification.pop())
        animalIdentification = input().split()

    for i in animalIdentificationList:
        while i in animalSounds:
            animalSounds.remove(i)

    print(' '.join(animalSounds))