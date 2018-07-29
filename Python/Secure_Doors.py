peopleInBuilding = []
commands = []
length = int(input())

for i in range(length):
    command = input().split()

    if command[0] == "entry":
        if command[1] not in peopleInBuilding:
            peopleInBuilding.append(command[1])
            commands.append(command[1] + " entered")
        else:
            commands.append(command[1] + " entered (ANOMALY)")
        
    else:
        if command[1] in peopleInBuilding:
            peopleInBuilding.remove(command[1])
            commands.append(command[1] + " exited")
        else:
            commands.append(command[1] + " exited (ANOMALY)")

for i in commands:
    print(i)
