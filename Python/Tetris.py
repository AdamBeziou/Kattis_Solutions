columnsPiece = input().split()
columns = int(columnsPiece[0])
piece = int(columnsPiece[1])

drop = 0

sequence = input().split()
sequence = [int(x) for x in sequence]

if piece == 1:
    drop += len(sequence)
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2] and sequence[i] == sequence[i+3]:
               drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 2:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1]:
               drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 3:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] + 1:
                drop += 1
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2] - 1:
                drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 4:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] - 1:
               drop += 1
            if sequence[i] == sequence[i+1] + 1 and sequence[i] == sequence[i+2] + 1:
                drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 5:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] - 1:
               drop += 1
            if sequence[i] == sequence[i+1] + 1:
                drop += 1
            if sequence[i] == sequence[i+1] + 1 and sequence[i] == sequence[i+2]:
                drop += 1
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2]:
                drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 6:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] + 2:
                drop += 1
            if sequence[i] == sequence[i+1]:
                drop += 1
            if sequence[i] == sequence[i+1] - 1 and sequence[i] == sequence[i+2] - 1:
                drop += 1
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2]:
                drop += 1
            else:
                pass
        except IndexError:
            break

elif piece == 7:
    for i in range(len(sequence)):
        try:
            if sequence[i] == sequence[i+1] - 2:
                drop += 1
            if sequence[i] == sequence[i+1]:
                drop += 1
            else:
                pass
        except IndexError:
            break

        try:
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2] + 1:
                drop += 1
            if sequence[i] == sequence[i+1] and sequence[i] == sequence[i+2]:
                drop += 1
            else:
                pass
        except IndexError:
            break

print(drop)
