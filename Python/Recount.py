nameVotes = {}
name = ""

while name != "***":
    name = input()
    if name == "***":
        break
    elif name not in nameVotes:
        nameVotes[name] = 1
    else:
        nameVotes[name] = nameVotes[name] + 1

sortedCandidates = sorted(nameVotes.items(), key = lambda x: x[1])
if len(sortedCandidates) > 1 and sortedCandidates[-1][1] == sortedCandidates[-2][1]:
    print("Runoff!")
else:
    print(sortedCandidates.pop()[0])


    