firstPolicy = 0
secondPolicy = 0
thirdPolicy = 0

preferenceList = input()
initialPosition = preferenceList[0]
preferenceList = preferenceList[1:]

for i in range(len(preferenceList)):
    if i == 0:
        if preferenceList[i] == "U" and initialPosition == "D":
            firstPolicy += 1
            secondPolicy += 2
            thirdPolicy += 1
        elif preferenceList[i] == "D" and initialPosition == "D":
            firstPolicy += 1
        elif preferenceList[i] == "U" and initialPosition == "U":
            secondPolicy += 1
        elif preferenceList[i] == "D" and initialPosition == "U":
            firstPolicy += 2
            secondPolicy += 1
            thirdPolicy += 1
    else:
        if preferenceList[i] == "D":
            firstPolicy += 2
        elif preferenceList[i] == "U":
            secondPolicy += 2

        if preferenceList[i] != preferenceList[i - 1]:
            thirdPolicy += 1

print(firstPolicy)
print(secondPolicy)
print(thirdPolicy)