ABCD = input().split()
ABCD = [int(x) for x in ABCD]
PMG = input().split()
PMG = [int(x) for x in PMG]

for i in range(len(PMG)):
    dogs = 0

    for j in range(len(ABCD) // 2):
        switch = False

        timeElapsed = 0

        while timeElapsed < PMG[i]:
            switch = not switch
            
            if switch:
                timeElapsed += ABCD[j * 2]
            else:
                timeElapsed += ABCD[j * 2 + 1]

        if switch:
            dogs += 1

    if dogs == 0:
        print("none")
    elif dogs == 1:
        print("one")
    else:
        print("both")